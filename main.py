import requests
import json
import running

with open('params.json') as f:
   params = json.load(f)

ID = params["parameters"]["id"]
AccessToken = params["parameters"]["accesstoken"]

URL = f'https://www.strava.com/api/v3/athletes/{ID}/stats'

PARAMS = {'access_token':AccessToken}

r = requests.get(url = URL, params = PARAMS)

data = r.json()
with open('response.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii = 'False, indent = 4')

RunDistance = data['all_run_totals']['distance'] 
distance = running.nearest_whole_km(RunDistance)
print(f'{distance} km')