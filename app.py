# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print("Hello DARA 2024")

"""
print("DARA students are very quiet")

print ("Please chat in slack")
"""

"""
VARIABLE IN PYTHON 

SN = 2024
Age = 25
Kenya_code = 254 
my_date = 21 
pi = 3.142
Height = 5.8
YourAge = "twenty"
comment = "give me a thumbs up"


THIS IS WRONG VARIABLE NAME FORMAT:
2age = 50
my age = 50 
my-age = 50

-------------------------------------------------------------------------------

IMPORTANT VARIABLE TYPES:
    1. INTEGER - WHOLE NUMBER: 50, -100
    2. FLOAT - DECIMAL NUMBER: -0.5, 1500.1
    3. STRING - TEXT:: "a", "50", "DARA", "DARA CODING SCHOOL"
    
"""

"""
HOW TO READ IN CSV FILE IN PYTHON
"""

import pandas

countrydata_file = pandas.read_csv("country_data.csv")

print(countrydata_file)

diabdata_file = pandas.read_csv("diab_data.csv")

print(diabdata_file)

housingdata_file = pandas.read_csv("housing_data.csv")

print(housingdata_file)

#insurancedata_file = pandas.read_csv("insurance_data.csv")

#print(insurancedata_file)

iris_file = pandas.read_csv("iris.csv")

print(iris_file)

# The insurance file is giving a ParserError: Error tokenizing data. C error: Expected 1 fields in line 7, saw 2



