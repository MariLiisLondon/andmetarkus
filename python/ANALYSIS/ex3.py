import pandas as pd


file_name = r"C:\Users\opilane\Documents\andmetarkus-1\python\ANALYSIS\ProductTable.xlsx"

data = pd.read_excel(file_name)# loeme ekseli andmed

data_dict = data.to_dict(orient='records') # tee dictionaris, võta dictionarist ja nii, et iga reida oleks eraldi

print(data_dict)


file_csvst = r"C:\Users\opilane\Documents\andmetarkus-1\python\ANALYSIS\CustomerTable.csv"

data_csv = pd.read_csv(file_csvst) # loeme csv faili
data_csv_dict = data_csv.to_dict # tee dictionaris, võta dictionarist ja nii, et iga reida oleks eraldi
print(data_csv_dict)
