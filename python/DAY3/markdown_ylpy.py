import requests
import pandas as pd
import matplotlib.pyplot as plt

### ÜL1. Too andmed API-st
# kasutajad
kasutajad_url = 'https://jsonplaceholder.typicode.com/users'
kasutajad_response = requests.get(kasutajad_url) # request on pythony libary,kus on kirjas, mida pead kasutama, et erinevatel viisidel andmeid pärida, get küsib andmeid 


# nende ülesanded
tegevusalad_url = 'https://jsonplaceholder.typicode.com/todos'
tegevusalad_response = requests.get(tegevusalad_url)



### ÜL2. Töötle andmeid
# - [ ] Seo 'todos' vastava kasutajaga 'userId' abil.  
# - [ ] Arvuta iga kasutaja kohta:
#   - Kokku ülesandeid  
#   - Tehtud ülesandeid  
#   - Tegemata ülesandeid  

# Seon 'todo' ja 'user' 'userId' abil  
#kõigepealt muudame andmed tabeliks tuues üleval  sisse pandad
ulesanded = pd.DataFrame(tegevusalad_response.json())  # teeme jsoniks, muidu on alguses objekt e nagu mingi kogu app või lehekül, aga maham, et ta oleks nagu sõnaline tekst, et saaksime analüüsida 
kasutajad = pd.DataFrame(kasutajad_response.json())  # sulud tähendavad, et annad andmed, mite jsoni funsktisooni, mis teeb siis objektist teksti

merged = pd.merge(ulesanded, kasutajad, left_on='userId', right_on='id', how='left') #kuidas seonduvad, mis alusel, mis meetodiga
##print(merged)


# --- ÜL3: Arvuta kokkuvõte ---
summary = merged.groupby('name').agg( ## group by kataloogist võtad agg tähendab koonda, summeri ## group by thhed nagu andmehunniku nime järgi
    total_tasks=('id_x', 'count'),       # kokku kõik ülesanded ## id_x on sisse ehtitatud,
    done=('completed', 'sum')            # tehtud ülesanded (True = 1) total taski kolmis on väärtused kas tehtud või mitte, mina tahan ainult tehtud, sp liidan kõik tehtud väärtused
)
summary['not_done'] = summary['total_tasks'] - summary['done']

# --- ÜL4: Joonista stacked bar diagramm ---
plt.figure(figsize=(12, 6))
plt.bar(summary.index, summary['done'], label='Tehtud', color='green')
plt.bar(summary.index, summary['not_done'], bottom=summary['done'], label='Tegemata', color='red')

plt.title("Kasutajate Todo Ülesanded")
plt.ylabel("Ülesannete arv")
plt.xlabel("Kasutaja")
plt.xticks(rotation=45, ha='right')
plt.legend()  # Lisa legend (selgitus värvidele)
plt.tight_layout()  # Mahutab sildid paremini ära
plt.show()