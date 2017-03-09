.separator ,
.mode column
.headers on

CREATE TABLE unemployment
  (fips_code integer, 
   state VARCHAR(2), 
   area_name VARCHAR(50), 
   civilian_labor_force_2008 integer, 
   unemployed_2008 integer, 
   unemployment_rate_2008 real,  
   civilian_labor_force_2012 integer, 
   unemployed_2012 integer,
   unemployment_rate_2012 real, 
   civilian_labor_force_2015 integer, 
   unemployed_2015 integer,
   unemployment_rate_2015 real, 
   unemployment_rate_difference_2008_to_2015 real, 
   unemployment_rate_difference_2012_to_2015 real, 
   labor_Force_Percent_Difference_2008_to_2015 real,  
   labor_Force_Percent_Difference_2012_to_2015 real); 
  
.import Unemployment_Processed2.csv unemployment