import psycopg
import json
from datetime import datetime

def write_runs_to_db(runs: list):
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    runs.reverse()  
    for i in range(0, len(runs)-1):
        data = runs[i]
        pace = float(data['pace'])
        distance = float(data['distance'])
        duration = float(data['time'])
        strdate = str(data['date'])
        date = datetime.strptime(strdate, "%d-%m-%Y").date()

        # Connect to an existing database
        with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                # Pass data to fill a query placeholders and let Psycopg perform
                # the correct conversion (no SQL injections!)
                cur.execute(
                    "INSERT INTO run (pace, distance, duration, date) VALUES (%s, %s, %s, %s)",
                    (pace, distance, duration, date))

                # Make the changes to the database persistent
                conn.commit()
                
def get_db_parameters():
    with open('db/dbparams.json') as f:
        params = json.load(f)

    dbname = params["parameters"]["dbname"]
    user = params["parameters"]["user"]
    host = params["parameters"]["host"]
    password = params["parameters"]["password"]
    port = params["parameters"]["port"]
    
    return dbname, user, host, password, port