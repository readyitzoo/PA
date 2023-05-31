# Dilirici Mihai, grupa 143


def citire_matrice(nume_fisier):
    f = open(nume_fisier)
    m = [[]]
    for linie in f:
        for coloana in linie:
            m[linie][coloana] = coloana
    return m
m = citire_matrice("date.in")
print(m)