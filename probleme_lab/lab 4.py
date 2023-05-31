# # seminar 4 probl 5
# # a
# n,m =[int(x) for x in input("n,m=").split()]

# import random

# with open("matrice.in","w") as f:
#     for i in range(n):
#         for j in range(m):
#             f.write(str(random.randint(0,100)) + " ")
#         f.write("\n")
        
# # b
# with open("matrice.in") as f:
#     a=[[int(nr) for nr in linie.split()] for linie in f]
#     print(*a, sep="\n", end = "\n\n")

# T = [[a[lin][col] for lin in range(n)] for col in range(m)]
# print(*T, sep="\n", end = "\n\n")

# M = sorted(a, key = lambda linie : linie[-1])
# print(*M, sep="\n")

#lab 4.pdf
#a
def create_dic(*args):
    D={}
    for nume in args:
        f=open(nume)
        for linie in f:
            for cuv in linie.split():
                # if cuv in D:
                #     D[cuv] += 1
                # else:
                #     D[cuv] = 1
                D[cuv] = D.get(cuv, 0) +1
        f.close()
    return D

#b
d = create_dic("cuvinte1.in", "cuvinte2.in")
print(d)
print(sorted(d.keys()))

#c
d1 = create_dic("cuvinte1.in")
print(sorted(d1.items(), key= lambda t: -t[1])) # - pentru sortare invers, echivalent cu reverse= true

#d
d2 = create_dic("cuvinte2.in")
print(d2)
print(min(d2.items(), key = lambda t : (-t[1], t[0]))[0])

#e

s = 0
s1 = 0
s2 = 0
for cuv in d1.keys() | d2.keys():
    s += d1.get(cuv, 0) * d2.get(cuv, 0)
    s1 += d1.get(cuv, 0) ** 2
    s2 += d2.get(cuv, 0) ** 2

rez = s / (s1 ** 0.5 * s2 ** 0.5)

print (f"{rez:.2}")



