#!/usr/bin/python

####################################################

#   	MassGrabber(Mass Admin Panel Finder)	   #

#    		Author: Viper 1337		   #

# Tested On: Windows 7,8,8.1,10 Ubuntu 14.04,16.04 #

####################################################



import urllib2

import time

import sys	



flag = 0 # A Flag to varify if no admin panel found

banner = '''


  __  __                _____           _     _                __      ___                   __ ____ ____ ______ 
 |  \/  |              / ____|         | |   | |               \ \    / (_)                 /_ |___ \___ \____  |
 | \  / | __ _ ___ ___| |  __ _ __ __ _| |__ | |__   ___ _ __   \ \  / / _ _ __   ___ _ __   | | __) |__) |  / / 
 | |\/| |/ _` / __/ __| | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|   \ \/ / | | '_ \ / _ \ '__|  | ||__ <|__ <  / /  
 | |  | | (_| \__ \__ \ |__| | | | (_| | |_) | |_) |  __/ |       \  /  | | |_) |  __/ |     | |___) |__) |/ /   
 |_|  |_|\__,_|___/___/\_____|_|  \__,_|_.__/|_.__/ \___|_|        \/   |_| .__/ \___|_|     |_|____/____//_/    
                                                                          | |                                    
                                                                          |_|                                    
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868

'''

print(banner)

sap = "-" * 69

################GLOBALS########################

site = [] # initiation of site list

panel = [] # initiation of panel list

sitelen = '' #initalizing sites count

length = '' # initializing panel count

TTD = 0.4 # Time dilay change it for max speed

###############################################

try:

	out = open('shariq.txt','w')

except IOError as error:

	print("[Error] Failed to open file!")

	sys.exit("Exiting ...")

def urlFix(url): #Fix URL if http or https missing

        if "http://" in url or "https://" in url:

                return url



        return "http://" + url

def SiteLists():

	global site

	sitelist = raw_input("Enter Sites List: ")

	try:

		with open(sitelist) as sites:

			for each in sites:

				grab2 = each.rstrip() # will remove end of line \n

				site.append(grab2)

		for a in site:

			tar = a

	except KeyboardInterrupt:

		sys.exit("\n[User Interrupt] : Exiting .. ")



	except IOError as error:

		print("[Error]   : %s not found" % sitelist)

		sys.exit("Exiting... ")	

def PanelLists():

	global panel

	wordlist = raw_input("Enter WordList: ")

	try:

		with open(wordlist) as adm: # default open is 'r'

		

			print(sap)

			print("[Loading]      : Loading Panels & Sites..")

			time.sleep(TTD)



			for panels in adm:

				grab = panels.rstrip() # will remove end of line \n

				panel.append(grab)

	except KeyboardInterrupt:

		sys.exit("\n[User Interrupt] : Exiting .. ")



	except IOError as error:

		print("[Error]        : %s not found" % wordlist)

		sys.exit("Exiting... ")

def ListsValidity():

	global site,panel,sitelen,length,out

	tarlength = len(site)

	print("[Sites]        : %d Sites Loaded.." % tarlength)

	time.sleep(TTD)



	badlength = len(panel)

	print("[Panels]       : %d Panels Loaded.." % badlength)

	time.sleep(TTD)

	

	panel = list(set(panel)) # this will remove duplicates [a set has no duplicates]

	site = list(set(site))



	sitelen = len(site)

	length = len(panel)

	print("[Using Sites]  :"),

	print("%d/%d Sites being used (%d duplicates).." % (sitelen, tarlength, tarlength - sitelen))



	print("[Using Panels] :"),

	print("%d/%d Panels being used (%d duplicates).." % (length, badlength, badlength - length))

	output = '''

	=====================================

	    	 MassGrabber Results         

		Total Sites    =  '''+str(sitelen)+'''

		Total Payloads =  '''+str(length)+'''

	=====================================

	'''

	out.write(output)

def MassGrabber():

	global flag,out

	

	counter = 0

	if sitelen > 0 and length >0:

		for a in site:

			tar = a

			counter +=1

			try:



				url = urlFix(tar)

				ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"

				header = {'User-Agent' : ua}



				req = urllib2.Request(url, None, header)

				resp = urllib2.urlopen(req)



				print(sap)

				out1 = "[Connecting] : %s..." % url

				print(out1)

				out.write("\n" + sap + "\n" + out1 + "\n")

				if resp.code == 200:

					time.sleep(TTD)

					out2 = "[Connected]  : %s is connected" % url

					print(out2)

					out.write(out2 + "\n")

					time.sleep(TTD)

					out3 = "[Checking %d/%d] : Checking %s \n" %(counter, sitelen, url)

					print(out3)

					out.write(out3 + "\n")



			except KeyboardInterrupt:

				sys.exit("\n[User Interrupt] : Exiting .. ")



			except:

				print(sap)

				out4 = "[Connecting] : %s" % url

				print(out4)

				out.write("\n" + sap + "\n" + out4 + "\n")

				time.sleep(TTD)

				out5 = "[Failed] : %s is offline or invalid URL\n" % url

				print(out5)

				out.write(out5 + "\n")



				flag = 0



			try:

				for x in panel:

					x = "/" + x

					payload = url + x

					try:

						#correction of duplication of http or https

						payload = payload.replace("//", "/")

						payload = payload.replace("http:/", "http://")

						payload = payload.replace("https:/", "https://")



						plreq = urllib2.Request(payload, None, header)

						plresp = urllib2.urlopen(plreq)



						if plresp.code == 200: #show pages with proper response

							flag = 1

							out6 = "[OK] : %s" % payload

							print(out6)

							out.write(out6 + "\n")



						elif plresp.code == 302: #show redirected pages

							flag = 1

							out7 = "[FOUND] : %s" % payload

							print(out7)

							out.write(out7 + "\n")



						elif plresp.code == 403: #show Forbbiden pages

							flag = 1

							out8 = "[FORBBIDEN] : %s" % payload

							print(out8)

							out.write(out8 + "\n")





					except KeyboardInterrupt:

						sys.exit("\n[User Interrupt] : Exiting .. ")



					except:

						continue

				

				if not flag:

					out9 = "[NO PANEL] : No Panel Found.. "

					print(out9)

					out.write(out9)

				else:

					pass







			except KeyboardInterrupt:

				sys.exit("\n[User Interrupt] : Exiting .. ")

	

	else:

		print(sap)

		print("[Error]    : Enter a valid list ..")	

	





def Main():

	SiteLists()

	PanelLists()

	ListsValidity()

	MassGrabber()

	p.close()

	print(sap)

	print("[Task Complete] : Results are saved into shariq.txt")

if __name__ == "__main__":

	Main()