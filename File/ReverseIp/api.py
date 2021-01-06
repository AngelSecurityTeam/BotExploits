import time,sys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
colorama.init()


# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
#coded by mister spy
#contact me 712083179
def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 

  ______               _     _   ____        _    __      ____ ___  
 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
logo()


taz = raw_input("IPS :")
with open(taz) as f :
    for i in f :

        req_proxy = RequestProxy()
        api = 'http://api.hackertarget.com/reverseiplookup/?q='+i
        try :
            request = req_proxy.generate_proxied_request(api)
            if request is not None:
                print("\t Response: ip={0}".format(u''.join(request.text).encode('utf-8')))
                save = open("Grabbed.txt","a")
                save.write(request.text + '\n')
                save.close()
                print "Ips : ==> " , i

        except :
            print "Dead Proxy"