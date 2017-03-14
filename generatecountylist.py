import sqlite3

command ="SELECT county, state FROM election_results;"
connection = sqlite3.connect("data1215-full.db")
c = connection.cursor()
results = c.execute(command).fetchall()
county_list = []
for result in results:
    temp = result[0].strip().replace(" ", "_")+"_"+result[1].strip()
    county_list.append(temp)
county_results = []
state = county_list[0][-2:]
county = county_list[0][:-3].replace("_", " ")
state = "\"" + state + "\""
county = "\"" + county + "\""
command ="SELECT * FROM election_results AS e INNER JOIN fd12 ON e.fips_code=fd12.fips_code INNER JOIN fd15 ON e.fips_code=fd15.fips_code INNER JOIN diff_1215 AS d ON e.fips_code=d.fips_code INNER JOIN unemployment AS u ON e.fips_code=u.fips_code  WHERE e.county =" + county + " AND e.state=" + state +" ;"
result = c.execute(command).fetchall()
county_results.append(result)
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
print(get_header(c))
print(result)
#css_for_table = "<style> table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%;} td, th { border: 1px solid #dddddd; text-align: left; padding: 8px;} tr:nth-child(even) {background-color: #dddddd;}</style>"
