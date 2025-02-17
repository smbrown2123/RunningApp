import calls
import math
import generic
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def get_total_distance():
    data = calls.get_stats()

    RunDistance = data['all_run_totals']['distance'] 
    distance = generic.nearest_whole_km(RunDistance)
    
    return distance

def get_numner_of_runs():
    Data = calls.get_stats()
    Runs = Data['all_run_totals']['count'] 
    
    return Runs

def get_runs():
    runs = []
    NumActivities = generic.get_numner_of_activities()
    NumCalls = math.ceil(NumActivities / 200)
    for i in range (1, NumCalls + 1):
        Activities = calls.get_activities(i)
        for activity in Activities:
            if activity['type'] == 'Run':
                DateTime = datetime.strptime(activity['start_date_local'], "%Y-%m-%dT%H:%M:%SZ")
                Date = DateTime.strftime("%d-%m-%Y")
                Distance = generic.convert_to_km(activity['distance'])
                Time = activity['moving_time']/60
                Pace = (Time) / Distance
                runs.append({'distance': Distance,'date': Date, 'time': Time, 'pace': Pace})
    
    return runs

def display_all_runs(df: pd.DataFrame):
    norm = plt.Normalize(df['pace'].min(), df['pace'].max())
    colours = plt.cm.RdYlGn_r(norm(df['pace']))
    
    Chart = df.plot.bar("date", "distance", color = colours, legend = False, title = 'All Runs Over Time')
    Chart.set_ylabel('Distance (km)')
    Chart.set_xlabel('Run')
    Chart.set_xticklabels('')

    plt.show()