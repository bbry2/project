#!/usr/bin python3
#Ryan Hopkins

import sys
import sqlite3
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
from scipy import stats
import seaborn as sns
import statsmodels
 
DATABASE_NAME = "data1215.db"

'''
Database filename change: Alter DATABASE_NAME above.
How to update data: If a table is added, the command in construct_sql_command will need to be altered to include that table.
'''


def regression(predictor, outcome, w_command):
    connection = sqlite3.connect(DATABASE_NAME)
    c = connection.cursor()
    command = construct_sql_command(predictor, outcome, w_command)
    results = c.execute(command).fetchall()
    df_results = pd.read_sql_query(command, connection)
    headers = get_header(c)
    connection.close()
    outcomes = []
    predictors = []
    for result in results:
        predictors.append(result[0])
        outcomes.append(result[1])
    slope, intercept, r_value, p_value, std_err = stats.linregress(predictors, outcomes)
    lower_b1 = slope - 1.96*std_err
    upper_b1 = slope + 1.96*std_err
    p_value = float(p_value)
    outcome_label = headers[1]
    outcome_label = outcome_label.title()
    predictor_label = headers[0]
    predictor_label = predictor_label.title()

    print("<br> <b> <u> Regression </u> </b> <br>")	
    print('Our model for the <b>',len(results),'</b> counties you\'ve selected is: <br>')
    print('<b> (' + outcome_label + ') = ',round(intercept, 2), '+', round(slope, 4), '(' + predictor_label + ')</b> <br>')
    print('There is a<b>', str(round(100*p_value, 6)), '% </b>chance the slope is 0. If the slope is zero, we do not have statistically significant evidence of an association between', predictor_label, 'and', outcome_label, '<br>')
    print('Go to our <a href="http://localhost/information.php">information page</a> to see more about the variables. <br>')
    if p_value > .05:
        print("A statistician would say that there<b><i> is not </i> a statistically significant </b> association here. <br>")
    else:
        print("A statistician would say that there <b><i> is </i>a statistically significant association </b>here. <br>")
    print('We can explain <b>', round(100*r_value**2, 4), '% </b> of the variation in', outcome_label, 'by variation in', predictor_label, '<br> <br>')

    fig = plt.figure()
    plt.suptitle(predictor_label+ " and " + outcome_label, fontsize=16)
    plt.xlabel(predictor_label, fontsize=13)
    plt.ylabel(outcome_label, fontsize=15)
    
    fid = plt.scatter(predictors, outcomes, s=30, alpha=0.15, marker='o')
    par = np.polyfit(predictors, outcomes, 1, full=True)
    slope = par[0][0]
    intercept = par[0][1]
    yd = outcomes 
    xd = predictors
    reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
    xl = [min(xd), max(xd)]
    yl = [slope*xx + intercept  for xx in xl]
    if 'diff' not in predictor and 'difference' not in predictor and 'Difference' not in predictor \
    and 'd.' not in predictor and 'marg' not in predictor:
        plt.xlim(xmin=0)
    if 'diff' not in outcome and 'difference' not in outcome and 'Difference' not in outcome \
    and 'd.' not in outcome and 'marg' not in outcome and 'Diff' not in outcome:
        plt.ylim(ymin=0)

    plt.plot(xl, yl, '-r')
    plt.savefig("regression.png")
    print("<center> <img src=\"regression.png\" alt=\"Regression\" height=\"500\" width=\"550\"></center>")
	


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

def construct_sql_command(predictor, outcome, w_command):
    f_command = " FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code ";
    if predictor[0] == 'e' and predictor[-4:] == 'perc':
        predictor = "100*"+predictor
    if outcome[0] == 'e' and outcome[-4:] == 'perc':
        outcome = "100*"+outcome
    s_command = "SELECT " + predictor + ", " + outcome
    return s_command + " " + f_command + " " + w_command + ";"


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 4:
    	outcome = sys.argv[1]
    	predictor = sys.argv[2]
    	w_command = sys.argv[3]
    	regression(predictor, outcome, w_command)
    else:
    	print("No given correct arguments:", predictor, outcome, w_command)