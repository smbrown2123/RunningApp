# functions for drawing charts

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import math
import formats

def display_all_runs(df: pd.DataFrame):
    norm = plt.Normalize(df['pace'].min(), df['pace'].max())
    colours = plt.cm.RdYlGn_r(norm(df['pace']))

    mpl.rcParams['axes.titlesize'] = 18
    
    Chart = df.plot.bar("date", "distance", color = colours, legend = False, title = 'All Runs Over Time', picker = True)
    Chart.set_ylabel('Distance (km)')
    Chart.set_xlabel('Run')
    Chart.set_xticklabels('')
    
    InfoText = None
    
    def on_select(event):
        nonlocal InfoText
        if InfoText is not None:
            InfoText.remove()
            InfoText = None
            
        # use the returned rectangle data from clicking on a bar to get a number corresponding to the run
        # rect x starts -0.25, 0.75, 1. This corresponds to runs 1, 2, 3
        xCoord = event.artist.xy[0] 
        xCoordWhole = math.modf(xCoord)[1]
        if xCoord > 0:
            runNumber = int(xCoordWhole + 2)
        else:
            runNumber = 1
        
        # lookup num -1 as dataframe locations start from 0 
        run = df.loc[runNumber - 1]
        Date = run['date']
        Distance = formats.round_distance(run['distance'])
        Pace = formats.convert_decimnal_pace(run['pace'])
        Time = formats.convert_from_mins(run['time'])
        
        InfoText = Chart.text(Chart.get_xlim()[1],Chart.get_ylim()[1], f'{Date}\n{Distance}\n{Pace}\n{Time}', fontsize = 12)
        
        plt.draw()
    
    Chart.figure.canvas.mpl_connect('pick_event', on_select)
    
    plt.show()
    
