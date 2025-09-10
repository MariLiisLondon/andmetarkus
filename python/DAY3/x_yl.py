# Laeme excelist ilmaandmed
import pandas as pd

data = pd.read_excel(r'C:\Users\opilane\Documents\andmetarkus-1\python\DAY3\Tallinn-Harku-2004-2024.xlsx',
                     skiprows=2)
df = pd.DataFrame(data)

# Filtreeri ainult read, kus Aasta on 2024
df_2024 = df[df['Aasta'] == 2024]


# Salvesta DataFrame uude faili
df_2024.to_csv(r'C:\Users\opilane\Documents\andmetarkus-1\python\DAY3\Tallinn-Harku-2004-2024.xlsx', index=False)