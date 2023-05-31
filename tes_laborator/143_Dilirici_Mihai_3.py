# Dilirici Mihai, grupa 143

d = {"nume": {}, "note": {}}



def citire(nume_fisier):
    f = open(nume_fisier)
    n, m = f.readline().split()
    n, m = int(n), int(m)
    for i in range (n):
        linie = f.readline()
        d["nume"] = linie
        for j in range(m):
            note = f.readline()
            d["nume"][linie]["note"][j] = note
        return d


def despre_elev (d, numele_elevului):
    if numele_elevului not in d["nume"]:
        print("elevul nu exista")
    else:
        nume_materie = d["nume"][numele_elevului]["note"][0]
        note = d["nume"][numele_elevului]["note"][1]
        s = 0
        k= 0
        for nota in note:
            s += nota
            k += 1
        s = s/k
        round(s, 2)
        return (nume_materie, s)

def adauga_nota(numele_elevului, materia, *note):
     pass


    

d = citire("note.in")
nume = input("nume= ")
for medii in d["nume"][nume]["note"]:
    a, b = despre_elev(d, nume)
    print(a, b)

print(d)
