import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import statsmodels

def make_plot(year, w_command):
    conn = sqlite3.connect("data1215-full.db")
    if year == "2015":
        df = pd.read_sql_query("SELECT * FROM fd15 JOIN election_results ON fd15.fips_code = election_results.fips_code" + w_command + ";", conn)
    elif year == "2012":
        df = pd.read_sql_query("SELECT * FROM fd12 JOIN election_results ON fd12.fips_code = election_results.fips_code" + w_command + ";", conn)
    corr = df.corr()
    a = corr.loc["population": "poverty", "diff_0812":"diff_0816"]
    fig = plt.figure()
    fid = sns.heatmap(a, vmax = 1, vmin= -1, annot=True)
    string = mpld3.fig_to_html(fig,template_type="simple")
    print(string)


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 4:
        year = sys.argv[1]
        w_command = sys.argv[2]
        #w_command = sys.argv[3]
        make_plot(year, w_command)
    else:
        print("No given correct arguments:", year, w_command)