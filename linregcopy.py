#! /usr/bin python3

import os
import sys
import json
import sqlite3
from math import sqrt
import numpy as np
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
from scipy import stats
import create_png


def regression(predictor, time_frame, w_command):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    command = construct_sql_command(predictor, time_frame, w_command)
    results = c.execute(command).fetchall()
    connection.close()
    differences = []
    predictors = []
    for result in results:
        differences.append(result[0])
        predictors.append(result[1])
    if sys.version[:1] == '2':
        slope, intercept = basic_linear_regression(predictors, differences)
        r_squared, std_err = compute_r_squared(predictors, differences, intercept, slope)
    elif sys.version[:1] == '3':
        slope, intercept, r_value, p_value, std_err = stats.linregress(predictors,differences)
    lower_b1 = slope - 1.96*std_err
    upper_b1 = slope + 1.96*std_err
    p_value = float(p_value)
    print("<br> <b> <u> Regression </u> </b> <br>") 
    print("A positive change in winning margin is a move toward the Democratic candiate, a negative change is toward the Republican canidate <br>")
    print('Our model for the <b>',len(results),'</b> counties you\'ve selected is: <br>')
    print('<b> (Change in winning margin %) = ',round(intercept, 2), '+', round(slope, 2), '(Change in', predictor, 'from', time_frame, ')</b> <br>')
    print('There is a<b>', str(round(100*p_value,2)), '% </b>chance the slope is 0. If the slope is zero, we do not have statistically significant evidence of an association between', predictor, 'and the change in margin. <br>')
    if p_value > .05:
        print("A statistician would say that there <b> is not </b> a statistically significant association here. <br>")
    else:
        print("A statistician would say that there <b> is </b> a statistically significant association here. <br>")
    #print('With 95% confidence, we can say the slope above is inside<b>',round(upper_b1,2), '</b>and<b>', round(lower_b1,2), '</b>. <br>')
    print('We can explain <b>', round(100*r_value**2, 4), '% </b> of the variation in winning margin by variation in', predictor, 'from', time_frame, '<br> <br>')
    #plt.figure()
    #plt.plot(x,y)
    # plt.show
    plt.plot(predictors, np.poly1d(np.polyfit(predictors, differences, 1))(predictors))
    # #plt.show()
    #os.chmod('./', 0o044)
    plt.savefig('example.png')
    #plt.savefig('tem.png')
    # #plt.savefig('/home/student/cs122-win-17-rhopkins18/project/ img.png')
    # plt.close()
    # plt.imshow(img)
    print("<b> <u> Raw Data </u> </b> <br>")    
    # if r_squared > .80:
    #   print("A statistician would normally consider this a <b> strong relationship </b>. <br>")
    # elif r_squared > .40 :
    #   print("A statistician would normally consider this a <b> moderate relationship</b>. <br>")
    # elif r_squared > .40 :
    #   print("A statistician would normally consider this a <b> weak relationship</b>. <br>")
    # else:
    #   print("A statistician would normally <b> not </b> consider this a significant relationship. <br> <br>")

def construct_sql_command(predictor, time_frame, w_command):
    s_command = ""
    if time_frame == "2008 to 2016" and predictor == "unemployment":
        s_command = "SELECT 100*diff_0816, unemployment_rate_difference_2008_to_2015 FROM election_results AS e JOIN unemployment AS u ON e.fips_code=u.fips_code "
    if time_frame == "2012 to 2016" and predictor == "unemployment":
        s_command = "SELECT 100*diff_1216, unemployment_rate_difference_2012_to_2015 FROM election_results AS e JOIN unemployment AS u ON e.fips_code=u.fips_code "
    if time_frame == "2008 to 2016" and predictor == "labor":
        s_command = "SELECT 100*diff_0816, labor_Force_Percent_Difference_2008_to_2015 FROM election_results AS e JOIN unemployment AS u ON e.fips_code=u.fips_code "
    if time_frame == "2012 to 2016" and predictor == "labor":
        s_command = "SELECT 100*diff_1216, labor_Force_Percent_Difference_2012_to_2015 FROM election_results AS e JOIN unemployment AS u ON e.fips_code=u.fips_code "

    return s_command + " " + w_command

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
        predictor = sys.argv[1]
        time_frame = sys.argv[2]
        w_command = sys.argv[3]
        regression(predictor, time_frame, w_command)
    else:
        print("No given correct arguments:", predictor, time_frame, w_command)