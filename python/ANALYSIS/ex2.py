import csv
data_from_csv=[]

# too csv faili

with open(r'C:\Users\opilane\Documents\andmetarkus-1\python\ANALYSIS\CustomerTable.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',') #nimetame ta readeriks

    data_from_csv = list(reader) #teeme listi
    print(data_from_csv)
    # loeme read

insert_statment = "INSERT INTO customers"
#statment + veergude nimed
insert_statment = insert_statment + f"\n({' '.join(data_from_csv[0])}) \nvalues"
print(insert_statment)

# loeme veerud, for tsükkel
for row in data_from_csv[1:]: #alustame teisest reast
    insert_statment = insert_statment + f"\n({' '.join(row)}),"
print(insert_statment)
#eemaldame viimase komakese
insert_statment = insert_statment[:-1] 
print(insert_statment)
  
