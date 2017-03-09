
import sqlite3
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt, mpld3
import sqlite3
import statsmodels

DATABASE_NAME = "data1215.db"
list_of_simple_sums = ["e.total_2008","e.dem_2008","e.gop_2008","e.oth_2008","e.total_2012","e.dem_2012","e.gop_2012","e.oth_2012", "e.total_2016","e.dem_2016","e.gop_2016","e.oth_2016", "u.civilian_labor_force_2008", "u.civilian_labor_force_2012", "u.civilian_labor_force_2015", "u.unemployed_2008", "u.unemployed_2012", "u.unemployed_2015", "fd12.health_cov", "fd15.health_cov"]
list_of_population_perecentages = ["fd12.cit_by_nat_per", "fd15.cit_by_nat_per", "fd12.not_cit_per", "fd15.not_cit_per", "fd12.bach_or_higher_per", "fd15.bach_or_higher_per", "fd12.less_than_hs_per", "fd15.less_than_hs_per", "fd12.male_per", "fd15.male_per","fd12.female_per","fd15.female_per", "fd12.poverty", "fd15.poverty", "fd12.white_per", "fd15.white_per", "fd12.black_per", "fd15.black_per", "fd12.asian_per", "fd15.asian_per", "fd12.hispanic_per", "fd15.hispanic_per", "fd12.health_cov_per", "fd15.health_cov_per", "fd12.median_age", "fd15.median_age", "fd12.median_inc", "fd15.median_inc", "fd12.gini", "fd15.gini"]
list_of_vote_percentages = ["e.dem_08_perc","e.gop_08_perc","e.oth_08_perc","e.dem_12_perc","e.gop_12_perc","e.oth_12_perc", "e.dem_16_perc","e.gop_16_perc","e.oth_16_perc"]
list_of_workforce_percentages = ["fd12.manu_per", "fd15.manu_per", "fd12.salary_workers", "fd15.salary_workers", "fd12.self_employed", "fd15.self_employed"]
list_of_citizen_sums = ["fd12.population", "fd15.population", "fd12.male_pop", "fd15.male_pop", "fd12.female_pop", "fd12.unemployment", "fd15.unemployment", "fd15.female_pop", "fd12.pop_citizen", "fd15.pop_citizen", "fd12.cit_by_nat", "fd15.cit_by_nat", "fd12.not_cit", "fd15.not_cit"]
list_of_citizen_percentages = ["fd12.not_cit_per", "fd15.not_cit_per", "fd12.cit_by_nat_per", "fd15.cit_by_nat_per"]
list_of_differences = ["d.population","d.health_cov","d.health_cov_per","d.median_age","d.median_inc","d.gini","d.manu_per","d.salary_workers","d.self_employed","d.pop_citizen","d.cit_by_nat","d.cit_by_nat_per","d.not_cit","d.not_cit_per","d.bach_or_higher_per","d.less_than_hs_per","d.male_pop","d.male_per","d.female_pop","d.female_per","d.unemployment","d.poverty"]
list_of_unemployment_rates = ["u.unemployment_rate_2008","u.unemployment_rate_2012","u.unemployment_rate_2015"]
'''
Database filename change: Alter DATABASE_NAME file above. 
How to add data fields: add the appropriate select commands to list_of_selects. 
the appropriate commands. Add the data to a list if for multiple on one chart or to the list_of_data if alone. If alone, add indices to waterfall
if statement in one_line_plot function. Similarly with multiple_line_plot, add indicies_of_selects dictionary.
Adding a year: Alter the year and lengths in one_line_plot and multiple_line_plot, adding the appropriate year(s) for labeling and in if statements.
Additional room on charts may be needed. Update commands in generate_table function.
'''

def generate_page(state):
    list_of_selects = ["e.total_2008","e.dem_2008","e.gop_2008","e.oth_2008","e.dem_08_perc","e.gop_08_perc","e.oth_08_perc","e.win_marg_08","e.winner_08","e.total_2012","e.dem_2012","e.gop_2012","e.oth_2012","e.dem_12_perc","e.gop_12_perc","e.oth_12_perc","e.win_marg_12","e.winner_12","e.total_2016","e.dem_2016","e.gop_2016","e.oth_2016","e.dem_16_perc","e.gop_16_perc","e.oth_16_perc","e.win_marg_16","e.winner_16","e.diff_0812","e.direction_0812","e.diff_1216","e.direction_1216","e.diff_0816","e.direction_0816","fd12.population","fd12.health_cov","fd12.health_cov_per","fd12.median_age","fd12.median_inc","fd12.gini","fd12.manu_per","fd12.salary_workers","fd12.self_employed","fd12.pop_citizen","fd12.cit_by_nat","fd12.cit_by_nat_per","fd12.not_cit","fd12.not_cit_per","fd12.bach_or_higher_per","fd12.less_than_hs_per","fd12.male_pop","fd12.male_per","fd12.female_pop","fd12.female_per","fd12.unemployment","fd12.poverty","fd15.population","fd15.health_cov","fd15.health_cov_per","fd15.median_age","fd15.median_inc","fd15.gini","fd15.manu_per","fd15.salary_workers","fd15.self_employed","fd15.pop_citizen","fd15.cit_by_nat","fd15.cit_by_nat_per","fd15.not_cit","fd15.not_cit_per","fd15.bach_or_higher_per","fd15.less_than_hs_per","fd15.male_pop","fd15.male_per","fd15.female_pop","fd15.female_per","fd15.unemployment","fd15.poverty","d.population","d.health_cov","d.health_cov_per","d.median_age","d.median_inc","d.gini","d.manu_per","d.salary_workers","d.self_employed","d.pop_citizen","d.cit_by_nat","d.cit_by_nat_per","d.not_cit","d.not_cit_per","d.bach_or_higher_per","d.less_than_hs_per","d.male_pop","d.male_per","d.female_pop","d.female_per","d.unemployment","d.poverty","u.area_name","u.civilian_labor_force_2008","u.unemployed_2008 ","u.unemployment_rate_2008  ","u.civilian_labor_force_2012","u.unemployed_2012","u.unemployment_rate_2012","u.civilian_labor_force_2015","u.unemployed_2015","u.unemployment_rate_2015","u.unemployment_rate_difference_2008_to_2015","u.unemployment_rate_difference_2012_to_2015","u.labor_Force_Percent_Difference_2008_to_2015","u.labor_Force_Percent_Difference_2012_to_2015", "fd12.white_per", "fd12.hispanic_per", "fd12.black_per", "fd12.asian_per", "fd15.white_per", "fd15.hispanic_per", "fd15.black_per", "fd15.asian_per", "d.white_per", "d.hispanic_per", "d.black_per", "d.asian_per" ]
        
    list_of_fields_extracted = ["Winning Margin", "Winner", "Difference", "Unemployment Rate", "Differences"]

    connection = sqlite3.connect(DATABASE_NAME)
    c = connection.cursor()
    state_param = (state,)
    command = "SELECT COUNT(*) FROM election_results WHERE state=?" #safely put user typed input in SQL
    result = c.execute(command, state_param).fetchall()
    if result[0][0] == 0: #output a warning if the county entered is not found
        print("<h2> The state entered is not found. Make sure to use the two letter state abbreviation")
        print("<br> For example: state=FL")
        return True
    print("Go back to the <a href=\"http://localhost/elections.php\">home page</a>")
    print("<h1> Data for", state , "</h1> <br>")
    print("<h3> Please be patient while the tables and raw data table load. </h3>")
    print("<h5> Below you will find charts which give a visual representation of the data. At the bottom of the page is a table of the raw data for the county. </h5>")

    
    employment_areas = ["Percent of Workers on Salary","Percent of Workers Self-Employed","Percent Employment in Manufacturing"]
    citizen_areas = ["Population of Citizens","Population of Non-Citizens","Population of Naturalized Citizens"]
    votes_by_party_areas = ["Democratic Votes", "Republican Votes", "Third Party Votes"]
    percentage_votes_by_party = ["Percentage Democratic Votes","Percentage Republican Votes","Percentage Third Party Votes"]
    percent_by_race = ["Percent White", "Percent Hispanic", "Percent Black", "Percent Asian"]

    list_of_data = ["Unemployment Rate", "Total Unemployment"]
    list_of_data += ["Civilian Labor Force", "Population", "Median Age", "Health Coverage", "Health Coverage Perc"]
    list_of_data += ["Percent of Population in Poverty","Median Income","Gini Coefficient"]
    list_of_data += ["Percent of Workers on Salary", "Population of Citizens"]
    multiple_line_data_titles = ["Total Votes by Party", "Percentage of Votes by Party", "Percent Employment by Area", "Citizens and Non-Citizens", "Percent by Race/Ethnicity"]
    
    result_dict = generate_results(state)

    multiple_line_data_lists =[votes_by_party_areas, percentage_votes_by_party, employment_areas, citizen_areas, percent_by_race]
    for i in range(0, len(multiple_line_data_titles)):
        multiple_line_plot(multiple_line_data_titles[i], multiple_line_data_lists[i], state, result_dict)

    count = 0
    to_print = ""
    fig = plt.figure(figsize=(10,3))
    for title in list_of_data:
        to_print = one_line_plot(title, state, result_dict, count % 4, fig) + " "
        count += 1
        if count % 4 == 0:
            fig.tight_layout()
            print(to_print)
            fig = plt.figure(figsize=(10,3))

    generate_table(result_dict)


def multiple_line_plot(title, data_field_list, state, result_dict):
    data_dict = {}
    if title == "Total Votes by Party":
        data_dict["Dem"] = [result_dict["e.dem_2008"], result_dict["e.dem_2012"], result_dict["e.dem_2016"]]
        data_dict["GOP"] = [result_dict["e.gop_2008"], result_dict["e.gop_2012"], result_dict["e.gop_2016"]]
        data_dict["3rd"] = [result_dict["e.oth_2008"], result_dict["e.oth_2012"], result_dict["e.oth_2016"]]
    if title == "Percentage of Votes by Party":
        data_dict["Dem"] = [result_dict["e.dem_08_perc"], result_dict["e.dem_12_perc"], result_dict["e.dem_16_perc"]]
        data_dict["GOP"] = [result_dict["e.gop_08_perc"], result_dict["e.gop_12_perc"], result_dict["e.gop_16_perc"]]
        data_dict["3rd"] = [result_dict["e.oth_08_perc"], result_dict["e.oth_12_perc"], result_dict["e.oth_16_perc"]]
    if title == "Percent Employment by Area":
        data_dict["Percent of Workers in Manufacturing"] = [result_dict["fd12.manu_per"], result_dict["fd15.manu_per"]]
        data_dict["Percent of Workers Self-Employed"] = [result_dict["fd12.self_employed"], result_dict["fd15.self_employed"]]
    if title == "Citizens and Non-Citizens":
        data_dict["Population of Non-Citizens"] = [result_dict["fd12.not_cit"], result_dict["fd15.not_cit"]]
        data_dict["Population of Naturalized Citizens"] = [result_dict["fd12.cit_by_nat"], result_dict["fd15.cit_by_nat"]]
    if title == "Percent by Race/Ethnicity":
        data_dict["Percent White"] = [result_dict["fd12.white_per"],result_dict["fd15.white_per"]]
        data_dict["Percent Hispanic"] = [result_dict["fd12.hispanic_per"],result_dict["fd15.hispanic_per"]]
        data_dict["Percent Black"] = [result_dict["fd12.black_per"],result_dict["fd15.black_per"]]
        data_dict["Percent Asian"] = [result_dict["fd12.asian_per"],result_dict["fd15.asian_per"]]

    bar_width = .22
    fig, ax = plt.subplots()
    length = len(data_dict)
    index = np.arange(length)
    loops = 0
    for title2, list_for_bucket in data_dict.items():
        results = list_for_bucket
        y_axis = []
        for r in results:
            if isinstance(r, str):
                r =r.replace(",", "")
                r.replace("", ",")
            y_axis.append(float(r))
        color_choice = 'y'
        if title2 == "GOP":
            color_choice = "r"
        elif title2 == "Dem":
            color_choice = "b"
        elif title2 == "3rd":
            color_choice = "g"
        else:
            if loops == 1:
                color_choice = 'c'
            if loops == 2:
                color_choice = 'r'
            if loops == 3:
                color_choice = 'g'
        if loops == 0:
            rects1 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        if loops == 1:
            rects2 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        if loops == 2:
            rects3 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        if loops == 3:
            rects4 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        loops += 1
    #plt.xlabel('Year')
    plt.ylabel(title, fontsize=13)
    plt.title(title, fontsize = 16)
    if length == 4: #race/ethnicity data
        years = ('2012', '2015')
        plt.xticks(np.arange(len(years)) + bar_width / 2, years)
    if length == 3: #election data 
        years = ('2008', '2012', '2016')
        plt.xticks(np.arange(len(years)) + bar_width / 2, years)
    if length == 2: #demographic data
        years = ('2012', '2015')
        plt.xticks(np.arange(len(years)) + bar_width / 2, years)
    plt.legend(loc='best')
    #plt.xlabel("Year", fontsize=13)
    string = mpld3.fig_to_html(fig, template_type="simple")
    print(string)

    
def one_line_plot(title,  state, result_dict, count, fig):
    data_list = []
    if title == "Unemployment Rate":
        data_list = [result_dict["u.unemployment_rate_2008"],result_dict["u.unemployment_rate_2012"],result_dict["u.unemployment_rate_2015"]]
    if title == "Total Unemployment":
        data_list = [result_dict["u.unemployed_2008"],result_dict["u.unemployed_2012"],result_dict["u.unemployed_2015"]]
    if title == "Civilian Labor Force":
        data_list = [result_dict["u.civilian_labor_force_2008"],result_dict["u.civilian_labor_force_2012"],result_dict["u.civilian_labor_force_2015"]]
    if title == "Population":
        data_list = [result_dict["fd12.population"],result_dict["fd15.population"]]
    if title == "Median Age":
        data_list = [result_dict["fd12.median_age"],result_dict["fd15.median_age"]]
    if title == "Health Coverage":
        data_list = [result_dict["fd12.population"],result_dict["fd15.population"]]
    if title == "Health Coverage Perc":
        data_list = [result_dict["fd12.health_cov_per"],result_dict["fd15.health_cov_per"]]
    if title == "Percent of Population in Poverty":
        data_list = [result_dict["fd12.poverty"],result_dict["fd15.poverty"]]
    if title == "Median Income":
        data_list = [result_dict["fd12.median_inc"],result_dict["fd15.median_inc"]]
    if title == "Gini Coefficient":
        data_list = [result_dict["fd12.gini"],result_dict["fd15.gini"]]
    if title == "Population of Citizens":
        data_list = [result_dict["fd12.pop_citizen"],result_dict["fd15.pop_citizen"]]
    if title == "Percent of Workers on Salary":
        data_list = [result_dict["fd12.salary_workers"],result_dict["fd15.salary_workers"]]

    results = data_list
    x_axis = []
    if len(results) == 2:
        x_axis = ["2012", "2015"]
        labels = ("2012", "2015")
    if len(results) == 3:
        x_axis = ["2008", "2012", "2015"]
        labels = ("2008", "2012", "2015")
    y_axis = []
    for r in results:
        if isinstance(r, str):
            r =r.replace(",", "")
            r.replace("", ",")
        y_axis.append(float(r))
    index = np.arange(len(labels))
    bar_width = .8
    plt.subplot(1,4,count)
    plt.xticks(index + bar_width/2, labels)
    rects = plt.bar(index, y_axis, bar_width)
    plt.ylabel(title, fontsize=13)
    fig.subplots_adjust(wspace = 1, hspace=1)
    string = mpld3.fig_to_html(fig, template_type="simple")

    return string




def generate_results(state):
    connection = sqlite3.connect(DATABASE_NAME)
    list_of_commands = []
    command = "SELECT "
    for select in list_of_simple_sums:
        command += "SUM(" + select + "), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    
    list_of_commands.append(command)
    c = connection.cursor()
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    result_dict = {}
    for dat, label in zip(results, list_of_simple_sums):
        result_dict[label] = dat
    result_dict["e.dem_08_perc"] = 100*result_dict["e.dem_2008"]/result_dict["e.total_2008"]
    result_dict["e.gop_08_perc"] = 100*result_dict["e.gop_2008"]/result_dict["e.total_2008"]
    result_dict["e.oth_08_perc"] = 100*result_dict["e.oth_2008"]/result_dict["e.total_2008"]
    result_dict["e.dem_12_perc"] = 100*result_dict["e.dem_2012"]/result_dict["e.total_2012"]
    result_dict["e.gop_12_perc"] = 100*result_dict["e.gop_2012"]/result_dict["e.total_2012"]
    result_dict["e.oth_12_perc"] = 100*result_dict["e.oth_2012"]/result_dict["e.total_2012"]
    result_dict["e.dem_16_perc"] = 100*result_dict["e.dem_2016"]/result_dict["e.total_2016"]
    result_dict["e.gop_16_perc"] = 100*result_dict["e.gop_2016"]/result_dict["e.total_2016"]
    result_dict["e.oth_16_perc"] = 100*result_dict["e.oth_2016"]/result_dict["e.total_2016"]
    result_dict["e.win_marg_08"] = result_dict["e.dem_08_perc"] - result_dict["e.gop_08_perc"]
    result_dict["e.win_marg_12"] = result_dict["e.dem_12_perc"] - result_dict["e.gop_12_perc"]
    result_dict["e.win_marg_16"] = result_dict["e.dem_16_perc"] - result_dict["e.gop_16_perc"]
    result_dict["e.diff_0812"] = result_dict["e.win_marg_12"] - result_dict["e.win_marg_08"]
    result_dict["e.diff_0816"] = result_dict["e.win_marg_16"] - result_dict["e.win_marg_08"]
    result_dict["e.diff_1216"] = result_dict["e.win_marg_16"] - result_dict["e.win_marg_12"]
    if result_dict["e.diff_0812"] > 0:
        result_dict["e.direction_0812"] = "Dem"
    else:
        result_dict["e.direction_0812"] = "Gop"
    if result_dict["e.diff_0816"] > 0:
        result_dict["e.direction_0816"] = "Dem"
    else:
        result_dict["e.direction_0816"] = "Gop"
    if result_dict["e.diff_1216"] > 0:
        result_dict["e.direction_1216"] = "Dem"
    else:
        result_dict["e.direction_1216"] = "Gop"
    if result_dict["e.dem_2008"] > result_dict["e.gop_2008"]:
        result_dict["e.winner_08"] = "Dem"
    else:
        result_dict["e.winner_08"] = "Gop"
    if result_dict["e.dem_2012"] > result_dict["e.gop_2012"]:
        result_dict["e.winner_12"] = "Dem"
    else:
        result_dict["e.winner_12"] = "Gop"
    if result_dict["e.dem_2016"] > result_dict["e.gop_2016"]:
        result_dict["e.winner_16"] = "Dem"
    else:
        result_dict["e.winner_16"] = "Gop"
    list_of_population_perecentages_2012 = list_of_population_perecentages[::2]
    command = "SELECT "
    for select in list_of_population_perecentages_2012:
        command += "AVG(" + select + "*fd12.population*1.0/fd12.population), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_population_perecentages_2012):
        result_dict[head] = dat
    list_of_population_perecentages_2015 = list_of_population_perecentages[1::2]
    command = "SELECT "
    for select in list_of_population_perecentages_2015:
        command += "AVG(" + select + "*fd15.population*1.0/fd15.population), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_population_perecentages_2015):
        result_dict[head] = dat

    list_of_workforce_percentages_2012 = list_of_workforce_percentages[::2]
    command = "SELECT "
    for select in list_of_workforce_percentages_2012:
        command += "AVG(" + select + "*u.civilian_labor_force_2012*1.0/u.civilian_labor_force_2012), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_workforce_percentages_2012):
        result_dict[head] = dat
    list_of_workforce_percentages_2015 = list_of_workforce_percentages[1::2]
    command = "SELECT "
    for select in list_of_workforce_percentages_2015:
        command += "AVG(" + select + "*u.civilian_labor_force_2015*1.0/u.civilian_labor_force_2015), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_workforce_percentages_2015):
        result_dict[head] = dat
    command = "SELECT "
    for select in list_of_citizen_sums:
        command += "SUM(" + select + "), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    for dat, head in zip(results, list_of_citizen_sums):
        result_dict[head] = dat
    list_of_citizen_percentages_2012 = list_of_citizen_percentages[::2]
    command = "SELECT "
    for select in list_of_citizen_percentages_2012:
        command += "AVG(" + select + "*fd12.population*1.0/fd12.population), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_citizen_percentages_2012):
        result_dict[head] = dat
    list_of_citizen_percentages_2015 = list_of_citizen_percentages[1::2]
    command = "SELECT "
    for select in list_of_citizen_percentages_2012:
        command += "AVG(" + select + "*fd15.population*1.0/fd15.population), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    for dat, head in zip(results, list_of_citizen_percentages_2015):
        result_dict[head] = dat
    command = "SELECT "
    command += "AVG(u.unemployment_rate_2008*u.civilian_labor_force_2008*1.0/u.civilian_labor_force_2008), "
    command += "AVG(u.unemployment_rate_2012*u.civilian_labor_force_2012*1.0/u.civilian_labor_force_2012), "
    command += "AVG(u.unemployment_rate_2015*u.civilian_labor_force_2015*1.0/u.civilian_labor_force_2015), "
    command = command[:-3]
    command += ") FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.state=\"" + state + "\";";
    result = c.execute(command).fetchall()
    results = result[0]
    for dat, head in zip(results, list_of_unemployment_rates):
        result_dict[head] = dat
    result_dict["u.unemployment_rate_difference_2008_to_2015"] = result_dict["u.unemployment_rate_2015"] - result_dict["u.unemployment_rate_2008"]
    result_dict["u.unemployment_rate_difference_2012_to_2015"] = result_dict["u.unemployment_rate_2015"] - result_dict["u.unemployment_rate_2012"]
    result_dict["u.labor_Force_Percent_Difference_2008_to_2015"] = result_dict["u.civilian_labor_force_2015"] - result_dict["u.unemployment_rate_2008"]
    result_dict["u.labor_Force_Percent_Difference_2008_to_2015"] = 100*(result_dict["u.civilian_labor_force_2015"] - result_dict["u.civilian_labor_force_2008"])/result_dict["u.civilian_labor_force_2015"]
    result_dict["u.labor_Force_Percent_Difference_2012_to_2015"] = 100*(result_dict["u.civilian_labor_force_2015"] - result_dict["u.civilian_labor_force_2012"])/result_dict["u.civilian_labor_force_2015"]

    for difference in list_of_differences:
        result_dict["d."+difference[2:]] = result_dict["fd15."+difference[2:]] - result_dict["fd12."+difference[2:]]
    for result in result_dict:
        if isinstance(result_dict[result], float):
            result_dict[result] = round(result_dict[result], 2)

    return result_dict



def generate_table(result_dict):

    list_of_election_data_labels = ["e.total_2008","e.dem_2008","e.gop_2008","e.oth_2008","e.dem_08_perc","e.gop_08_perc","e.oth_08_perc","e.win_marg_08","e.winner_08","e.total_2012","e.dem_2012","e.gop_2012","e.oth_2012","e.dem_12_perc","e.gop_12_perc","e.oth_12_perc","e.win_marg_12","e.winner_12","e.total_2016","e.dem_2016","e.gop_2016","e.oth_2016","e.dem_16_perc","e.gop_16_perc","e.oth_16_perc","e.win_marg_16","e.winner_16","e.diff_0812","e.direction_0812","e.diff_1216","e.direction_1216","e.diff_0816","e.direction_0816"]
    list_of_unemployment_data_labels = ["u.civilian_labor_force_2008","u.unemployed_2008","u.unemployment_rate_2008","u.civilian_labor_force_2012","u.unemployed_2012","u.unemployment_rate_2012","u.civilian_labor_force_2015","u.unemployed_2015","u.unemployment_rate_2015","u.unemployment_rate_difference_2008_to_2015","u.unemployment_rate_difference_2012_to_2015","u.labor_Force_Percent_Difference_2008_to_2015","u.labor_Force_Percent_Difference_2012_to_2015"]
    list_of_2012_demographic_data = ["fd12.population","fd12.health_cov","fd12.health_cov_per","fd12.median_age","fd12.median_inc","fd12.gini","fd12.manu_per","fd12.salary_workers","fd12.self_employed","fd12.pop_citizen","fd12.cit_by_nat","fd12.cit_by_nat_per","fd12.not_cit","fd12.not_cit_per","fd12.bach_or_higher_per","fd12.less_than_hs_per","fd12.male_pop","fd12.male_per","fd12.female_pop","fd12.female_per","fd12.unemployment","fd12.poverty"]
    list_of_2015_demographic_data = ["fd15.population","fd15.health_cov","fd15.health_cov_per","fd15.median_age","fd15.median_inc","fd15.gini","fd15.manu_per","fd15.salary_workers","fd15.self_employed","fd15.pop_citizen","fd15.cit_by_nat","fd15.cit_by_nat_per","fd15.not_cit","fd15.not_cit_per","fd15.bach_or_higher_per","fd15.less_than_hs_per","fd15.male_pop","fd15.male_per","fd15.female_pop","fd15.female_per","fd15.unemployment","fd15.poverty"]
    list_of_differences_in_demographic_data = ["d.population","d.health_cov","d.health_cov_per","d.median_age","d.median_inc","d.gini","d.manu_per","d.salary_workers","d.self_employed","d.pop_citizen","d.cit_by_nat","d.cit_by_nat_per","d.not_cit","d.not_cit_per","d.bach_or_higher_per","d.less_than_hs_per","d.male_pop","d.male_per","d.female_pop","d.female_per","d.unemployment","d.poverty"]
    
    list_of_table_names = ["Election Data", "Unemployment Data", "2012 Demographic Data", "2015 Demographic Data", "2012 to 2015 Demographic Data Differences"]
    list_of_tables = [list_of_election_data_labels, list_of_unemployment_data_labels, list_of_2012_demographic_data, list_of_2015_demographic_data, list_of_differences_in_demographic_data]
    for table, table_name in zip(list_of_tables, list_of_table_names):
        output = "<tr>"
        for header in table:
            output += "<th>" +  header + "</th>"
        output += "</tr>"
        output += "<tr>"
        for data_name in table:
            output += "<td>" + str(result_dict[data_name]) + "</td>"

        print("<table>", output, "<br>")
        print("<h4>", table_name,"</h4>")




def get_header(cursor):
    '''
    Given a cursor object, returns the appropriate header (column names)
    '''
    desc = cursor.description
    header = ()
    for i in desc:
        header = header + (clean_header(i[0]),)
    return list(header)

def clean_header(s):
    '''
    Removes table name from header
    '''
    for i in range(len(s)):
        if s[i] == ".":
            s = s[i+1:]
            break
    return s 

if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 2:
        state = sys.argv[1]
        generate_page(state)
    else:
        print("<h3> Incorrect format entered </h3>")