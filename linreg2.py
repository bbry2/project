#! /usr/bin python3

import os
import sys
import json
import sqlite3
import pandas as pd
from math import sqrt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
from scipy import stats
import seaborn as sns
import statsmodels
 


def regression(predictor, outcome, w_command):
    connection = sqlite3.connect("data1215-full.db")
    c = connection.cursor()
    command = construct_sql_command(predictor, outcome, w_command)
    #print(command)
    results = c.execute(command).fetchall()
    df_results = pd.read_sql_query(command, connection)
    headers = get_header(c)
    connection.close()
    outcomes = []
    predictors = []
    for result in results:
        predictors.append(result[0])
        outcomes.append(result[1])
    if sys.version[:1] == '2':
        slope, intercept = basic_linear_regression(predictors, outcomes)
        r_squared, std_err = compute_r_squared(predictors, outcomes, intercept, slope)
    elif sys.version[:1] == '3':
        slope, intercept, r_value, p_value, std_err = stats.linregress(predictors, outcomes)
    lower_b1 = slope - 1.96*std_err
    upper_b1 = slope + 1.96*std_err
    p_value = float(p_value)
    #outcome_label = outcome[2:]
    outcome_label = headers[1]
    #outcome_label = outcome_label.replace("_", " ")
    outcome_label = outcome_label.title()
    #predictor_label = predictor[2:]
    #predictor_label = predictor_label.replace("_", " ")
    predictor_label = headers[0]
    predictor_label = predictor_label.title()
    print("<br> <b> <u> Regression </u> </b> <br>")	
    #print("A positive change in winning margin is a move toward the Democratic candiate, a negative change is toward the Republican canidate <br>")
    print('Our model for the <b>',len(results),'</b> counties you\'ve selected is: <br>')
    print('<b> (' + outcome_label + ') = ',round(intercept, 2), '+', round(slope, 2), '(' + predictor_label + ')</b> <br>')
    print('There is a<b>', str(round(100*p_value, 6)), '% </b>chance the slope is 0. If the slope is zero, we do not have statistically significant evidence of an association between', predictor_label, 'and', outcome_label, '<br>')
    if p_value > .05:
        print("A statistician would say that there <b> is not </b> a statistically significant association here. <br>")
    else:
        print("A statistician would say that there <b> is </b> a statistically significant association here. <br>")
    #print('With 95% confidence, we can say the slope above is inside<b>',round(upper_b1,2), '</b>and<b>', round(lower_b1,2), '</b>. <br>')
    print('We can explain <b>', round(100*r_value**2, 4), '% </b> of the variation in', outcome_label, 'by variation in', predictor_label, '<br> <br>')
    #plt.figure()
    #plt.plot(x,y)
    # plt.show
    fig = plt.figure()
    #fid = plt.plot([3,1,4,1,5])
    #fid = plt.plot(predictors, np.poly1d(np.polyfit(predictors, differences, 1))(predictors))
    plt.suptitle('test title', fontsize=20)
    plt.xlabel(predictor_label, fontsize=18)
    plt.ylabel(outcome_label, fontsize=16)
    
    #plt.axhline(0, color="gray", linestyle="--")
    #plt.axvline(0, color="gray", linestyle="--")

    fid = plt.scatter(predictors, outcomes, s=30, alpha=0.15, marker='o')
    par = np.polyfit(predictors, outcomes, 1, full=True)
    slope = par[0][0]
    intercept = par[0][1]
    yd = outcomes 
    xd = predictors
    reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
    xl = [min(xd), max(xd)]
    yl = [slope*xx + intercept  for xx in xl]

    # coefficient of determination, plot text  
    #variance = np.var(yd)
    #residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)])
    #Rsqr = np.round(1-residuals/variance, decimals=6)
    #print(Rsqr)
    #plt.text(.1*max(xd)+.1*min(xd),.4*max(yd)+.1*min(yd),"R^2 = " + str(100*Rsqr) + "%", fontsize=15)

    # error bounds
    #yerr = [abs(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)]
    #par = np.polyfit(xd, yerr, 2, full=True)

    #yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]
    #yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]

    plt.plot(xl, yl, '-r')
    #plt.plot(xd, yerrLower, '--r')
    #plt.plot(xd, yerrUpper, '--r')
    string = mpld3.fig_to_html(fig,template_type="simple")
    print(string)
    # fig = plt.figure()
    # fid = sns.regplot(x=predictor[2:], y=outcome[2:], data=df_results)
    # string = mpld3.fig_to_html(fig,template_type="simple")
    # print(string)
    # #plt.show()
    #os.chmod('./', 0o044)
    #plt.show()
    #plt.savefig('temp.png')
    # #plt.savefig('/home/student/cs122-win-17-rhopkins18/project/ img.png')
    # plt.close()
    # plt.imshow(img)
    print("<b> <u> Raw Data </u> </b> <br>")	
	# if r_squared > .80:
	# 	print("A statistician would normally consider this a <b> strong relationship </b>. <br>")
	# elif r_squared > .40 :
	# 	print("A statistician would normally consider this a <b> moderate relationship</b>. <br>")
	# elif r_squared > .40 :
	# 	print("A statistician would normally consider this a <b> weak relationship</b>. <br>")
	# else:
	# 	print("A statistician would normally <b> not </b> consider this a significant relationship. <br> <br>")


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

def basic_linear_regression(x, y):
    length = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(map(lambda a: a * a, x))
    sum_of_products = sum([x[i] * y[i] for i in range(length)])
    a = (sum_of_products - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
    b = (sum_y - a * sum_x) / length
    return a, b

def compute_r_squared(predictors, differences, b0, b1):
	residuals = []
	for predictor, difference in zip(predictors, differences):
		res = difference - (b0 + b1*predictor)
		residuals.append(res)
	avg_obs = sum(differences)/len(differences)
	ss_total = 0
	for difference in differences:
		ss_total += (difference - avg_obs)**2
	ss_resid = 0.0
	for residual in residuals:
		ss_resid += residual**2
	s_squared = ss_resid/(len(differences)-2)
	standard_error = 0.0
	avg_predictor = sum(predictors)/len(predictors)
	sum_diff = 0.0
	for predictor in predictors:
		sum_diff += (predictor - avg_predictor)**2
	standard_error = sqrt(s_squared / sum_diff)

	return 1 - ss_resid/ss_total, standard_error

if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 4:
    	outcome = sys.argv[1]
    	predictor = sys.argv[2]
    	w_command = sys.argv[3]
    	regression(predictor, outcome, w_command)
    else:
    	print("No given correct arguments:", predictor, outcome, w_command)