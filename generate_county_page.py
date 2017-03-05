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



def generate_page(county_state):
    list_of_selects = ["e.total_2008","e.dem_2008","e.gop_2008","e.oth_2008","e.dem_08_perc","e.gop_08_perc","e.oth_08_perc","e.win_marg_08","e.winner_08","e.total_2012","e.dem_2012","e.gop_2012","e.oth_2012","e.dem_12_perc","e.gop_12_perc","e.oth_12_perc","e.win_marg_12","e.winner_12","e.total_2016","e.dem_2016","e.gop_2016","e.oth_2016","e.dem_16_perc","e.gop_16_perc","e.oth_16_perc","e.win_marg_16","e.winner_16","e.diff_0812","e.direction_0812","e.diff_1216","e.direction_1216","e.diff_0816","e.direction_0816","fd12.population","fd12.health_cov","fd12.health_cov_per","fd12.median_age","fd12.median_inc","fd12.gini","fd12.manu_per","fd12.salary_workers","fd12.self_employed","fd12.pop_citizen","fd12.cit_by_nat","fd12.cit_by_nat_per","fd12.not_cit","fd12.not_cit_per","fd12.bach_or_higher_per","fd12.less_than_hs_per","fd12.male_pop","fd12.male_per","fd12.female_pop","fd12.female_per","fd12.unemployment","fd12.poverty","fd15.population","fd15.health_cov","fd15.health_cov_per","fd15.median_age","fd15.median_inc","fd15.gini","fd15.manu_per","fd15.salary_workers","fd15.self_employed","fd15.pop_citizen","fd15.cit_by_nat","fd15.cit_by_nat_per","fd15.not_cit","fd15.not_cit_per","fd15.bach_or_higher_per","fd15.less_than_hs_per","fd15.male_pop","fd15.male_per","fd15.female_pop","fd15.female_per","fd15.unemployment","fd15.poverty","d.population","d.health_cov","d.health_cov_per","d.median_age","d.median_inc","d.gini","d.manu_per","d.salary_workers","d.self_employed","d.pop_citizen","d.cit_by_nat","d.cit_by_nat_per","d.not_cit","d.not_cit_per","d.bach_or_higher_per","d.less_than_hs_per","d.male_pop","d.male_per","d.female_pop","d.female_per","d.unemployment","d.poverty","u.area_name","u.civilian_labor_force_2008","u.unemployed_2008 ","u.unemployment_rate_2008  ","u.civilian_labor_force_2012","u.unemployed_2012","u.unemployment_rate_2012","u.civilian_labor_force_2015","u.unemployed_2015","u.unemployment_rate_2015","u.unemployment_rate_difference_2008_to_2015","u.unemployment_rate_difference_2012_to_2015","u.labor_Force_Percent_Difference_2008_to_2015","u.labor_Force_Percent_Difference_2012_to_2015"]
    list_of_tables = ["election_results", "fd12", "fd15", "diff_1215"]
    state = "\"" + county_state[-2:] + "\""
    state = county_state[-2:]
    county = county_state[:-2].strip()
    print("<h1> Data for", county + ",", state , "</h1> <br>")
    
    
    employment_areas = ["Percent of Workers on Salary","Percent of Workers Self-Employed","Percent Employment in Manufacturing"]
    citizen_areas = ["Population of Citizens","Population of Non-Citizens","Population of Naturalized Citizens"]
    votes_by_party_areas = ["Democratic Votes", "Republican Votes", "Third Party Votes"]
    percentage_votes_by_party = ["Percentage Democratic Votes","Percentage Republican Votes","Percentage Third Party Votes"]
    list_of_data = ["Unemployment Rate", "Total Unemployment"]
    list_of_data += ["Civilian Labor Force", "Population", "Median Age", "Health Coverage", "Health Coverage Perc"]
    list_of_data += ["Percent of Population in Poverty","Median Income","Gini Coefficient"]
    multiple_line_data_titles = ["Total Votes by Party", "Percentage of Votes by Party", "Percent Employment in Areas", "Citizens and Non-Citizens"]
    multiple_line_data_lists =[votes_by_party_areas, percentage_votes_by_party, employment_areas, citizen_areas]
    for title in list_of_data:
        one_line_plot(title, county, state, list_of_selects)
    for i in range(0, len(multiple_line_data_titles)):
        multiple_line_plot(multiple_line_data_titles[i], multiple_line_data_lists[i], county, state, list_of_selects)

    generate_table(state, county)

def multiple_line_plot(title, data_field_list, county, state, list_of_selects):
    indicies_of_selects = {}}
    if title = "Total Votes by Party":
        indicies_of_selects["Dem"] = [1, 10, 19]
        indicies_of_selects["GOP"] = [2, 11, 20]
        indicies_of_selects["3rd"] = [3, 12, 21]
    if title = "Percentage of Votes by Party":
        indicies_of_selects["Dem"] = [4, 13, 22]
        indicies_of_selects["GOP"] = [5, 14, 23]
        indicies_of_selects["3rd"] = [6, 15, 24]    
    if title = "Percent Employment in Areas":
        indicies_of_selects["Percent of Workers in Manufacturing"] = [39, 61]
        indicies_of_selects["Percent of Workers Self-Employed"] = [41, 63]
        indicies_of_selects["Percent of Workers on Salary"] = [40, 62] 
    if title = "Citizens and Non-Citizens":
        indicies_of_selects["Population of Citizens"] = [42, 64]
        indicies_of_selects["Population of Non-Citizens"] = [45, 67]
        indicies_of_selects["Population of Naturalized Citizens"] = [43, 65]

    connection = sqlite3.connect("data1215-full.db")
    c = connection.cursor()
    fig = plt.figure()
    plt.xlabel("Year", fontsize=18)
    selects = " "
    list_of_results = []
    for title, list_of_indices in indicies_of_selects.items():
        for index in list_of_indices:
            selects += list_of_selects[index] + " , "
        selects = selects[:-2]
        command = "SELECT " + selects + " FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.county =\"" + county + "\" AND e.state=\"" + state + "\";";
        
        result = c.execute(command).fetchall()
        results = result[0]
        for i in range(0, len(results)):
            if isinstance(results[i], str):
                results[i] = results[i].replace(",", "")
        list_of_data.append(results)

    x_axis = []
    if len(results) == 2:
        x_axis = [2012, 2015]
    if len(results) == 3:
        x_axis = [2008, 2012, 2015]
    y_axis = []
    y_axis.append(float(r))

    
    plt.ylabel(title, fontsize=18)
    plt.axhline(0, color="gray", linestyle="")
    fid = plt.plot(x_axis, y_axis)
    string = mpld3.fig_to_html(fig, template_type="general")
    print("<h3>", title, "</h3>",string)
    
def one_line_plot(title, county, state, list_of_selects):
    indicies_of_selects = []
    if title == "Unemployment Rate":
        indicies_of_selects = [102,105,108]
    if title == "Total Unemployment":
        indicies_of_selects = [101,104,107]
    if title == "Civilian Labor Force":
        indicies_of_selects = [100,103,106]
    if title == "Population":
        indicies_of_selects = [33,55]
    if title == "Median Age":
        indicies_of_selects = [36,58]
    if title == "Health Coverage":
        indicies_of_selects = [34,56]
    if title == "Health Coverage Perc":
        indicies_of_selects = [35,57]
    if title == "Percent of Population in Poverty":
        indicies_of_selects = [54,76]
    if title == "Median Income":
        indicies_of_selects = [37,59]
    if title == "Gini Coefficient":
        indicies_of_selects = [38,60]
    selects = " "
    for index in indicies_of_selects:
        selects += list_of_selects[index] + " , "
    selects = selects[:-2]
    command = "SELECT " +selects+ " FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.county =\"" + county + "\" AND e.state=\"" + state + "\";";
    connection = sqlite3.connect("data1215-full.db")
    c = connection.cursor()
    result = c.execute(command).fetchall()
    results = result[0]
    x_axis = []
    if len(results) == 2:
        x_axis = [2012, 2015]
    if len(results) == 3:
        x_axis = [2008, 2012, 2015]
    y_axis = []
    for r in results:
        if isinstance(r, str):
            r =r.replace(",", "")
            r.replace("", ",")
        y_axis.append(float(r))

    fig = plt.figure()
    plt.xlabel("Year", fontsize=18)
    plt.ylabel(title, fontsize=18)
    plt.axhline(0, color="gray", linestyle="")

    fid = plt.plot(x_axis, y_axis)

    string = mpld3.fig_to_html(fig, template_type="general")
    print("<h3>", title, "</h3>",string)



def generate_table(state, county):
    command = "SELECT e.*, fd12.*, fd15.*, d.*, u.* FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.county =\"" + county + "\" AND e.state=\"" + state + "\";";
    connection = sqlite3.connect("data1215-full.db")
    c = connection.cursor()
    result = c.execute(command).fetchall()
    results = result[0]
    header = get_header(c)
    length = len(header)
    num_tables = length // 9
    start = 3
    repeated_data_indices = [36, 37, 60, 61, 84, 85, 108, 109, 110] 
    for j in range(0,num_tables):
        l = 9*j + start
        output = "<tr>"
        for i in range(l, l+9):
            if i not in repeated_data_indices:
                output += "<th>" +  header[i] + "</th>"
        output += "</tr>"
        output += "<tr>"
        for i in range(l, l+9):
            if i not in repeated_data_indices:
                output += "<td>" + str(results[i]) + "</td>"
        print("<table>", output, "<br>")

    


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
        county_state = sys.argv[1]
        generate_page(county_state)
    else:
        print("<h3> Incorrect format entered </h3>")