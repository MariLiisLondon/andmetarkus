
import pandas as pd

# Lae elektrihindade graafikud

source_data = pd.read_json(r'C:\Users\opilane\Documents\andmetarkus-1\python\DAY3\el_data_2024.json')
electricity_data = pd.json_normalize(source_data["data"])
print(electricity_data.head())

source_data_2 = pd.read_csv(r'C:\Users\opilane\Documents\andmetarkus-1\python\DAY3\tallinn_harku_2024.csv')
weather_data = pd.DataFrame(source_data_2)
print(weather_data.head())

weather_data['datetime'] = pd.to_datetime(
    weather_data['Aasta'].astype(str) + '-'
    + weather_data['Kuu'].astype(str) + '-'
    + weather_data['Päev'].astype(str) + ' '
    + weather_data['Kell UTC'].astype(str))

merged = pd.merge(electricity_data, weather_data, on='datetime', how='inner')
print(merged.columns)


    