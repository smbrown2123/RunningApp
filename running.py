# functions for getting running data from the api
import math
from datetime import datetime

import calls
from generic import *
from formats import *

def get_total_distance():
    Data = calls.get_stats()

    RunDistance = Data['all_run_totals']['distance'] 
    Distance = nearest_whole_km(RunDistance)
    
    return Distance

def get_numner_of_runs():
    Data = calls.get_stats()
    Runs = Data['all_run_totals']['count'] 
    
    return Runs

def get_runs():
    runs = []
    NumActivities = get_numner_of_activities()
    NumCalls = math.ceil(NumActivities / 200)
    for i in range (1, NumCalls + 1):
        Activities = calls.get_activities(i)
        for activity in Activities:
            if activity['type'] == 'Run':
                DateTime = datetime.strptime(activity['start_date_local'], "%Y-%m-%dT%H:%M:%SZ")
                Date = DateTime.strftime("%d-%m-%Y")
                Distance = convert_to_km(activity['distance'])
                Time = activity['moving_time']/60
                Pace = Time / Distance
                runs.append({'distance': Distance,'date': Date, 'time': Time, 'pace': Pace})
    
    return runs