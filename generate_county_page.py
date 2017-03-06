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
    county = county_state[:-2].replace("_", " ").strip()
    if county[-1] == ",":
        county = county[:-1]
    print("<h1> Data for", county + ",", state , "</h1> <br>")
    print("<h3> Please be patient while the tables and raw data table load. </h3> <br>")
    print("<h5> Below you will find charts which give a visual representation of the data. At the bottom of the page is a table of the raw data for the county. </h5> <br>")
    
    
    employment_areas = ["Percent of Workers on Salary","Percent of Workers Self-Employed","Percent Employment in Manufacturing"]
    citizen_areas = ["Population of Citizens","Population of Non-Citizens","Population of Naturalized Citizens"]
    votes_by_party_areas = ["Democratic Votes", "Republican Votes", "Third Party Votes"]
    percentage_votes_by_party = ["Percentage Democratic Votes","Percentage Republican Votes","Percentage Third Party Votes"]
    list_of_data = ["Unemployment Rate", "Total Unemployment"]
    list_of_data += ["Civilian Labor Force", "Population", "Median Age", "Health Coverage", "Health Coverage Perc"]
    list_of_data += ["Percent of Population in Poverty","Median Income","Gini Coefficient"]
    list_of_data += ["Percent of Workers on Salary", "Population of Citizens"]
    multiple_line_data_titles = ["Total Votes by Party", "Percentage of Votes by Party", "Percent Employment by Area", "Citizens and Non-Citizens"]
    multiple_line_data_lists =[votes_by_party_areas, percentage_votes_by_party, employment_areas, citizen_areas]
    for i in range(0, len(multiple_line_data_titles)):
        multiple_line_plot(multiple_line_data_titles[i], multiple_line_data_lists[i], county, state, list_of_selects)

    count = 0
    to_print = ""
    fig = plt.figure(figsize=(10,3))
    for title in list_of_data:
        to_print = one_line_plot(title, county, state, list_of_selects, count % 4, fig) + " "
        count += 1
        if count % 4 == 0:
            fig.tight_layout()
            print(to_print)
            fig = plt.figure(figsize=(10,3))

    generate_table(state, county)

def multiple_line_plot(title, data_field_list, county, state, list_of_selects):
    indicies_of_selects = {}
    if title == "Total Votes by Party":
        indicies_of_selects["Dem"] = [1, 10, 19]
        indicies_of_selects["GOP"] = [2, 11, 20]
        indicies_of_selects["3rd"] = [3, 12, 21]
    if title == "Percentage of Votes by Party":
        indicies_of_selects["Dem"] = [4, 13, 22]
        indicies_of_selects["GOP"] = [5, 14, 23]
        indicies_of_selects["3rd"] = [6, 15, 24]    
    if title == "Percent Employment by Area":
        indicies_of_selects["Percent of Workers in Manufacturing"] = [39, 61]
        indicies_of_selects["Percent of Workers Self-Employed"] = [41, 63]
    if title == "Citizens and Non-Citizens":
        indicies_of_selects["Population of Non-Citizens"] = [45, 67]
        indicies_of_selects["Population of Naturalized Citizens"] = [43, 65]

    bar_width = .22
    connection = sqlite3.connect("data1215-full.db")
    c = connection.cursor()
    fig, ax = plt.subplots()
    length = len(indicies_of_selects)
    index = np.arange(length)
    loops = 0
    for title2, list_of_indicies in indicies_of_selects.items():
        selects = " "
        for index in list_of_indicies:
            selects += list_of_selects[index] + ", "
        selects = selects[:-2]
        command = "SELECT " +selects+ " FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code WHERE e.county =\"" + county + "\" AND e.state=\"" + state + "\";";
        result = c.execute(command).fetchall()
        results = result[0]
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
                color_choice = 'm'
        if loops == 0:
            rects1 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        if loops == 1:
            rects2 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        if loops == 2:
            rects3 = plt.bar(np.arange(len(y_axis)) + loops*bar_width, y_axis, bar_width, color=color_choice, label=title2)
        loops += 1
    plt.xlabel('Year')
    plt.ylabel(title, fontsize=13)
    plt.title(title, fontsize = 16)
    if length == 3:
        years = ('2008', '2012', '2016')
        plt.xticks(np.arange(len(indicies_of_selects)) + bar_width / 2, years)
    if length == 2:
        years = ('2012', '2015')
        plt.xticks(np.arange(len(indicies_of_selects)) + bar_width / 2, years)
    plt.legend()
    plt.xlabel("Year", fontsize=13)
    string = mpld3.fig_to_html(fig, template_type="simple")
    print(string)

    
def one_line_plot(title, county, state, list_of_selects, count, fig):
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
    if title == "Population of Citizens":
        indicies_of_selects = [42, 64]
    if title == "Percent of Workers on Salary":
        indicies_of_selects = [40, 62]
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