# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shapefile as sf
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection







def get_polygon_lists(df,df_diff,states):
    filename = open("elpo12p010g.shp")
    filename2 = open("elpo12p010g.dbf")
    shape_file = sf.Reader(shp = filename, dbf = filename2)
    poly_list_dict = {'poly_list': {'rd':[], 'bu':[]}, 'vote_diff': {'rd':[], 'bu':[]},
    'win_marg': {'rd':[], 'bu':[]}, 'unemp1216': {'rd':[], 'bu':[]}, 'manuper': {'rd':[], 'bu':[]},
    'median_income': {'rd':[], 'bu':[]}, 'median_age': {'rd':[], 'bu':[]}, 'not_cit': {'rd':[], 'bu':[]}}
    color_array_dict = {'poly_list':{'rd':[10], 'bu':[10]}, 'unemp1216': {'rd':[], 'bu':[]},
    'vote_diff': {'rd':[], 'bu':[]},'win_marg': {'rd':[], 'bu':[]}, 'manuper': {'rd':[], 'bu':[]},
    'median_income': {'rd':[], 'bu':[]}, 'median_age': {'rd':[], 'bu':[]}, 'not_cit': {'rd':[], 'bu':[]}}
    shapes = shape_file.shapes()
    records = shape_file.records()
    #Remove Bedford City, VA, since no longer a county
    shapes.pop(2689)
    records.pop(2689)
    if states == []:
        for i in range(len(shapes)):
            if records[i][0] != 'AK' and records[i][0] != 'HI':
                points = shapes[i].points
                poly = Polygon(points)
                df1 = df[df['fips_code'] == int(records[i][3])]
                df1_2 = df_diff[df_diff['fips_code'] == int(records[i][3])]
                df2 = df1['winner'] == 'Gop' 
                df3 = df1['vote_diff1216'] < 0
                df4 = df1['win_marg'] < 0
                df5 = df1_2['unemp1216'] > 0
                df6 = df1_2['manuper'] > 0
                df7 = df1_2['median_age']>0
                df8 = df1_2['median_income']>0
                df9 = df1_2['not_cit']>0
                if df2.bool():
                    poly_list_dict['poly_list']['rd'].append(poly)
                else:
                    poly_list_dict['poly_list']['bu'].append(poly)
                if df3.bool():
                    color_array_dict['vote_diff']['rd'].append(float(df1.get('vote_diff1216')))
                    poly_list_dict['vote_diff']['rd'].append(poly)
                else:
                    color_array_dict['vote_diff']['bu'].append(float(df1.get('vote_diff1216')))
                    poly_list_dict['vote_diff']['bu'].append(poly)
                if df4.bool():
                    color_array_dict['win_marg']['rd'].append(float(df1.get('win_marg')))
                    poly_list_dict['win_marg']['rd'].append(poly)
                else:
                    color_array_dict['win_marg']['bu'].append(float(df1.get('win_marg')))
                    poly_list_dict['win_marg']['bu'].append(poly)    
                
                if df5.bool():
                    color_array_dict['unemp1216']['rd'].append(float(df1_2.get('unemp1216')))
                    poly_list_dict['unemp1216']['rd'].append(poly)
                else:
                    color_array_dict['unemp1216']['bu'].append(float(df1_2.get('unemp1216')))
                    poly_list_dict['unemp1216']['bu'].append(poly)
                
                if df6.bool():
                    color_array_dict['manuper']['rd'].append(float(df1_2.get('manuper')))
                    poly_list_dict['manuper']['rd'].append(poly)
                else:
                    color_array_dict['manuper']['bu'].append(float(df1_2.get('manuper')))
                    poly_list_dict['manuper']['bu'].append(poly)
                if df7.bool():
                    color_array_dict['median_age']['rd'].append(float(df1_2.get('median_age')))
                    poly_list_dict['median_age']['rd'].append(poly)
                else:
                    color_array_dict['median_age']['bu'].append(float(df1_2.get('median_age')))
                    poly_list_dict['median_age']['bu'].append(poly)
                if df8.bool():
                    color_array_dict['median_income']['rd'].append(float(df1_2.get('median_income')))
                    poly_list_dict['median_income']['rd'].append(poly)
                else:
                    color_array_dict['median_income']['bu'].append(float(df1_2.get('median_income')))
                    poly_list_dict['median_income']['bu'].append(poly)
                if df9.bool():
                    color_array_dict['not_cit']['rd'].append(float(df1_2.get('not_cit')))
                    poly_list_dict['not_cit']['rd'].append(poly)
                else:
                    color_array_dict['not_cit']['bu'].append(float(df1_2.get('not_cit')))
                    poly_list_dict['not_cit']['bu'].append(poly)
    else:
        for i in range(len(shapes)):
            if records[i][0] in states and records[i][0] != 'AK' and records[i][0] != 'HI':
                points = shapes[i].points
                poly = Polygon(points)
                df1 = df[df['fips_code'] == int(records[i][3])]
                df1_2 = df_diff[df_diff['fips_code'] == int(records[i][3])]
                df2 = df1['winner'] == 'Gop' 
                df3 = df1['vote_diff1216'] < 0
                df4 = df1['win_marg'] < 0
                df5 = df1_2['unemp1216'] > 0
                df6 = df1_2['manuper'] > 0
                df7 = df1_2['median_age']>0
                df8 = df1_2['median_income']>0
                df9 = df1_2['not_cit']>0
                if df2.bool():
                    poly_list_dict['poly_list']['rd'].append(poly)
                else:
                    poly_list_dict['poly_list']['bu'].append(poly)
                if df3.bool():
                    color_array_dict['vote_diff']['rd'].append(float(df1.get('vote_diff1216')))
                    poly_list_dict['vote_diff']['rd'].append(poly)
                else:
                    color_array_dict['vote_diff']['bu'].append(float(df1.get('vote_diff1216')))
                    poly_list_dict['vote_diff']['bu'].append(poly)
                if df4.bool():
                    color_array_dict['win_marg']['rd'].append(float(df1.get('win_marg')))
                    poly_list_dict['win_marg']['rd'].append(poly)

                else:
                    color_array_dict['win_marg']['bu'].append(float(df1.get('win_marg')))
                    poly_list_dict['win_marg']['bu'].append(poly)
                if df5.bool():
                    color_array_dict['unemp1216']['rd'].append(float(df1_2.get('unemp1216')))
                    poly_list_dict['unemp1216']['rd'].append(poly)
                else:
                    color_array_dict['unemp1216']['bu'].append(float(df1_2.get('unemp1216')))
                    poly_list_dict['unemp1216']['bu'].append(poly)
                
                if df6.bool():
                    color_array_dict['manuper']['rd'].append(float(df1_2.get('manuper')))
                    poly_list_dict['manuper']['rd'].append(poly)
                else:
                    color_array_dict['manuper']['bu'].append(float(df1_2.get('manuper')))
                    poly_list_dict['manuper']['bu'].append(poly)
                if df7.bool():
                    color_array_dict['median_age']['rd'].append(float(df1_2.get('median_age')))
                    poly_list_dict['median_age']['rd'].append(poly)
                else:
                    color_array_dict['median_age']['bu'].append(float(df1_2.get('median_age')))
                    poly_list_dict['median_age']['bu'].append(poly)
                if df8.bool():
                    color_array_dict['median_income']['rd'].append(float(df1_2.get('median_income')))
                    poly_list_dict['median_income']['rd'].append(poly)
                else:
                    color_array_dict['median_income']['bu'].append(float(df1_2.get('median_income')))
                    poly_list_dict['median_income']['bu'].append(poly)
                if df9.bool():
                    color_array_dict['not_cit']['rd'].append(float(df1_2.get('not_cit')))
                    poly_list_dict['not_cit']['rd'].append(poly)
                else:
                    color_array_dict['not_cit']['bu'].append(float(df1_2.get('not_cit')))
                    poly_list_dict['not_cit']['bu'].append(poly)
                
    return [poly_list_dict, color_array_dict]

def plot_counties(df, df_diff, states, display_opts):
    args_to_vars = {'W': 'poly_list', 'w':'win_marg', 'd':'vote_diff', 'u':'unemp1216', 'm':'manuper', 'i':'median_income',
                    'a':'median_age', 'n':'not_cit'}
    title_dict = {'W': 'Winning Party by County in 2016 Election', 'd':'Difference in Winning Margin Between 2012 and 2015',
                  'w': 'Winning Margin by County in 2016', 'u': 'Difference in Unemployment Rate from 2012 to 2015',
                  'm': 'Difference in Manufcaturing Job Percentages between 2012 and 2015', 'i':'Difference in Median Income betwen 2012 and 2015',
                  'a':'Difference in Median Age betwen 2012 and 2015','n':'Difference in Percentage of Population not U.S. Citizens between 2012 and 2015'}
    poly_dict, color_dict = get_polygon_lists(df, df_diff, states)
    fig1 = plt.figure(figsize = (14, 6))
    rd_cmap1 = 'Reds'
    bu_cmap1 = 'Blues'
    rd_cmap2 = 'Reds'
    bu_cmap2 = 'Blues'
    if display_opts[0] == 'W':
        rd_cmap1 = 'bwr_r'
        bu_cmap1 = 'bwr'
    if display_opts[1] == 'W':
        rd_cmap2 = 'bwr_r'
        bu_cmap2 = 'bwr'
    bu_list1 = poly_dict[args_to_vars[display_opts[0]]]['bu']
    rd_list1 = poly_dict[args_to_vars[display_opts[0]]]['rd']
    z_bu1 = color_dict[args_to_vars[display_opts[0]]]['bu']
    z_rd1 = color_dict[args_to_vars[display_opts[0]]]['rd']
    bu_list2 = poly_dict[args_to_vars[display_opts[1]]]['bu']
    rd_list2 = poly_dict[args_to_vars[display_opts[1]]]['rd']
    z_bu2 = color_dict[args_to_vars[display_opts[1]]]['bu']
    z_rd2 = color_dict[args_to_vars[display_opts[1]]]['rd']
    ax1=fig1.add_subplot(121)
    bu_collection1 = PatchCollection(bu_list1, array = np.array(z_bu1)*100, cmap=plt.get_cmap(bu_cmap1), alpha=1)
    rd_collection1 = PatchCollection(rd_list1, array = np.array(z_rd1)*100, cmap = plt.get_cmap(rd_cmap1), alpha = 1)
    ax1.add_collection(bu_collection1)
    ax1.add_collection(rd_collection1)
    ax1.set_xlabel('Longitude ($^{\circ}$E)')
    ax1.set_ylabel('Lattitude ($^{\circ}$N)')
    ax1.autoscale_view()
    ax1.set_title(title_dict[display_opts[0]])
    ax2 = fig1.add_subplot(122)
    bu_collection2 = PatchCollection(bu_list2, array = np.array(z_bu2)*500, cmap=plt.get_cmap(bu_cmap2), alpha=1)
    rd_collection2 = PatchCollection(rd_list2, array = np.array(z_rd2)*500, cmap = plt.get_cmap(rd_cmap2), alpha = 1)
    ax2.add_collection(bu_collection2)
    ax2.add_collection(rd_collection2)
    ax2.set_xlabel('Longitude ($^{\circ}$E)')
    ax2.set_ylabel('Lattitude ($^{\circ}$N)')
    ax2.autoscale_view()
    ax2.set_title(title_dict[display_opts[1]])
    #html_fig = mpld3.fig_to_html(fig1, template_type = "general")
    #print(html_fig)
    plt.savefig('test_map_plot.png')
    print("<img src=\"test_map_plot.png\" alt=\"Map\" height=\"500\" width=\"1200\">")




if __name__=="__main__":
    args = sys.argv[1:]
    display_opts = args[0]
    states = args[1:]
    df1 = pd.read_csv('e.csv', delimiter = ',', usecols = [0,1,2,28,29,32], names = ['fips_code', 'state', 'county', 'win_marg','winner', 'vote_diff1216'])
    df_diff = pd.read_csv('diff_1215.csv', delimiter = ',', usecols = [0,5,6,8,15,22], names = ['fips_code','median_age','median_income','manuper','not_cit', 'unemp1216'])
    df_diff.iloc[2412, 0] = 46113
    plot_counties(df1, df_diff, states, display_opts)
    
    
    
    
    
    
    
    
    
    
    