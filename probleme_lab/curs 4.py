#LISTE

ls = [2, 4, 5]
ls = [1, "ab"]  #pot fi neomogene - cu el de tipuri dif
ls = [[1,2], [3,4]]

#cu ajutorul metodei list(iterabil)
ls = list("abc")
print (ls) # lista de litere

#lista vida
ls = []
ls = list()

#secvente de initializare (list comprehension)

#[expresie for x in iterabil]
ls = [0 for i in range(10)]
"""
ls = []
for i in range(10):
    ls + = [0]
    ls.append(0)
"""
print(ls)

#2. lista primelor 10 patrate perfecte
ls = [i*i for i in range(10)]
print(ls)

#3. citirea unui vector de nr intregi
ls1 = input("dati vectorul ").split()
print (ls1)
ls1 = [int(x) for x in ls1]
print (ls1)

#citirea condensata
ls = [int(x) for x in input("dati vectorul").split()]
print (ls)

#comprehensiune conditionata - cu if dupa for
#[expresie for x in iterabil if conditie]

#1. filtrarea el. unei liste dupa un criteriu - exp: elem. poz. 

ls = [3, -21, 7, -10, 7]
ls_poz= [x for x in ls if x>0]
print (ls_poz)
#afisarea el. poz. citite de pe o linie:
ls = [int(x for x in input("dati vectorul").split() if int(x)>0)]
print (f"lista nr poz intriduse {ls}")

#intersectia a doua liste
ls1 = [3, 5, 1, 8, 10]
ls2 = [7, 10, 20, 1]
ls_intersectie = [x for x in ls1 if x in ls2]
print (ls_intersectie)

#actualizarea listei:

ls [3:6] = [0,0,0,0,0] #va creste lista, nu trb sa aiba aceeasi lungime
ls [1:6:2] = [-1, -2, -3] #aceeasi lungime