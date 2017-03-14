To run properly, execute "chmod 777 ." (as you suggested!) so that the VM can save images to the folder for the webpage to access.
Go to localhost/index.html to access the website from a browser. There are directions onscreen. The homepage features some ideas taken from popular media you may want to test and potential output you may want to try and produce.

The webpages: elections.php, regression.php, maps.php, information.php
    Webpages constructed based on input to URL: countydata.php?county=Example County and statedata.php?state=EX

Python files support the functioning of the website: generate_county_page.py, generate_state_page.py, plot_counties.py, linreg2.py, correlationmap.py

The files have comments which explain how to update the files if the database name is changed or data fields are added.

The website uses php5, HMTL5, CSS, Python3, Python2, and SQLite3. This allowed us to customize the website to a great extent and format the output in an accessible way. 

To prevent command injection, the website uses checkboxes and dropdowns. The exception is the county and state data pages, you could type in a command, so it is sent to the python file as a string and the python file processes it.

elections.php: home for election analyzer. All tools can be accessed on this page at once by following the onscreen instructions. The table features all counties will links to each's county page as well as any data fields you select. If the table overflows, scroll to the side to side the rest. For any information on variables or data sources, following the link to the information page.

regression.php: A page which gives easy access to the regression tool. Produced by linreg2.py.

maps.php: A page which gives easy access to the mapping tool. Produced by plot_counties.py.

information.php: A page giving variable descriptions and source information.

countydata.php?county=Example County: A page for a particular county displaying all information for a county in easy to evaluate visual form as well as a raw data table (for those who might want it, variable descriptions on information.php). Produced by generate_county_page.py.

statedata.php?state=EX: State level data put together county-by-county from SQLite3 commands. A page for a particular state displaying all information for a state in easy to evaluate visual form as well as a raw data table (for those who might want it, variable descriptions on information.php). Produced by generate_state_page.

Data: Data was taken from sources listed on the information page. We put together estimates from different years and many different files. The raw data to produced useful parameters and statistics, like percentages and differences, which were loaded into the database file data1215.db.

The various csv and xls files contain the data which was loaded into the data1215.db.