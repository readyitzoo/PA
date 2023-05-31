# verificati daca 2 fisiere sunt anagrame ( au aceleasi caractere
# in afara de caracterele de endl)

# def citire_fisier(nume_fisier):
#     f=open(nume_fisier)
#     d= {}
#     for linie in f:
#         for caracter in linie.rstrip('\n'):
#             d[caracter] = d.get(caracter, 0) + 1
#     f.close
#     return d

# d1 = citire_fisier("fisier1.in")
# d2 = citire_fisier("fisier2.in")
# print (d1)
# print (d2)
# print(d1 == d2)

# Se dau 2 fisiere, afisati intr un al 3-lea fisier acele linii "i" din primul
# fisier care sunt anagrame ale liniei "i" coresp. din cel de-al 2-lea fis.

def prelucrare_linie(linie):
    d={}
    for caracter in linie.rstrip('\n'):
        d[caracter]=d.get(caracter, 0) + 1
    return d

g= open ("fisier3.out", "w")
f1 = open("fisier1.in")
f2 = open("fisier2.in")
linie1 = f1.readline()
linie2 = f2.readline()

while linie1 != "" and linie2 != "":
    if prelucrare_linie(linie1) == prelucrare_linie(linie2):
        g.write(linie1)
    linie1 = f1.readline()
    linie2 = f2.readline()

f1.close()
f2.close()
g.close()