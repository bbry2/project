<?php /* Mapping Page Template - Ryan Hopkins */ ?> 
<!-- Page for producing maps of US -->
 <head>
<title>Map Generator</title>
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
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
<div id="primary"> <div id="content" role="main"> </div><!-- #content -->
<form method="post" id="election_analysis" action="">
<h1> Map Generator </h1> 
<h3> Information about the data used as well as our sources can be found at our <a href="http://localhost/information.php">information page</a>. </h3>
<h5> See all of our tools <a href="http://localhost/elections.php">here</a>. </h5>

<h2> 1. Select States </h2>

<h4> <b> Check all states you'd like to see counties from: </b></h4>
<h5> <i> Leave state field blank to display all counties in the US </i> </h5> 

<li><label for="AL">AL</label> <input type="checkbox" name="AL" id="AL" value="AL">&emsp;<label for="AZ">AZ</label> <input type="checkbox" name="AZ" id="AZ" value="AZ">&emsp;<label for="AR">AR</label> <input type="checkbox" name="AR" id="AR" value="AR">&emsp;<label for="CA">CA</label> <input type="checkbox" name="CA" id="CA" value="CA">&emsp;<label for="CO">CO</label> <input type="checkbox" name="CO" id="CO" value="CO">&emsp;<label for="CT">CT</label> <input type="checkbox" name="CT" id="CT" value="CT">&emsp;<label for="DE">DE</label> <input type="checkbox" name="DE" id="DE" value="DE">&emsp;<label for="DC">DC</label> <input type="checkbox" name="DC" id="DC" value="DC">&emsp;<label for="FL">FL</label> <input type="checkbox" name="FL" id="FL" value="FL">&emsp;<label for="GA">GA</label> <input type="checkbox" name="GA" id="GA" value="GA">&emsp;<label for="HI">HI</label> <input type="checkbox" name="HI" id="HI" value="HI">&emsp;<label for="ID">ID</label> <input type="checkbox" name="ID" id="ID" value="ID">&emsp;<label for="IL">IL</label> <input type="checkbox" name="IL" id="IL" value="IL">&emsp;<label for="IN">IN</label> <input type="checkbox" name="IN" id="IN" value="IN">&emsp;<label for="IA">IA</label> <input type="checkbox" name="IA" id="IA" value="IA">&emsp;<label for="KS">KS</label> <input type="checkbox" name="KS" id="KS" value="KS">&emsp;<label for="KY">KY</label> <input type="checkbox" name="KY" id="KY" value="KY">&emsp;<li><label for="LA">LA</label> <input type="checkbox" name="LA" id="LA" value="LA">&emsp;<label for="ME">ME</label> <input type="checkbox" name="ME" id="ME" value="ME">&emsp;<label for="MD">MD</label> <input type="checkbox" name="MD" id="MD" value="MD">&emsp;<label for="MA">MA</label> <input type="checkbox" name="MA" id="MA" value="MA">&emsp;<label for="MI">MI</label> <input type="checkbox" name="MI" id="MI" value="MI">&emsp;<label for="MN">MN</label> <input type="checkbox" name="MN" id="MN" value="MN">&emsp;<label for="MS">MS</label> <input type="checkbox" name="MS" id="MS" value="MS">&emsp;<label for="MO">MO</label> <input type="checkbox" name="MO" id="MO" value="MO">&emsp;<label for="MT">MT</label> <input type="checkbox" name="MT" id="MT" value="MT">&emsp;<label for="NE">NE</label> <input type="checkbox" name="NE" id="NE" value="NE">&emsp;<label for="NV">NV</label> <input type="checkbox" name="NV" id="NV" value="NV">&emsp;<label for="MH">MH</label> <input type="checkbox" name="MH" id="MH" value="MH">&emsp;<label for="NJ">NJ</label> <input type="checkbox" name="NJ" id="NJ" value="NJ">&emsp;<label for="NM">NM</label> <input type="checkbox" name="NM" id="NM" value="NM">&emsp;<label for="NY">NY</label> <input type="checkbox" name="NY" id="NY" value="NY">&emsp;<label for="NC">NC</label> <input type="checkbox" name="NC" id="NC" value="NC">&emsp;<li><label for="ND">ND</label> <input type="checkbox" name="ND" id="ND" value="ND">&emsp;<label for="OH">OH</label> <input type="checkbox" name="OH" id="OH" value="OH">&emsp;<label for="OK">OK</label> <input type="checkbox" name="OK" id="OK" value="OK">&emsp;<label for="OR">OR</label> <input type="checkbox" name="OR" id="OR" value="OR">&emsp;<label for="PA">PA</label> <input type="checkbox" name="PA" id="PA" value="PA">&emsp;<label for="RI">RI</label> <input type="checkbox" name="RI" id="RI" value="RI">&emsp;<label for="SC">SC</label> <input type="checkbox" name="SC" id="SC" value="SC">&emsp;<label for="SD">SD</label> <input type="checkbox" name="SD" id="SD" value="SD">&emsp;<label for="TN">TN</label> <input type="checkbox" name="TN" id="TN" value="TN">&emsp;<label for="TX">TX</label> <input type="checkbox" name="TX" id="TX" value="TX">&emsp;<label for="UT">UT</label> <input type="checkbox" name="UT" id="UT" value="UT">&emsp;<label for="VT">VT</label> <input type="checkbox" name="VT" id="VT" value="VT">&emsp;<label for="VA">VA</label> <input type="checkbox" name="VA" id="VA" value="VA">&emsp;<label for="WA">WA</label> <input type="checkbox" name="WA" id="WA" value="WA">&emsp;<label for="WV">WV</label> <input type="checkbox" name="WV" id="WV" value="WV">&emsp;<label for="WI">WI</label> <input type="checkbox" name="WI" id="WI" value="WI">&emsp;<label for="WY">WY</label> <input type="checkbox" name="WY" id="WY" value="WY">

<h2> 2. Display Maps </h2>
<h4> Display maps of selected variables by county in states selected. </h4>
<label for="map_vars1"></label>
<select name="map_vars1" id="map_vars1">
<option value="">--No Choice--</option>
<option value="W">Winning Party in 2016</option>
<option value="w">Winning Margin 2016</option>
<option value="d">Shift in Winning Margin between 2012 and 2016</option>
<option value="i">2012 to 2015 Difference in Median Income</option>
<option value="a">2012 to 2015 Difference in Median Age</option>
<option value="n">2012 to 2015 Difference in Percent of Population Not Citizens</option>
<option value="m">2012 to 2015 Difference in Percent Employment in Manufacturing</option>
<option value="u">2012 to 2015 Difference in Unemployment Rate</option>
</select>
<label for="map_vars2"></label>
<select name="map_vars2" id="map_vars2">
<option value="">--No Choice--</option>
<option value="W">Winning Party</option>
<option value="w">Winning Margin</option>
<option value="d">Shift in Winning Margin between 2012 and 2016</option>
<option value="i">2012 to 2015 Difference in Median Income</option>
<option value="a">2012 to 2015 Difference in Median Age</option>
<option value="n">2012 to 2015 Difference in Percent of Population Not Citizens</option>
<option value="m">2012 to 2015 Difference in Percent Employment in Manufacturing</option>
<option value="u">2012 to 2015 Difference in Unemployment Rate</option>
</select>

<br>
<br>
<input type="submit" value="submit" />
<br>
</form>

<?php

$only_county = 0;

$state_array = [$_POST["AL"], $_POST["AZ"], $_POST["AR"], $_POST["CA"], $_POST["CO"], $_POST["CT"], $_POST["DE"], $_POST["DC"], $_POST["FL"], $_POST["GA"], $_POST["HI"], $_POST["ID"], $_POST["IL"], $_POST["IN"], $_POST["IA"], $_POST["KS"], $_POST["KY"], $_POST["LA"], $_POST["ME"], $_POST["MD"], $_POST["MA"], $_POST["MI"], $_POST["MN"], $_POST["MS"], $_POST["MO"], $_POST["MT"], $_POST["NE"], $_POST["NV"], $_POST["MH"], $_POST["NJ"], $_POST["NM"], $_POST["NY"], $_POST["NC"], $_POST["ND"], $_POST["OH"], $_POST["OK"], $_POST["OR"], $_POST["PA"], $_POST["RI"], $_POST["SC"], $_POST["SD"], $_POST["TN"], $_POST["TX"], $_POST["UT"], $_POST["VT"], $_POST["VA"], $_POST["WA"], $_POST["WV"], $_POST["WI"], $_POST["WY"]];

//Filter by state
$count_where = 0;
foreach($state_array as $state) {
    if ($state != "") {
        $only_county = 0;
        if (!empty($_POST["county"])){
            $w_command = $w_command . "(e.state = '" . $state . "') OR ";
        }
        if (empty($_POST["county"])){
            if ($count_where < 1){
                $w_command = $w_command . "WHERE (e.state = '" . $state . "') OR ";
                $count_where = $count_where + 1;
            } else {
                $w_command = $w_command . "(e.state = '" . $state . "') OR ";
            }
        }
    }
}
if ($only_county != 1){
    $w_command = substr($w_command, 0, -4);
}
//Put together data filters


$path = '/usr/bin';
putenv("PYTHONPATH=$path");
apache_setenv("PYTHONPATH", "$path");
//Correlation Heat Map

//mapping the counties
if(!empty($_POST["map_vars1"]) && !empty($_POST["map_vars2"])){
    $command3 = "python2 plot_counties.py ";
    $command3 = $command3 . $_POST["map_vars1"] . $_POST["map_vars2"];
    foreach($state_array as $state){
    if(!empty($state)){
        $command3 = $command3 . " " . $state . " ";
    }
    //$command3 = $command3 . " 2>&1";
   } 
  $output = shell_exec($command3);
  echo $output;
}
?>


</div><!-- #primary --> <?php ?>

