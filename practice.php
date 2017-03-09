<?php
$r = 'python3 practcepy.py';
exec($r);
echo "hi";
$path = '/usr/bin';
putenv("PYTHONPATH=$path");
apache_setenv("PYTHONPATH", "$path");

$command2 = "python3 practcepy.py";
$pid = popen( $command2,"r");
while( !feof( $pid ) )
{
echo fread($pid, 256);
flush();
ob_flush();
usleep(100000);
}
pclose($pid);


$im = imagecreatefrompng("img.png");
header('Content-Type: image/png');
imagepng($im);
imagedestroy($im);
?>