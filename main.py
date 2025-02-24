import csv
import pandas as pd

from running import *
from charts import *

#Uncomment below to use API (requires params to be filled in)
''' 
runs = get_runs()
df = pd.DataFrame(runs)
display_all_runs(df) 
'''

#Comment out the follwoing code to use the API, this code reads data from the csv file instead of fetching from Strava
csvData = pd.read_csv('output.csv')
df = pd.DataFrame(csvData)
display_all_runs(df) 
