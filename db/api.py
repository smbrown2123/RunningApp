from fastapi import FastAPI
import psycopg

from db.dblogic import *
from StravaAPI.running import get_runs

app = FastAPI()

@app.get("/runs")
def all_runs():
    response = get_all_runs_from_db()
    
    return response

@app.get("/run/{run_id}")
def get_run_by_id(run_id):
    response = get_run_from_db_by_id(run_id)
    
    return response

@app.get("/runs/refresh")
def refresh_data_from_strava():
    runs = get_runs()
    write_runs_to_db(runs)
    
    return "Db data refreshed"