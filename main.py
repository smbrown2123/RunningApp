import json
import csv
import running
import pandas as pd


with open('params.json') as f:
   params = json.load(f)

ID = params["parameters"]["id"]
AccessToken = params["parameters"]["accesstoken"]

runs = running.get_runs(ID, AccessToken)

with open('output.json', 'w', encoding = 'utf-8') as f:
    json.dump(runs, f, ensure_ascii = 'False, indent = 4')

#DataJson = pd.read_json(runs)
df = pd.DataFrame(runs)
DataCsv = df.to_csv()

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['distance', 'date', 'time', 'pace']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(runs)

running.display_all_runs(df)