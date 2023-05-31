D = {}
fin = open("elevi.in")
for linie in fin:
    cnp, nume, prenume, note = linie.split(maxsplit = 3)
    D[int(cnp)] = [nume, prenume, [int(x) for x in note.split()]]
fin.close()
print(D)

cnp = 2501910000034
D[cnp][-1][0] += 1

print (D)