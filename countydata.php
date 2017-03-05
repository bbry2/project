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


$path = '/usr/bin';
putenv("PYTHONPATH=$path");
apache_setenv("PYTHONPATH", "$path");
//$db = new SQLite3('data1215-full.db');
$county_state = $_GET['county'];
$command2 = "python3 generate_county_page.py" . " \"" . $county_state . "\" " . "2>&1";
//echo $command2;
$pid = popen($command2, "r");
while( !feof( $pid ) )
{
echo fread($pid, 256);
flush();
ob_flush();
usleep(100000);
}
pclose($pid);

/*#county= has space between each world (e.g. county = Orange County FL)
$state = substr($county_state, -2);
$county = substr($county_state, 0, -3);
echo "<h1> Data for " . $county . ", " . $state . "</h1> <br>";
//Remove LIMIT 1 to show/do this to all results.
$command ="SELECT * FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code  WHERE e.county =\"" . $county . "\" AND e.state=\"" . $state ."\";";
//echo $command;
if(!$db){
    echo $db->lastErrorMsg();
}
$result = $db->query($command);

$row = $result->fetchArray();
$output = "<tr>";

$count = 0;
foreach(array_keys($header_list) as $key){
    if($count < 8){
        $output = $output . "<th>" .  $header_list[$key] . "</th>";
        $count = $count + 1;
    }
}
$count = 0;
$output = $output . "</tr> <tr>";
foreach(array_keys($row) as $key){
    if($count < 8){
        if(is_numeric($key) && $key > 2){
            $output = $output . "<td>" . $row[$key] . "</td>";
            $count = $count + 1;
        }
    }
}
echo "</tr><table>" . $output;*/
/*while($row = $result->fetchArray()){
    $output = $output . "<td>" . $row[$key] . "</td>";
  }
  $output = $output . "</tr>";
  echo $output;
}
*/
// Echo page content
//echo $row['content'];
?>