import math
import calls

def get_total_distance(ID, AccessToken):
    data = calls.get_stats(ID, AccessToken)

    RunDistance = data['all_run_totals']['distance'] 
    distance = nearest_whole_km(RunDistance)
    
    return distance

def nearest_whole_km(distance: float):
    RunDistanceInt = int(distance)
    RunDistacneNearest = math.ceil(RunDistanceInt / 1000)
    
    return RunDistacneNearest