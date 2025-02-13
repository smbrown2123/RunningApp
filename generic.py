import calls

def get_numner_of_activities(ID: int, AccessToken: str):
    data = calls.get_stats(ID, AccessToken)
    runs = data['all_run_totals']['count'] 
    cycles = data['all_ride_totals']['count'] 
    swims = data['all_swim_totals']['count']
    
    activities = runs + cycles + swims
    
    return activities

def nearest_whole_km(Distance: float):
    DistanceInt = int(Distance)
    DistacneNearest = round(DistanceInt / 1000)
    
    return DistacneNearest

def convert_to_km(Distance: float):
    Distance = round(Distance/1000, 2)
    
    return Distance