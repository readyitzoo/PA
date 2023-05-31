#citim linie cu linie si fiecare linio o memoram ca set+ intersectie
f = open("numere_comune.in")
rez=set([int(x) for x in f.readline().split()]) 
for linie in f:
    m = set([int(x) for x in linie.split()]) 
    rez &= m
    #rez.intersection_update(m)
print(sorted(rez))
f.close()