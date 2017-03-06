# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import shapefile as sf
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def get_polygon_lists(df, states):
    filename = open("elpo12p010g.shp")
    filename2 = open("elpo12p010g.dbf")
    shape_file = sf.Reader(shp = filename, dbf = filename2)
    poly_list_bu = []
    poly_list_rd = []
    z_rd = []
    z_bu = []
    diff_rd = []
    diff_bu = []
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
                df1 = df[df['fips'] == int(records[i][3])]
                df2 = df1['winner'] == 'Gop' 
                df3 = df1['diff1216'] < 0
                if df2.bool():
                    poly_list_rd.append(poly)
                else:
                    poly_list_bu.append(poly) 
                if df3.bool():
                    z_rd.append(float(df1['diff1216'].base))
                    diff_rd.append(poly)
                else:
                    z_bu.append(float(df1['diff1216'].base))
                    diff_bu.append(poly)
    else:
        for i in range(len(shapes)):
            if records[i][0] in states and records[i][0] != 'AK' and records[i][0] != 'HI':
                points = shapes[i].points
                poly = Polygon(points)
                df1 = df[df['fips'] == int(records[i][3])]
                df2 = df1['winner'] == 'Gop'
                df3 = df1['diff1216'] < 0
                if df2.bool():                    
                    poly_list_rd.append(poly)
                else:
                    poly_list_bu.append(poly)
                if df3.bool():
                    z_rd.append(float(df1['diff1216'].base))
                    diff_rd.append(poly)
                else:
                    z_bu.append(float(df1['diff1216'].base))
                    diff_bu.append(poly)
    return [poly_list_bu, poly_list_rd, diff_rd, diff_bu, z_rd, z_bu]

def plot_counties(df, states):
    bu_list, rd_list, diff_rd, diff_bu, z_rd, z_bu = get_polygon_lists(df, states)
    z = np.array([10])
    fig1 = plt.figure(figsize = (11, 11))
    ax1=fig1.add_subplot(121)
    bu_collection1 = PatchCollection(bu_list, array = z, cmap=plt.get_cmap('bwr'), alpha=1)
    rd_collection1 = PatchCollection(rd_list, array = z, cmap = plt.get_cmap('bwr_r'), alpha = 1)
    ax1.add_collection(bu_collection1)
    ax1.add_collection(rd_collection1)
    ax1.set_xlabel('Longitude ($^{\circ}$E)')
    ax1.set_ylabel('Lattitude ($^{\circ}$N)')
    ax1.autoscale_view()
    ax1.set_title('Winning Party by County in 2016 Election')
    ax2 = fig1.add_subplot(122)
    bu_collection2 = PatchCollection(diff_bu, array = np.array(z_bu), cmap=plt.get_cmap('Blues'), alpha=1)
    rd_collection2 = PatchCollection(diff_rd, array = np.array(z_rd), cmap = plt.get_cmap('Reds'), alpha = 1)
    ax2.add_collection(bu_collection2)
    ax2.add_collection(rd_collection2)
    ax2.set_xlabel('Longitude ($^{\circ}$E)')
    ax2.set_ylabel('Lattitude ($^{\circ}$N)')
    ax2.autoscale_view()
    ax2.set_title('Difference in Votes Cast by County Between 2012 and 2016')
    html_fig = mpld3.fig_to_html(fig1, template_type = "simple")
    print(html_fig)


if __name__=="__main__":
    args = sys.argv[1:]
    df = pd.read_csv('e.csv', delimiter = ',', usecols = [0,1,2,29,32], names = ['fips', 'state', 'county', 'winner', 'diff1216'])
    df.iloc[2547, 1] = 'DC County'
    plot_counties(df, args)
    
    
    
    
    
    
    
    
    
    