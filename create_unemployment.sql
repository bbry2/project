CREATE TABLE unemployment(FIPS_code integer, state VARCHAR(2), area_name VARCHAR(50), civilian_labor_force_2008 integer, unemployed_2008 integer, unemployment_rate_2008 float,  civilian_labor_force_2012 integer, unemployed_2012 integer,
 unemployment_rate_2012 float, civilian_labor_force_2015 integer, unemployed_2015 integer,
 unemployment_rate_2015 float, unemployment_rate_difference_2008_to_2015 float, unemployment_rate_difference_2012_to_2015 float, labor_Force_Percent_Difference_2008_to_2015, labor_Force_Percent_Difference_2012_to_2015); 
.separator ,
.import Unemployment_Processed.csv unemployment