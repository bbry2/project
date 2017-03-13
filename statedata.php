<?php /* Mapping Page Template - Ryan Hopkins */ ?> 
<!-- Page for state data -->

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
<head>
<title>State Data</title>
</head>

<?php
/*Updating data: no changes needed*/

$path = '/usr/bin';
putenv("PYTHONPATH=$path");
apache_setenv("PYTHONPATH", "$path");
$state = $_GET['state'];
$command2 = "python3 generate_state_page.py" . " \"" . $state . "\"";
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