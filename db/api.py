from fastapi import FastAPI
import psycopg

from db.dblogic import *
from StravaAPI.running import *

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
    runsDb = count_runs_in_db()
    runs = get_new_runs(runsDb)
    write_runs_to_db(runs)
    print(runs)
    return runs #"Db data refreshed"

@app.get("/runs/hard-refresh")
def refresh_all_runs_from_strava():
    clear_runs()
    runs = get_runs()
    write_runs_to_db(runs)
    
    return runs#"Database Hard Refreshed"