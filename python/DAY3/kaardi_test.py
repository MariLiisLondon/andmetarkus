import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#laeme eesti maakonndade geograafilised andmed
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
estonia = gdf[gdf['name'] == 'Estonia']
estonia

#lahutama maakonnad eralid objektideks
estonia = estonia.explode(index_parts=False).reset_index(drop=True)
estonia['maakond'] = ['Harju', 'Hiiu', 'Ida-Viru', 'Jõgeva', 'Järva', 'Lääne', 'Lääne-Viru', 'Põlva', 'Pärnu', 'Rapla', 'Saare', 'Tartu', 'Valga', 'Viljandi', 'Võru']

# laeme elanik arvu andmed
