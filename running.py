import math

def nearest_whole_km(distance: float):
    RunDistanceInt = int(distance)
    RunDistacneNearest = math.ceil(RunDistanceInt / 1000)
    
    return RunDistacneNearest