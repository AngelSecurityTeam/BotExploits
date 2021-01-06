<?php
error_reporting(0);
session_start();
define('SENDINBOX_PATH', realpath(dirname(__FILE__)));
require_once("Modules/database.php");
require_once("Modules/wploit-modules.php");
require_once("Modules/sdata-modules.php");
require_once("Modules/scanner.php");

require_once("Exploit/default-admin.php");
require_once("Exploit/plugins-email-subscribers.php");
require_once("Exploit/plugins-gravityforms.php");
require_once("Exploit/wp-content-injection.php");
require_once("Exploit/magento-exploit.php");
/**
 * 
 * @nedjworgan@gmail.com
 * @[UPDATE] 29 December 2019
*/
class wploit
{
	function __construct()
	{

		mkdir("log");

		$this->wploit_modules 					= new wploit_modules;
		$this->database 						= new Database;
		$this->scanner 							= new Scanner;
		$this->ExploitDefaultAdmin 				= new ExploitDefaultAdmin;
		$this->Exploit_Plugins_emailsubscribers = new Exploit_Plugins_emailsubscribers;
		$this->Exploit_Plugins_gravityforms 	= new Exploit_Plugins_gravityforms;
		$this->Exploit_wp_content_injection 	= new Exploit_wp_content_injection;
		$this->Exploit_Magento 					= new Exploit_Magento;


	  	echo $this->wploit_modules->color("red","\n========================================================\r\n\n");
        echo $this->wploit_modules->color("red","┌─┐┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐ Version : 1\r\n");
		echo $this->wploit_modules->color("red","└─┐│  ├─┤││││││├┤ ├┬┘ \r\n");
		echo $this->wploit_modules->color("red","└─┘└─┘┴ ┴┘└┘┘└┘└─┘┴└─\r\n");
       	echo $this->wploit_modules->color("random","\r\n==> Scanner And Exploiter <===\r\n");
       	echo $this->wploit_modules->color("red","\n========================================================\r\n\n");

    

		#########################################
		$this->wploit_modules->delay 	= 0;
		$this->menu 					= $this->database->menu();
		$this->menu_exploit 			= $this->database->menu_exploit();
		#########################################
		foreach ($this->menu as $key => $value) {
			echo $this->wploit_modules->color("yellow","[+] Scanner [".$key."] ".$value['title']."\r\n");
		}
		echo $this->wploit_modules->color("red","\n========================================================\r\n\n");
		$select = $this->wploit_modules->stuck("Select Number : ");
		$threads = $this->wploit_modules->stuck("Thread : ");
		
		$this->wploit_modules->threads 	= $threads;
		
		switch ($this->menu[$select]['action']) {
			case 'wordpress_scanner_plugin':
				$this->scanner_plugins();echo "\r\n";
			break;
			case 'scanner_plugins_joomla':
				$this->scanner_plugins_joomla();echo "\r\n";
			break;
			case 'magento_exploit':
				$this->scanner_magento();echo "\r\n";
			break;
			case 'wordpress_exploit_plugin_themes':
				echo "\r\n";
				echo $this->wploit_modules->color("yellow","\n========================[ MENU EXPLOIT ]================\r\n\n");
				foreach ($this->menu_exploit as $key => $value) {
					echo $this->wploit_modules->color("reed","[+] Scanner [".$key."] ".$value['title']."\r\n");
				}
				echo $this->wploit_modules->color("yellow","\n========================================================\r\n\n");
				$select = $this->wploit_modules->stuck("Select Number : ");


				switch ($this->menu_exploit[$select]['action']) {
					case 'Email_Subscribers':
						$this->exploit_email_subscribers();
					break;
					case 'Gravity_Forms':
						$this->exploit_Gravity_Forms();
					break;
					case 'content_injection':
						$this->exploit_content_injection();
					break;
					default:
						die('!error!');
					break;
				}

			break;
			case 'scanner_cms_detector':
				$this->scanner_cms();echo "\r\n";
			break;
			case 'wordpress_exploit_defaultadmin':
				$this->exploit_defaultadmin();echo "\r\n";
			break;
			default:
				die('!error!');
			break;
		}
	}
	function filter_domain($urlS){
		$url = parse_url($urlS);
		$url = (!isset($url["scheme"]) ? "http://".$urlS : $url["scheme"]."://".$url["host"]);
		return $url;
	}

	function scanner_magento(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-magento-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$logScan 	  = ($logScan+1);
				$config_url[] =  array('url' => $this->filter_domain($url));
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->Exploit_Magento->scanner($config_url , "Line : ".$logScan." of ".ceil((count($dataConfig['list'])*$dataConfig['threads'])) ); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function scanner_plugins(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  = $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." ( ".(count($this->database->wordpress_plugins())*$dataConfig['threads'])." / Request ), Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-scannerPlugins-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				foreach ($this->database->wordpress_plugins() as $key => $dbPlugins) {
					$config_url[] =  array('url' => $this->filter_domain($url)."/".$dbPlugins , 'plugin' => $key);
				}
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->scanner->wordpress_plugins($config_url); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function scanner_plugins_joomla(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  = $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." ( ".(count($this->database->wordpress_plugins())*$dataConfig['threads'])." / Request ), Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-scannerPlugins-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				foreach ($this->database->joomla_plugins() as $key => $dbPlugins) {
					$config_url[] =  array('url' => $this->filter_domain($url)."/".$dbPlugins , 'plugin' => $key);
				}
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->scanner->joomla_plugins($config_url); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function scanner_cms(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}

		$logScan = 0;

		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-cmsdetector-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$logScan 	  = ($logScan+1);
				$config_url[] =  array('url' => $this->filter_domain($url) );
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->scanner->cms_detector($config_url , "Line : ".$logScan." of ".ceil((count($dataConfig['list'])*$dataConfig['threads']))  ); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function exploit_defaultadmin(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-defaultadmin-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$config_url[] =  array('url' => $this->filter_domain($url));
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->ExploitDefaultAdmin->scanner($config_url); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function exploit_email_subscribers(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-Exploit_Plugins_emailsubscribers-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$logScan 	  = ($logScan+1);
				$config_url[] =  array('url' => $this->filter_domain($url));
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->Exploit_Plugins_emailsubscribers->scanner($config_url , "Line : ".$logScan." of ".ceil((count($dataConfig['list'])*$dataConfig['threads'])) ); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function exploit_Gravity_Forms(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-Exploit_Plugins_Gravity_Forms-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$logScan 	  = ($logScan+1);
				$config_url[] =  array('url' => $this->filter_domain($url));
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->Exploit_Plugins_gravityforms->scanner($config_url , "Line : ".$logScan." of ".ceil((count($dataConfig['list'])*$dataConfig['threads'])) ); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
	function exploit_content_injection(){
		$dataConfig = $this->wploit_modules->required();
		$xselc  	= $this->wploit_modules->stuck("Total Request : ".(count($dataConfig['list'])*$dataConfig['threads'])." , Keep going ? [0 = NO , 1 = YES] : ");echo "\r\n";
		if($xselc == 0){
			die('!error!');
		}
		foreach ($dataConfig['list'] as $keys => $dataurl) {
			$fopn = fopen("log/log-Exploit_Plugins_Gravity_Forms-".$dataConfig['namafile'].".txt", "w");
			foreach ($dataurl as $ukey => $url) {
				$logScan 	  = ($logScan+1);
				$config_url[] =  array('url' => $this->filter_domain($url));
				fwrite($fopn, $ukey."|".$url."\r\n");
			}
			fclose($fopn);
			$this->Exploit_wp_content_injection->scanner($config_url , "Line : ".$logScan." of ".ceil((count($dataConfig['list'])*$dataConfig['threads'])) ); unset($config_url);
			sleep($dataConfig['delay']);
		}
	}
}
$wploit = new wploit;
$wploit->run();
