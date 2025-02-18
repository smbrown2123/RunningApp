import json
import csv
import running
import pandas as pd
import charts
import generic

'''with open('output.json', 'w', encoding = 'utf-8') as f:
    json.dump(runs, f, ensure_ascii = 'False, indent = 4')

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['distance', 'date', 'time', 'pace']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(runs) '''

runs = running.get_runs()
df = pd.DataFrame(runs)
df.to_csv()

charts.display_all_runs(df) 