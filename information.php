<?php ?>
<!-- Adding Data: Add the variable names and descriptions below. -->
<div id="primary">
<h1> Information and Sources </h1>
<h2> Election Data </h2>
<h3> Election data from user <i>tonmcg</i> on Github: <a href="https://github.com/tonmcg/US_Elections_Results">Link</a></h3>
<a name="FIPSCODE"></a> <b> fips_code </b>: State-County FIPS code <br>
<li>  The State-County FIPS code is a unique ID assigned to every county in the United States. 
<br> The first two numbers identify the state, the following three identify the county within the state.  </li> 
<b> state </b>: Name of state <br>
<b> county </b>: Name of county <br>
<b> total_<year> </b>: Number of total voters in [year] <br>
<b> dem_[year] </b>: Number of votes for the democratic canidate in [year] <br>
<b> gop_[year] </b>: Number of votes for republican canidate in [year] <br>
<b> oth_[year] </b>: Number of votes for third party candidates in [year] <br>
<b> dem_[year]_perc </b>: Percent of votes for the democratic canidate in [year] <br>
<b> gop_[year]_perc </b>: Percent of votes for the republican canidate in [year] <br>
<b> oth_[year]_perc </b>: Percent of votes for third party candidates in [year] <br>
<b> win_marg_[year] </b>: dem_[year]_perc - gop_[year]_perc <br>
<b> winner_[year] </b>: 'Dem' if win_marg_[year] is positive, 'Gop' otherwise <br>
<b> diff_0812 </b>: win_marg_12 - win_marg_08 <br>
<b> direction_0812 </b>: 'Dem' if diff_0812 is positive, 'Gop' otherwise <br>
<b> diff_1216 </b>: win_marg_16 - win_marg_12 <br>
<b> direction_1216 </b>: 'Dem' if diff_1216 is positive, 'Gop' otherwise <br>
<b> diff_0816 </b>: win_marg_16 - win_marg_08 <br>
<b> direction_0816 </b>: 'Dem' if diff_0816 is positive, 'Gop' otherwise <br>
<h3> Demographic Data </h3>
<h4>All data is from United States Government agencies </h4>
<h5> Find more data at the United States Census Bureau's <a href="https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml">Fact Finder</a> and <a href="https://data.gov">Data.gov</a></h5>
<b> fips_code </b>: <a href="#FIPSCODE">State-County FIPS code</a>  <br>
<b> county </b>: Name of county <br>
<b> population </b>: Total population <br>
<b> health_cov </b>: Population covered by Medicare <br>
<b> health_cov_per </b>: Percent of population covered by Medicare <br>
<b> median_age </b>: Median age <br>
<b> median_inc </b>: Median income (by household) <br>
<li> For more income and poverty data and an interactive map, see <a href="https://www.census.gov/did/www/saipe/data/">US Census SAIPE Data</a>  <br>
<b> gini </b>: Gini index coefficient; a measure of weatlh <br>
<li> Ranges from 0 to 1, 1 being the most unequal and 0 being least. See <a href="https://en.wikipedia.org/wiki/Gini_coefficient">here</a> for more.</li> 
<b> manu_per </b>: Percent labor force employed in manufacturing <br>
<li> Reported on American Community Survey, see the ACS program <a href="https://www.census.gov/programs-surveys/acs/">here</a> <br>
<b> salary_workers </b>: Percent labor force employed in salaried occupations <br>
<li> Reported on American Community Survey, see the ACS program <a href="https://www.census.gov/programs-surveys/acs/">here</a> <br>
<b> self_employed real </b>: Percent labor force self-employed <br>
<li> Reported on American Community Survey, see the ACS program <a href="https://www.census.gov/programs-surveys/acs/">here</a> <br>
<b> pop_citizen </b>: Total U.S. citizen population <br>
<b> cit_by_nat </b>: Total naturalized citizen population <br>
<b> cit_by_nat_per </b>: Percent of citizens how were naturalizaed <br>
<b> not_cit </b>: Number of non-U.S. Citizens <br>
<b> not_cit_per </b>: Percent of population non-U.S. citizens <br>
<b> bach_or_higher_per </b>: Percent of population with Bachelor's degree or higher educational attainment <br>
<li> Uses population at the age of 25 or older with Bachelor's degree. See how this compares to the United States as a whole  <a href="https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_15_1YR_S1501&prodType=table">here</a>. <br> 
<b> less_than_hs_per </b>: Percentage of people with educational attainment less than a high-school degree <br>
<li> Uses population at the age of 25 or older with Bachelor's degree. See how this compares to the United States as a whole  <a href="https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_15_1YR_S1501&prodType=table">here</a>. <br> 
<b> male_pop </b>: Total male population <br>
<b> male_per </b>: Percent of population male <br>
<b> female_pop </b>: Total female population <br>
<b> female_per </b>: Percent of population female <br>
<b> unemployment </b>: Percent of population unemployed and over 25 years old <br>
<b> poverty </b>: Percentage of households in poverty <br>
<b> white_per </b>: Percent of population identifying their race as "white" (This includes those identifying ethinicty as "Hispanic")<br>
<b> black_per </b>: Percent of population identifying their race as "white" <br>
<b> asian_per </b>: Percent of population identifying their race as "white" <br>
<b> hispanic_per </b>: Percent of population identifying their ethnicity as "white" <br>

<h3> Unemployment Data </h3>
<h4>Data is from United States Census Bureau, Bureau of Labor Statistics, and the USDA </h4>
<b> fips_code </b>: <a href="#FIPSCODE">State-County FIPS code</a>  <br>
<b> state </b>: Name of state <br>
<b> area_name </b>: Name of county <br>
<b> civilian_labor_force_[year] </b>: Number of people in civilian labor force in [year] <br>
<li> Civilian labor force annual average. Find more at <a href="http://www.bls.gov/lau/">BLS Data</a> See <a href="#Notes">Notes</a>. <br>
<b> unemployed_[year] </b>: Number of unemployed people in [year] <br>
<li> Number unemployed annual average (U-3). Find more at <a href="http://www.bls.gov/lau/">BLS Data</a> See <a href="#Notes">Notes</a>. <br>
<b> unemployment_rate_[year] </b>: <year> unemployment rate <br>
<li> Unemployment rate (U-3). Find more at <a href="https://www.bls.gov/lau/#cntyaa">BLS Data at the county level</a>.  See <a href="#Notes">Notes</a>. <br>
<b> unemployment_rate_difference_2008_to_2015 </b>: unemployment_rate_2015 - unemployment_rate_2008 <br>
<b> unemployment_rate_difference_2012_to_2015 </b>: unemployment_rate_2015 - unemployment_rate_2012 <br>
<b> labor_Force_Percent_Difference_2008_to_2015 </b>: Difference in labor force participation rate from 2008-2015 <br>
<b> labor_Force_Percent_Difference_2012_to_2015 </b>: Difference in labor force participation rate from 2012-2015
<br>
<br>
<b> Notes:</b> <a name="Notes"></a> The Bureau of Labor Statistics revised its estimation methodology for 
unemployment data in spring 2014, affecting 2015 data. See <a href="https://www.bls.gov/lau/substate_unemp.pdf">BLS Estimation Change PDF</a>  for more.
We do not feel that this change impacts the results or skews analysis.
<br>
See <a href="https://www.bls.gov/cps/eetech_intro.pdf"> Employment methodology</a> for more on how employment data is measured.