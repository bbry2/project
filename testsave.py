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

DATABASE_NAME = "data1215.db"
'''
Database filename change: Alter DATABASE_NAME above.
How to update data: If a year is added to the election data, that will need to be added to the command below. If a new field
is desired, a new command will need to be written like the ones below.
'''

def make_plot(field, command):
    conn = sqlite3.connect(DATABASE_NAME)
    command1 = command[:6]
    command2 = command[6:]
    if field == "differences":
        command = command1 + " e.diff_0812, e.diff_1216, e.diff_0816, " + command2
        xticklabels_list = ["2008-2012 Difference", "2012-2016 Difference", "2008-2016 Difference"]
    if field == "winning_margins":
        command = command1 + " e.win_marg_08, e.win_marg_12, e.win_marg_16, " + command2
        xticklabels_list = ["2008 Winning Margin", "2012 Winning Margin", "2016 Winning Margin"]
    if field == "democrat_perc":
        command = command1 + " e.dem_08_perc, e.dem_12_perc, e.dem_16_perc, " + command2
        xticklabels_list = ["2008 Democratic Vote %", "2012 Democratic Vote %", "2016 Democratic Vote %"]
    if field == "republican_perc":
        command = command1 + " e.gop_08_perc, e.gop_12_perc, e.gop_16_perc, " + command2
        xticklabels_list = ["2008 Republican Vote %", "2012 Republican Vote %", "2016 Republican Vote %"]
    df = pd.read_sql_query(command, conn)
    corr = df.corr()
    a = corr.iloc[3:,:3]
    print(list(df)[5:])
    labels_list = list(df)[5:]
    yticklabels_list = []
    for label in labels_list:
        label = label.replace("_", " ").strip()
        label = label.replace("perc", "%")
        label = label.replace("per", "%")
        label = label.title()
        yticklabels_list.append(label)
    fig = plt.figure(figsize=(12,7))
    command2 = command[6:]
    if field == "differences":
        fid = sns.heatmap(a, vmax = 1, vmin= -1, cmap='RdBu',annot=True, xticklabels = xticklabels_list, yticklabels = yticklabels_list)
    if field == "winning_margins":
        fid = sns.heatmap(a, vmax = 1, vmin= -1, cmap='RdBu',annot=True, xticklabels = xticklabels_list, yticklabels = yticklabels_list)
    if field == "democrat_perc":
        fid = sns.heatmap(a, vmax = 1, vmin= -1, cmap='RdBu',annot=True, xticklabels = xticklabels_list, yticklabels = yticklabels_list)
    if field == "republican_perc":
        fid = sns.heatmap(a, vmax = 1, vmin= -1, cmap='RdBu',annot=True, xticklabels = xticklabels_list, yticklabels = yticklabels_list)
    s = os.getcwd()
    print(s)
    string = mpld3.fig_to_html(fig, template_type="general")
    print(string)


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 3:
        field = sys.argv[1]
        command = sys.argv[2]
        make_plot(field, command)
    else:
        print("Not given correct arguments:", year, command)