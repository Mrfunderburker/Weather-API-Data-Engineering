import pandas as pd
import json
import requests

url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-52.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=auto"
response = requests.get(url)

data = response.json()

with open("data/json/url.json", mode = "w") as file:
    json.dump(data, file, indent = 4)

    df = pd.DataFrame(data)

    # Extract the 'hourly' data from the fetched data
hourly_data = data.get('hourly', {})
# Prepare the data to be saved into a DataFrame
json_data = {
    "time": hourly_data.get("time", []),
    "temperature_2m": hourly_data.get("temperature_2m", []),
    "relative_humidity_2m": hourly_data.get("relative_humidity_2m", []),
    "precipitation": hourly_data.get("precipitation", []),
    "surface_pressure": hourly_data.get("surface_pressure", [])}

df =pd.DataFrame(json_data)

df.to_csv("data/csv/new.csv", index=False)