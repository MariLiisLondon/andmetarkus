
boys_names = ['Peeter', 'Ain', 'Kusti', 'Mark', 'Paul']
boys_names.append('Jaan')

girls_names = ['Mari-Liis', 'Kati', 'Jana', 'Liis', 'Ann']  
girls_names.append('Katrin')
names = [] # tühi nimekiri
names = boys_names + girls_names
#print("names:" + str(names)) 

# sorteeritud nimed
#print("names:", sorted(names))

# vali esimene nimi kahest kokku pandud sprteeritud listis
##print("esimene nimi:", sorted(names)[0]) 

# sorteeritud nimed tagurpididi
##print("tagurpidi:", sorted(names, reverse=True))


# list
transactions = [1,2,2,3,4,5,6,7,8,9,10]
unic_transactions = set(transactions)
#print(unic_transactions)
all_transactions = list(range(2, 22))
#print(all_transactions)
common_transactions = unic_transactions.intersection(all_transactions)
#print("common:", common_transactions)

# dictionary
my_company_data = { id: 1000,
                    "name" : "Best Company ever",
                     "year_sales" : {125, 256, 325, 400, 512},
                     "employees" : {"Mari-Liis", "Kati", "Jana"}}
print(my_company_data) 

my_company_data["name"] = "uus nimi" # muudan nime
print(my_company_data)

#my_company_data.update[year_sales = [125]=500000000] # muudan müüki
#print(my_company_data)


# tuple
popular_boys_names = ('Peeter', 'Ain', 'Kusti', 'Mark', 'Paul')


