import json
import running

with open('params.json') as f:
   params = json.load(f)

ID = params["parameters"]["id"]
AccessToken = params["parameters"]["accesstoken"]

distance = running.get_total_distance(ID, AccessToken)

print(f'{distance} km')