def suma(n, f):
    s=0
    for i in range(1,n+1):
        s+=f(i)
    return s
#print(suma(10))
import math
print(suma(10,math.sqrt)) #se pot trimite param si prin poz si prin nume
def radical(x):
    return x**0.5
print(suma(10,f= radical))

# #b
# def suma_b(*numere, f):
#     s=0
#     for i in numere:
#         s+=f(i)
#     return s

# #print(suma_b(2,3,4,5))
# ls=[3,1,7]
# #print(suma_b(*ls))
# #print(suma(ls))
# from math import sqrt
# print(suma_b(4,9,16,f=sqrt))  #f obligatoriu sa fie apelat cu nume

# f=open("nume.txt")

# ls = []
# for linie in f:
#     #ls.append(int(x) for x in linie.split())
#     ls.extend(int(x) for x in linie.split())
# print(suma_b(*ls,f=sqrt))
# f.close()

def filtreaza(*numere, functie=None):
    if functie is None:
        return list(numere)
    ls=[]
    for nr in numere:
        if functie(nr):
            ls.append(nr)
    return ls
def pozitiv (x):
    return x>0
print (filtreaza(3,-1,6,8,-3,functie=pozitiv))

print(filtreaza("ana","are","10","mere", functie= str.isalpha))

print(filtreaza(3,-1,6,8,-3))