""" eu_northen_contry_codes = ["DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE"]  """
""" for CODE in eu_northen_contry_codes:
    print(CODE)  """

""" print("\n FOR loop, Lahendus 1 \n")

 # VÄLJAKS ESIMSED 2
for i in range(2): #SEE NUMBER ON I
    print(eu_northen_contry_codes[i]) 

print("\nLahendus 2 \n")

for code in eu_northen_contry_codes[:2]: #SEE NUMBER ON CODE
    print(code) 


print("\ntrüki tsükilst välja 2kuni neljas \n")

for code in eu_northen_contry_codes[1:4]: #SEE NUMBER ON CODE
    print(code, end=" ") # paneb järjekorda

print("\n viimased viis \n")
for code in eu_northen_contry_codes[-5:]: #SEE NUMBER ON CODE
    print(code, end=" ") # paneb järjekorda

print("\n lahendus 2, lihtsalt tlemendid tagurpidi\n")
for code in reversed(eu_northen_contry_codes): #SEE NUMBER ON CODE
    print(code, end=" ") # paneb järjekorda

print("\n lahendus 3,  len-iga, teeb üle ühe, alustab teisest koodist\n") """
""" 
for code in range(0,len(eu_northen_contry_codes),-2):
    print(code[i])  """  


# väljastame koodi, mis algavd e tähisega 
""" 
for code in eu_northen_contry_codes:
    if code.startswith("E"):
        print(code)

# lahendus 2
for code in eu_northen_contry_codes:
    if code[0] == "E":
        print(code)
 """

nimed=["Mari", "Jüri", "Kati", "Peeter", "Jaan", "Katrin"]

sorted_names = {"M" :[]}

for name in nimed:
    first_letter = name[0]
    if first_letter not in sorted_names:
        sorted_names[first_letter] = []
    sorted_names[first_letter].append(name) 
print(sorted_names)


    