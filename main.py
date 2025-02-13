import json
import running

with open('params.json') as f:
   params = json.load(f)

ID = params["parameters"]["id"]
AccessToken = params["parameters"]["accesstoken"]

runs = running.get_runs(ID, AccessToken)
for i in runs:
    print(i)