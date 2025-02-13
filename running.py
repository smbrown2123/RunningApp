import calls
import math
import generic
import json
from datetime import datetime

def get_total_distance(ID: int, AccessToken: str):
    data = calls.get_stats(ID, AccessToken)

    RunDistance = data['all_run_totals']['distance'] 
    distance = generic.nearest_whole_km(RunDistance)
    
    return distance

def get_numner_of_runs(ID: int, AccessToken: str):
    Data = calls.get_stats(ID, AccessToken)
    Runs = Data['all_run_totals']['count'] 
    
    return Runs

def get_runs(ID: int, AccessToken: str):
    runs = []
    NumActivities = generic.get_numner_of_activities(ID, AccessToken)
    NumCalls = math.ceil(NumActivities / 200)
    for i in range (1, NumCalls + 1):
        Activities = calls.get_activities(AccessToken, i)
        for activity in Activities:
            if activity['type'] == 'Run':
                DateTime = datetime.strptime(activity['start_date_local'], "%Y-%m-%dT%H:%M:%SZ")
                Date = DateTime.strftime("%d-%m-%Y")
                Distance = generic.convert_to_km(activity['distance'])
                Time = activity['moving_time']/60
                Pace = (Time) / Distance
                runs.append({'Distance (km)': Distance,'Date': Date, 'Time (m)': Time, 'Pace (m/km)': Pace})
    
    return runs
