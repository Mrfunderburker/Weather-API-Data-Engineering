import pandas as pd
import requests
import json

url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-52.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=auto"
r = requests.get(url)

data = r.json()

print(data)