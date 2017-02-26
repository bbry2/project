.separator ,
.mode column
.headers on

CREATE TABLE election_results
  (fips_code integer,
   state VARCHAR(2),
   county VARCHAR(100),
   total_2008 integer,
   dem_2008 integer,
   gop_2008 integer,
   oth_2008 integer,
   dem_08_perc real,
   gop_08_perc real,
   oth_08_perc real,
   win_marg_08 real,
   winner_08 VARCHAR(3),
   total_2012 integer,
   dem_2012 integer,
   gop_2012 integer,
   oth_2012 integer,
   dem_12_perc real,
   gop_12_perc real,
   oth_12_perc real,
   win_marg_12 real,
   winner_12 VARCHAR(3),
   total_2016 integer,
   dem_2016 integer,
   gop_2016 integer,
   oth_2016 integer,
   dem_16_perc real,
   gop_16_perc real,
   oth_16_perc real,
   win_marg_16 real,
   winner_16 VARCHAR(3),
   diff_0812 real,
   direction_0812 VARCHAR(6),
   diff_1216 real,
   direction_1216 VARCHAR(6),
   diff_0816 real,
   direction_0816 VARCHAR(6));

CREATE TABLE fd12
  (fips_code integer,
   county VARCHAR(150),
   population integer,
   health_cov integer,
   health_cov_per real,
   median_age integer,
   median_inc real,
   gini real,
   manu_per real,
   salary_workers real,
   self_employed real,
   pop_citizen integer,
   cit_by_nat integer,
   cit_by_nat_per real,
   not_cit integer,
   not_cit_per real,
   bach_or_higher_per real,
   less_than_hs_per real,
   male_pop integer,
   male_per real,
   female_pop integer,
   female_per real,
   unemployment real,
   poverty real);

CREATE TABLE fd15
  (fips_code integer,
   county VARCHAR(150),
   population integer,
   health_cov integer,
   health_cov_per real,
   median_age integer,
   median_inc real,
   gini real,
   manu_per real,
   salary_workers real,
   self_employed real,
   pop_citizen integer,
   cit_by_nat integer,
   cit_by_nat_per real,
   not_cit integer,
   not_cit_per real,
   bach_or_higher_per real,
   less_than_hs_per real,
   male_pop integer,
   male_per real,
   female_pop integer,
   female_per real,
   unemployment real,
   poverty real);

CREATE TABLE diff_1215
  (fips_code integer,
   county VARCHAR(150),
   population integer,
   health_cov integer,
   health_cov_per real,
   median_age integer,
   median_inc real,
   gini real,
   manu_per real,
   salary_workers real,
   self_employed real,
   pop_citizen integer,
   cit_by_nat integer,
   cit_by_nat_per real,
   not_cit integer,
   not_cit_per real,
   bach_or_higher_per real,
   less_than_hs_per real,
   male_pop integer,
   male_per real,
   female_pop integer,
   female_per real,
   unemployment real,
   poverty real);

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

.import e.csv election_results
.import fd12.csv fd12
.import fd15.csv fd15
.import diff_1215.csv diff_1215
.import Unemployment_Processed.csv unemployment