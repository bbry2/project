#! /usr/bin python3

import sys
import sqlite3
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import statsmodels
import seaborn as sns

def make_plot(field, command):
    conn = sqlite3.connect("data1215-full.db")
    # if year == "2015":
    #     df = pd.read_sql_query("SELECT * FROM fd15 JOIN election_results AS e ON fd15.fips_code = election_results.fips_code" + w_command + ";", conn)
    # elif year == "2012":
    #     df = pd.read_sql_query("SELECT * FROM fd12 JOIN election_results AS e ON fd12.fips_code = election_results.fips_code" + w_command + ";", conn)
    # elif year == "diff":
    #     df = pd.read_sql_query("SELECT * FROM diff_1215 JOIN election_results  AS e ON diff_1215.fips_code = election_results.fips_code" + w_command + ";", conn)
    command1 = command[:6]
    command2 = command[6:]
    if field == "differences":
        command = command1 + " e.diff_0812, e.diff_1216, e.diff_0816, " + command2
    if field == "winning_margins":
        command = command1 + " e.win_marg_08, e.win_marg_12, e.win_marg_16, " + command2
    if field == "democrat_perc":
        command = command1 + " e.dem_08_perc, e.dem_12_perc, e.dem_16_perc, " + command2
    if field == "republican_perc":
        command = command1 + " e.gop_08_perc, e.gop_12_perc, e.gop_16_perc, " + command2
    #print("<b>", command, "</b>")
    df = pd.read_sql_query(command, conn)
    corr = df.corr()
    a = corr.iloc[3:,:3]
    #a = corr.loc["population": "poverty", "diff_0812":"diff_0816"]
    fig = plt.figure()
    fid = sns.heatmap(a, vmax = 1, vmin= -1, cmap='RdBu',annot=True)
    string = mpld3.fig_to_html(fig,template_type="simple")
    print(string)


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 3:
        field = sys.argv[1]
        command = sys.argv[2]
        #w_command = sys.argv[3]
        make_plot(field, command)
    else:
        print("No given correct arguments:", year, w_command)