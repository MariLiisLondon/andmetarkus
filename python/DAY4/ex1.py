
# regex
import  re

string = "Minu kontonumber on 345678, aga vana konto oli 312345. Mõned näited, mida ei tohiks leida: 234567, 34567, 33445566, 39876, 399999, 3123457, 31234. Samuti on olemas 398765 ja 300001."

matches = re.findall(r'\b3\d{5}\b', string)  
print(matches)  # Otsib kõiki 6-kohalisi numbreid, mis algavad 3-ga ja prindib need välja
# \b tähistab sõna piiri, [0-9]{5} tähendab täpselt 5 numbrit vahemikus 0-9    

text2 = """See on esimene rida.
See on teine rida.
Kolmas rida on siin.
Neljandal real on samuti tekst."""


pattern2 = r'\n'  # Otsib reavahetusi
text2_ilma_reavahetusteta = re.sub(pattern2, ' ', text2)
print(text2_ilma_reavahetusteta)  # Asendab reavahetused


