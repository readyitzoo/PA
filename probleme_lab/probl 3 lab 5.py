fin = open("cuburi.txt")
fout = open ("turn.txt", "w")
def reint (x):
    return int(x.split()[0])

ls = []
n = int(fin.readline())
for linie in range(1,n+1):
    s = fin.readline()
    ls.append(s)
ls = sorted (ls, key = reint, reverse=True)

culoare = ""
h = 0
for cub in ls:
    if cub.split()[1] != culoare or culoare == "":
        h += int(cub.split()[0])
        culoare = cub.split()[1]
        fout.write(cub)
fout.write(f"Inaltime totala: {h}")
fin.close()
fout.close()