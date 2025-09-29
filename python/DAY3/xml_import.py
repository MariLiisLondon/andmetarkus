import requests
import pandas as pd


url = r"https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"

response = requests.get(url) #võtan requesti kataloogist, get meetodi e nn tellin ppest paki, *response' on terve pakk
xml_content = response.content # anna pakile nime ja  teen response paki lahti .contentiga, xml_content on kaup paki sees

#proovi leida sobiv  Xpath
df = pd.read_xml(xml_content, xpath=".//place")
print(df.head())


# --- ÜHEREALINE LAHENDUS ---
# Leia miinimumtemperatuuriga rida ja võta sealt nimi
place_with_min_temp = df.loc[df['tempmin'].idxmin(), 'name']

print(f"Kõige madalam temperatuur on kohas: {place_with_min_temp} +{df['tempmin'].min()}°C")

