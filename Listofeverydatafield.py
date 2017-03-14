#Used to store the labels and SQLite3 calls for the data. 

list1 = ["Total 2008 Votes",
"Total 2012 Votes",
"Total 2016 Votes",
"Democratic Votes 2008",
"Republican Votes 2008",
"Third Party Votes 2008",
"Percentage Democratic Votes 2008",
"Percentage Republican Votes 2008",
"Percentage Third Party Votes 2008",
"2008 Winner",
"Percentage Winning Margin 2008",
"Democratic Votes 2012",
"Republican Votes 2012",
"Third Party Votes 2012",
"Percentage Democratic Votes 2012",
"Percentage Republican Votes 2012",
"Percentage Third Party Votes 2012",
"2012 Winner",
"Percentage Winning Margin 2012",
"Democratic Votes 2016",
"Republican Votes 2016",
"Third Party Votes 2016",
"Percentage Democratic Votes 2016",
"Percentage Republican Votes 2016",
"Percentage Third Party Votes 2016",
"2016 Winner",
"Percentage Winning Margin 2016",
"Winning Percentage 2008 to 2012",
"Winning Percentage 2008 to 2016",
"Winning Percentage 2012 to 2016",
"2008 Unemployment Rate",
"2012 Unemployment Rate",
"2015 Unemployment Rate",
"2008 Total Unemployment",
"2012 Total Unemployment",
"2015 Total Unemployment",
"Difference in Unemployment Rate 2008 to 2015",
"Difference in Unemployment Rate 2012 to 2015",
"Civilian Labor Force in 2008",
"Civilian Labor Force in 2012",
"Civilian Labor Force in 2015",
"Difference in Labor Force Participation Rate 2008 to 2015",
"Difference in Labor Force Participation Rate 2012 to 2015",
"Total Population in 2012",
"Median Age in 2012",
"Health Coverage in 2012",
"Health Coverage Percent 2012",
"Male Population in 2012",
"Percent of Population Male in 2012",
"Female Population in 2012",
"Percent of Population Female in 2012",
"Percent of Population in Poverty in 2012",
"Median Income in 2012",
"Gini Coefficient in 2012",
"Percent Employment in Manufacturing 2012",
"Percent of Workers on Salary in 2012",
"Percent of Workers Self-Employed in 2012",
"Population of Citizens in 2012",
"Population of Non-Citizens in 2012",
"Population of Naturalized Citizens in 2012",
"Citizen by Naturalization Percent 2012",
"Percentage of Non-Citizens in 2012",
"Percent of Population with a Bachelor's Degree or Higher in 2012",
"Percent of Population with Less Than High School Degree in 2012",
"Total Population in 2015",
"Median Age in 2015",
"Health Coverage in 2015",
"Health Coverage Percent 2015",
"Male Population in 2015",
"Percent of Population Male in 2015",
"Female Population in 2015",
"Percent of Population Female in 2015",
"Percent of Population in Poverty in 2015",
"Median Income in 2015",
"Gini Coefficient in 2015",
"Percent Employment in Manufacturing in 2015",
"Percent of Workers on Salary in 2015",
"Percent of Workers Self-Employed in 2015",
"Population of Citizens in 2015",
"Population of Non-Citizens in 2015",
"Population of Naturalized Citizens in 2015",
"Citizen by Naturalization Percent 2015",
"Percentage of Non-Citizens in 2015",
"Percent of Population with a Bachelor's Degree or Higher in 2015",
"Percent of Population with Less Than High School Degree in 2015",
"2012 to 2015 Difference in Total Population",
"2012 to 2015 Difference in Median Age",
"2012 to 2015 Difference in Health Coverage",
"2012 to 2015 Difference in Health Coverage Percent",
"2012 to 2015 Difference in Male Population",
"2012 to 2015 Difference in Percent of Population Male",
"2012 to 2015 Difference in Female Population",
"2012 to 2015 Difference in Percent of Population Female",
"2012 to 2015 Difference in Percent of Population in Poverty",
"2012 to 2015 Difference in Median Income",
"2012 to 2015 Difference in Gini Coefficient",
"2012 to 2015 Difference in Percent Employment in Manufacturing",
"2012 to 2015 Difference in Percent of Workers on Salary",
"2012 to 2015 Difference in Percent of Workers Self-Employed",
"2012 to 2015 Difference in Population of Citizens",
"2012 to 2015 Difference in Population of Non-Citizens",
"2012 to 2015 Difference in Population of Naturalized Citizens",
"2012 to 2015 Difference in Citizen by Naturalization Percent",
"2012 to 2015 Difference in Percentage of Non-Citizens",
"2012 to 2015 Difference in Percent of Population with a Bachelor's Degree or Higher  ",
"2012 to 2015 Difference in Percent of Population with Less Than High School Degree"]

list2 = ["e.total_2008",
"e.dem_2008",
"e.gop_2008",
"e.oth_2008",
"e.dem_08_perc",
"e.gop_08_perc",
"e.oth_08_perc",
"e.win_marg_08",
"e.winner_08",
"e.total_2012",
"e.dem_2012",
"e.gop_2012",
"e.oth_2012",
"e.dem_12_perc",
"e.gop_12_perc",
"e.oth_12_perc",
"e.win_marg_12",
"e.winner_12",
"e.total_2016",
"e.dem_2016",
"e.gop_2016",
"e.oth_2016",
"e.dem_16_perc",
"e.gop_16_perc",
"e.oth_16_perc",
"e.win_marg_16",
"e.winner_16",
"e.diff_0812",
"e.direction_0812",
"e.diff_1216",
"e.direction_1216",
"e.diff_0816",
"e.direction_0816",
"fd12.population",
"fd12.health_cov",
"fd12.health_cov_per",
"fd12.median_age",
"fd12.median_inc",
"fd12.gini",
"fd12.manu_per",
"fd12.salary_workers",
"fd12.self_employed",
"fd12.pop_citizen",
"fd12.cit_by_nat",
"fd12.cit_by_nat_per",
"fd12.not_cit",
"fd12.not_cit_per",
"fd12.bach_or_higher_per",
"fd12.less_than_hs_per",
"fd12.male_pop",
"fd12.male_per",
"fd12.female_pop",
"fd12.female_per",
"fd12.unemployment",
"fd12.poverty",
"fd15.population",
"fd15.health_cov",
"fd15.health_cov_per",
"fd15.median_age",
"fd15.median_inc",
"fd15.gini",
"fd15.manu_per",
"fd15.salary_workers",
"fd15.self_employed",
"fd15.pop_citizen",
"fd15.cit_by_nat",
"fd15.cit_by_nat_per",
"fd15.not_cit",
"fd15.not_cit_per",
"fd15.bach_or_higher_per",
"fd15.less_than_hs_per",
"fd15.male_pop",
"fd15.male_per",
"fd15.female_pop",
"fd15.female_per",
"fd15.unemployment",
"fd15.poverty",
"d.population",
"d.health_cov",
"d.health_cov_per",
"d.median_age",
"d.median_inc",
"d.gini",
"d.manu_per",
"d.salary_workers",
"d.self_employed",
"d.pop_citizen",
"d.cit_by_nat",
"d.cit_by_nat_per",
"d.not_cit",
"d.not_cit_per",
"d.bach_or_higher_per",
"d.less_than_hs_per",
"d.male_pop",
"d.male_per",
"d.female_pop",
"d.female_per",
"d.unemployment",
"d.poverty",
"u.area_name",
"u.civilian_labor_force_2008",
"u.unemployed_2008",
"u.unemployment_rate_2008",
"u.civilian_labor_force_2012",
"u.unemployed_2012",
"u.unemployment_rate_2012",
"u.civilian_labor_force_2015",
"u.unemployed_2015",
"u.unemployment_rate_2015",
"u.unemployment_rate_difference_2008_to_2015",
"u.unemployment_rate_difference_2012_to_2015",
"u.labor_Force_Percent_Difference_2008_to_2015",
"u.labor_Force_Percent_Difference_2012_to_2015"]
