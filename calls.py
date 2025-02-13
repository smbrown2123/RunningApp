import requests

def get_stats(ID, AccessToken):
    URL = f'https://www.strava.com/api/v3/athletes/{ID}/stats'
    PARAMS = {'access_token':AccessToken}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    
    return data