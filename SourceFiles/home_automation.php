<html >
<!-- Datei /var/www/fernbedienung .php -->
<head >
</head >
<body >
<h1 align ="center ">Funk -Fernbedienung </h1 >
<?php
 echo "<p> Datum: " . date("j.n.Y H:i", time());
echo '<pre>';
exec('gpio -1 mode 26 out');

 
if(isset ($_GET ['command'])) {
	if($_GET ['command'] === 'sd-an') {
		$val = trim(@shell_exec (
		"/home/pi/Desktop/home_system.py"));
	}
	elseif ($_GET ['command'] === 'sd-aus') {
		$val = trim(@shell_exec (
		"touch /var/www/html/stop_script"));
	}
	elseif ($_GET ['command'] === 'light-on') {
		$val =trim(@shell_exec(
			"/home/pi/433Utils/RPi_utils/codesend 1377617 24"));
	}
	elseif ($_GET ['command'] === 'light-off') {
		$val =trim(@shell_exec(
			"/home/pi/433Utils/RPi_utils/codesend 1377620 24"));
	}
}
?>
<div align ="center ">
<a href ="<?php print ($_SERVER['PHP_SELF ']); ?>? command=sd-an">
Home system on</a>
<br>
<a href ="<?php print ($_SERVER['PHP_SELF ']); ?>? command=sd-aus">
Home system off</a>
</div>


<br>
<a href="<?php print($_SERVER['PHP_SELF ']); ?>?command=light-on">
Light on</a>
<br>
<a href="<?php print($_SERVER['PHP_SELF ']); ?>?command=light-off">
Light off</a>
</div>


</body >
</html >
