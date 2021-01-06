#######################################################################
#FAST CMS CHECKER PYTHON SCRIPT
#Don't forget to put a star and read how to use script:
#https://github.com/KTN1990/Fast_CMS_Checker-Detector
#And Check for more tools and exploits
#@kill_the_net
#######################################################################
#SCRIPT:
#######################################################################


# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##KILL THE NET##
#### PS: CHANGE Your Threads pool on line 186 to make script more faster :)
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time				   		
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'		
#########################################################################################
def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]
	x = ''' 
				 
  ______               _     _   ____        _    __      ____ ___  
 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868
 '''

	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
		pass

logo()
try:
	spy =raw_input('List Of Sites Name :')
	with codecs.open(spy, mode='r', encoding='ascii', errors='ignore') as f:
		ooo = f.read().splitlines()
except IndexError:
	print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listip.txt' + CEND)
	pass
ooo = list((ooo))
##########################################################################################
se = requests.session()
Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def wordpress(url):
    try:
        path0 = se.get(url, headers=Agent, verify=False, timeout=50)
        path4 = se.get(url + '/license.txt', headers=Agent, verify=False, timeout=50)
        path5 = se.get(url + '/xmlrpc.php?rsd', headers=Agent, verify=False, timeout=50)
        if path4.status_code == 200:
            if 'WordPress' in path4.content.encode('utf-8'):
                print(ktn3yell + '#[-WORDPRESS CMS-]=========> ' + '(' + url + ')' + CEND)
                open('wordpress.txt', 'a').write(url + '\n')
        elif path5.status_code == 200:
            if 'WordPress' in path4.content.encode('utf-8'):
                print(ktn3yell + '#[+WORDPRESS CMS+]=========> ' + '(' + url + ')' + CEND)
                open('wordpress.txt', 'a').write(url + '\n')
        elif '/wp-includes/' in path0.content.encode('utf-8'):
            print(ktn3yell + '#[*WORDPRESS CMS*]=========> ' + '(' + url + ')' + CEND)
            open('wordpress.txt', 'a').write(url + '\n')
        else:
            print(ktnred + '#[-NOT WORDPRESS-]=========> ' + '(' + url + ')' + CEND)
        pass
    except:
        pass
    pass
def joomla(url):
    try:
        path1 = se.get(url + '/README.txt', headers=Agent, verify=False, timeout=50)
        path2 = se.get(url + '/robots.txt', headers=Agent, verify=False, timeout=50)
        path3 = se.get(url + '/language/en-GB/en-GB.xml', headers=Agent, verify=False, timeout=50)
        if path1.status_code == 200:
            if 'Joomla' in path1.content.encode('utf-8'):
                print(ktngreen + '#[-JOOMLA CMS-]=========> ' + '(' + url + ')' + CEND)
                open('joomla.txt', 'a').write(url + '\n')
        elif path2.status_code == 200:
            if 'Joomla' in path2.content.encode('utf-8'):
                print(ktngreen + '#[+JOOMLA CMS+]=========> ' + '(' + url + ')' + CEND)
                open('joomla.txt', 'a').write(url + '\n')
        elif path3.status_code == 200:
            if 'Joomla' in path3.content.encode('utf-8'):
                print(ktngreen + '#[*JOOMLA CMS*]=========> ' + '(' + url + ')' + CEND)
                open('joomla.txt', 'a').write(url + '\n')
        else:
            print(ktnred + '#[-NOT JOOMLA-]=========> ' + '(' + url + ')' + CEND)

    except:
        pass
    pass
def drupal(url):
    try:
        path0 = se.get(url, headers=Agent, verify=False, timeout=50)
        path6 = se.get(url + '/CHANGELOG.txt', headers=Agent, verify=False, timeout=50)
        if path6.status_code == 200 :
            if 'Drupal' in path6.content.encode('utf-8'):
                print(ktn4blue + '#[-DRUPAL CMS-]=========> ' + '(' + url + ')' + CEND)
                open('drupal.txt', 'a').write(url + '\n')
        elif '/sites/default/' in path0.content.encode('utf-8'):
            print(ktn4blue + '#[+DRUPAL CMS+]=========> ' + '(' + url + ')' + CEND)
            open('drupal.txt', 'a').write(url + '\n')
        else:
            print(ktnred + '#[-NOT DRUPAL-]=========> ' + '(' + url + ')' + CEND)
    except:
        pass
    pass
def prestashop(url):
    try:
        path0 = se.get(url, headers=Agent, verify=False, timeout=50)
        if 'content="PrestaShop"' in path0.content.encode('utf-8'):
            print(ktn5purp + '#[-PRESTASHOP CMS-]=========> ' + '(' + url + ')' + CEND)
            open('Prestashop.txt', 'a').write(url + '\n')
            pass
        else:
            print(ktnred + '#[-NOT PRESTASHOP-]=========> ' + '(' + url + ')' + CEND)
        pass
    except:
        pass
    pass
def magento(url):
    try:
        path7 = se.get(url + '/user/login', headers=Agent, verify=False, timeout=50)
        path0 = se.get(url, headers=Agent, verify=False, timeout=50)
        if 'magento' in path0.content.encode('utf-8') or 'Magento' in path0.content.encode('utf-8'):
            print(ktn7grey + '#[-MAGENTO CMS-]=========> ' + '(' + url + ')' + CEND)
            open('magento.txt', 'a').write(url + '\n')
            pass
        elif path7.status_code == 200:
            if 'Magento' in path7.content.encode('utf-8'):
                print(ktn7grey + '#[+MAGENTO CMS+]=========> ' + '(' + url + ')' + CEND)
                open('magento.txt', 'a').write(url + '\n')
                pass
            pass
        else:
            print(ktnred + '#[-NOT MAGENTO-]=========> ' + '(' + url + ')' + CEND)
        pass
    except:
        pass
    pass
def opencart(url):
    try:
        path0 = se.get(url, headers=Agent, verify=False, timeout=50)
        if 'catalog/view/' in path0.content.encode('utf-8'):
            print(ktn6blueblue + '#[-OPENCART CMS-]=========> ' + '(' + url + ')' + CEND)
            open('Opencart.txt', 'a').write(url + '\n')
            pass
        else:
            print(ktnred + '#[-NOT OPENCART-]=========> ' + '(' + url + ')' + CEND)
        pass
    except:
        pass
    pass
def checkrpns(url):
    try:
        kill1 = se.get(url, headers=Agent, verify=False, timeout=50)
        if kill1.status_code == 200:
            wordpress(url)
            joomla(url)
            drupal(url)
            prestashop(url)
            magento(url)
            opencart(url)
            pass
        else:
            print(ktnred + '#[-DEAD SITE-]=========> ' + '(' + url + ')' + CEND)
        pass
    except:
        pass
    pass
##########################################################################################



##########################################################################################
def Main():
	try:
		
		start = timer()
		ThreadPool = Pool(150)
		Threads = ThreadPool.map(checkrpns, ooo)
		print('TIME TAKE: ' + str(timer() - start) + ' S')
	except:
		pass


if __name__ == '__main__':
	Main()