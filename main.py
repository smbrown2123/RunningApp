import json
import running
import pandas as pd
import matplotlib.pyplot as plt

with open('params.json') as f:
   params = json.load(f)

ID = params["parameters"]["id"]
AccessToken = params["parameters"]["accesstoken"]

runs = running.get_runs(ID, AccessToken)

with open('output.json', 'w', encoding = 'utf-8') as f:
    json.dump(runs, f, ensure_ascii = 'False, indent = 4')
    
#df = pd.DataFrame(runs)
#lines = df.plot.scatter("Date", "Distance")

#plt.show()