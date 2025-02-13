import requests
import json
import running

with open('params.json') as f:
   params = json.load(f)

id = params["parameters"]["id"]
accessToken = params["parameters"]["accesstoken"]

URL = f'https://www.strava.com/api/v3/athletes/{id}/stats'

PARAMS = {'access_token':accessToken}

r = requests.get(url = URL, params = PARAMS)

data = r.json()
with open('response.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii = 'False, indent = 4')

RunDistance = data['all_run_totals']['distance'] 
distance = running.nearest_whole_km(RunDistance)
print(f'{distance} km')