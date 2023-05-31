# Dilirici Mihai, grupa 143
# Să se scrie în fișierul text 𝑡𝑒𝑥𝑡. 𝑜𝑢𝑡 toate cuvintele din fișierul
# 𝑡𝑒𝑥𝑡. 𝑖𝑛 care au mulțimea literelor inclusă în mulțimea literelor cuvântului 𝑤 sau mesajul
# "𝐼𝑚𝑝𝑜𝑠𝑖𝑏𝑖𝑙" dacă în fișierul de intrare nu există nici un cuvânt cu proprietatea cerută,


f = open ("text.in")
g = open ("text.out", "w")

w = f.readline()
grupuri = []
lista = []
for linie in f:
    linie = linie.split()
    for cuvant in linie:
        ok = 1
        before = cuvant
        # print(cuvant)
        for i in range(len(cuvant)):
            if cuvant[i].lower() not in w and cuvant[i] != "-":
                ok = 0

        if ok == 1 and cuvant not in lista:
            lista.append(cuvant)
                     
k = 0
for cuvant1 in lista:
    l = [cuvant1]
    ok = 0
    for cuvant2 in lista:
        if cuvant1 != cuvant2:
            ok = 1
            for litera in cuvant1:
                litera = litera.lower()
                if litera not in cuvant2 and litera != "-":
                    ok = 0
            for litera in cuvant2:
                litera = litera.lower()
                if litera not in cuvant1 and litera != "-":
                    ok = 0
        if ok == 1 and cuvant2 not in l:
            l.append(cuvant2)
    l= sorted(l)
    # l1 = []
    # if l not in grupuri:
    #     cuvant = [l[0]]
    #     for litera in cuvant:
    #         if litera not in l1 and litera != "-":
    #             l1.append(litera)
    # grupuri.append(l1)
    if l not in grupuri:
      grupuri.append(l)
lmare = []
for grup in grupuri:
    l1=[]
    for litera in grup[0]:
        litera = litera.lower()
        if litera not in l1 and litera != "-":
            l1.append(litera)
    l1 = sorted(l1)
    lmare.append(l1)
grupuri = sorted(grupuri)

k = 0
lmare = sorted(lmare)
for seturi in lmare:
    g.write (f"Literele {seturi}")
    for cuvant in grupuri:
        ok = 1
        # print(cuvant)
        # print(seturi)
        for litera in cuvant:
            if litera not in seturi:
                ok = 0
    if ok == 1:
        for cuvant in grupuri[k]:
            g.write(cuvant)
        print (grupuri[k])
    k += 1

print(grupuri)