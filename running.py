import calls
import math
import generic
import json

with open('json.json') as f:
   params = json.load(f)


def get_total_distance(ID: int, AccessToken: str):
    data = calls.get_stats(ID, AccessToken)

    RunDistance = data['all_run_totals']['distance'] 
    distance = nearest_whole_km(RunDistance)
    
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
                Date = activity['start_date_local']
                Distance = convert_to_km(activity['distance'])
                runs.append({'Distance': Distance,'Date': Date})
    
    return runs
    
def nearest_whole_km(Distance: float):
    RunDistanceInt = int(Distance)
    RunDistacneNearest = round(RunDistanceInt / 1000)
    
    return RunDistacneNearest

def convert_to_km(Distance: float):
    RunDistance = round(Distance/1000, 2)
    
    return RunDistance