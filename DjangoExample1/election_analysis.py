from functools import reduce
import sqlite3
import json
import re
import os

# Use this filename for the database
DATA_DIR = os.path.dirname(__file__)
DATABASE_FILENAME = os.path.join(DATA_DIR, 'data.db')

def find_data(args_from_ui):
	connection = sqlite3.connect("data.db")
	c = connection.cursor()  #set up the connection to database
	if args_from_ui["county"] or args_from_ui["state"]:
		command = construct_sql_command(args_from_ui)
		results = c.execute(command).fetchall()
		header = get_header(c)
	else:
		results = []
	connection.close()
	if not results:
		header = []

	return (header, results)
	
def construct_sql_command(args_from_ui):
	s_command = "SELECT state, county, total_2008, dem_2008, gop_2008, oth_2008, "
	s_command += "dem_08_perc, gop_08_perc, oth_08_perc, win_marg_08, winner_08, "
	s_command += "total_2012, dem_2012, gop_2012, oth_2012, "
	s_command += "dem_12_perc, gop_12_perc, oth_12_perc, win_marg_12, winner_12, "
	s_command += "total_2016, dem_2016, gop_2016, oth_2016, "
	s_command += "dem_16_perc, gop_16_perc, oth_16_perc, win_marg_16, winner_16, "
	s_command += "diff_0812, diff_1216, diff_0816, direction_0812, direction_0816, direction_1216"
	f_command = " FROM election_results "
	w_command = ""
	if args_from_ui["county"] or args_from_ui["state"]:
		w_command = "WHERE "
	if args_from_ui["county"]:
		w_command += " (county='" + args_from_ui["county"] + "') "
	if args_from_ui["state"] and args_from_ui["county"]:
		for state in args_from_ui["state"]:
			w_command += " OR (state='" + state + "') "
	if args_from_ui["state"] and not args_from_ui["county"]:
		for state in args_from_ui["state"]:
			w_command += " (state='" + state + "') OR "
	w_command[:len(w_command)-3]
	command = s_command + f_command + w_command + ';'

	return command


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
