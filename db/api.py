from fastapi import FastAPI
import psycopg

from db.dblogic import *
from StravaAPI.running import get_runs

app = FastAPI()

@app.get("/runs")
def get_all_runs():
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    data =[]
    
    with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM run")
                for record in cur:
                    data.append(record)
                   
    return data

@app.get("/run/{run_id}")
def get_run_by_id(run_id):
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    data =[]
    
    with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM run where id= (%s)",(run_id,))
                for record in cur:
                    data.append(record)
                   
    return data

@app.get("/runs/refresh")
def refresh_data_from_strava():
    runs = get_runs()
    write_runs_to_db(runs)
    
    return runs