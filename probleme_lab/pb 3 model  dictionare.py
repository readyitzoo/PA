f = open ("autori.in")
m, n = f.readline().split()
m, n = int(m), int(n)
d = {"autori": {}, "carti": {}}

import json

for i in range (m):
    linie = f.readline().split()
    cod_autor = linie[0]
    nume_autor= linie[1] + " " + linie[2] 
    d["autori"][cod_autor] = {"nume": nume_autor, "carti": {}}


for i in range (n):
    linie = f.readline().split(maxsplit=4)
    cod_autor = linie[0]
    cod_carte = linie[1]
    an_aparitie = int(linie[2])
    nr_pagini = int(linie[3])
    titlu = linie[4]
    d["autori"][cod_autor]["carti"][cod_carte] = {"an": an_aparitie, "pag": nr_pagini, "titlu": titlu.strip()}
    d["carti"][cod_carte] = cod_autor
    
print(json.dumps(d, indent=2, sort_keys=True))

def sterge_carte(d, cod_carte):
    if cod_carte not in d["carti"]:
        return None
    cod_autor = d["carti"][cod_carte]
    del d["autori"][cod_autor]["carti"][cod_carte] 
    del d["carti"][cod_carte]
    return d["autori"][cod_autor]["nume"]

# cod_carte = input()
# nume_autor = sterge_carte(d, cod_carte)
# if nume_autor:
#     print(f"Cartea a fost scrisa de {nume_autor}")
#     print(json.dumps(d, indent=2, sort_keys=True))
# else:
#     print ("Cartea nu exista")
#print(json.dumps(d, indent=2, sort_keys=True))

def carti_autor (d, cod_autor):
    l = []
    if cod_autor not in d["autori"]:
        return None, l
    for carte in d["autori"][cod_autor]["carti"].values():
        l.append((carte["titlu"], carte["an"], carte["pag"]))
    return d["autori"][cod_autor]["nume"], l

nume, ls = carti_autor(d, "11")
if nume:
    print(nume)
    for carte in ls:
        print(*carte)
else:
    print("cod incorect")
    
