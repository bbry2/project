<?php /* County Page Template - Ryan Hopkins */ ?> 
<!-- Page for county data -->
<head>
<title>County Data</title>
</head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 4px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>

<?php
/*Updating data: no changes needed*/

$path = '/usr/bin';
putenv("PYTHONPATH=$path");
apache_setenv("PYTHONPATH", "$path");
$county_state = $_GET['county'];
$command2 = "python3 generate_county_page.py" . " \"" . $county_state . "\"";
$pid = popen($command2, "r");
while( !feof( $pid ) )
{
echo fread($pid, 256);
flush();
ob_flush();
usleep(100000);
}
pclose($pid);
?>