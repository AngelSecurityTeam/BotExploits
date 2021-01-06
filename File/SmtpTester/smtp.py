import smtplib,os,random,time
from time import strftime
from colorama import *
import sys
from optparse import OptionParser
import sys
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868
 
Note : domain|ip|user|pass



"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()
address =raw_input('Enter Ur Email Address: ')
a=raw_input('Enter List Smtp: ')
ob = open(a,'r')
lists = ob.readlines()
list1 = []
i = 0
for i in range(len(lists)):
  list1.append(lists[i].strip('\n'))
count = 0
for site in (list1):
 ur = site.rstrip()
 ch= ur.split('\n')[0].split('|')
 serveraddr=ch[0]
 toaddr=address
 fromaddr=ch[2]
 serverport=ch[1]
 SMTP_USER=ch[2]
 SMTP_PASS=ch[3]
 now = strftime("%Y-%m-%d %H:%M:%S")
 msg =  "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s"  % (fromaddr, toaddr, now, now)
 server = smtplib.SMTP()
 try:
  server.connect(serveraddr, serverport)
 except:
  print "FAILED ===> "+ur
  print '\n'  
  continue
 server.ehlo()
 server.ehlo()
 if SMTP_USER != "": 
  try: 
   server.login(SMTP_USER, SMTP_PASS)
  except:
    print "FAILED ===> "+ur
    print '\n' 
    continue
 server.sendmail(fromaddr, toaddr, msg)
 print "SUCCESS ===> "+ur+'\n' 
 zzz=open('Valid.txt','a')
 zzz.write(site+'\n')
 server.quit()
