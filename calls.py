import requests

def get_stats(ID: int, AccessToken: str):
    URL = f'https://www.strava.com/api/v3/athletes/{ID}/stats'
    PARAMS = {'access_token':AccessToken}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    
    return data

def get_activities(AccessToken: str,Page: int, PerPage = 200):
    URL = 'https://www.strava.com/api/v3/athlete/activities'
    PARAMS = {'access_token':AccessToken, 'per_page':PerPage, 'page':Page}
    
    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    
    return data