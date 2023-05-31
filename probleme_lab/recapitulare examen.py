# 1. a)
# def divizori(*numere):
#     d = {}
#     for numar in numere:
#         l = []
#         for i in range (2, numar+1):
#             if numar % i == 0:
#                 prim = 1
#                 for j in range (2, i//2 + 1):
#                     if i % j == 0:
#                         prim = 0
#                         break
#                 if prim == 1:
#                     l.append(i)
#         d[numar] = l
#     return d
# d = divizori(50,21, 16, 17, 3, 47)
# print(d)

# b) 
# litere_10 = [[chr(i + 97)] for i in range (10)]
# print(litere_10)

# c) in paint

# 2.

#   Ca sa programam cat mai mult spectacole intr-o zi, vom sorta in primul rand spectacolele dupa ora la care se termina. Apoi punem de fiecare data spectacolul care se termina cel mai repede, dar care nu se suprapune cu ultimul spectacol programat. Este un algoritm greedy deoarece alegem mereu spectacolul care pare cel mai bun la momentul alegerii si nu ne intoarcem in solutie sa schimbam ceva.
#	Presupunem solutia greedy S= {g1, g2, ... , gm} si solutia optima O= {o1, o2, ..., op}. Punem in evidenta prima diferenta intre S si O si inlocuim ok cu gk, deci acum ora la care se termina ultimul spectatacol este cel putin la fel de buna ca inainte. Ne intereseaza sa se termine cat mai repede pentru ca un spectacol care dureaza de 2 ori mai putin dar se termina cu 10 minute dupa cel ales de greedy se socoteste la fel, dar ne ocupa cu 10 minute mai mult si putem pierde o solutie.

# f = open ("spectacole.in")

# d = {}
# i = 0
# last = -1
# l = []
# for linie in f:
#     linie = linie.split()
#     d[i] =linie[0], linie[1]
#     i += 1
# d = (sorted(d.values(), key=lambda item: int(item[1])))
# print(d)
# for spectacol in d:
#     if int(spectacol[0]) >= last:
#         l.append(spectacol)
#         last = int(spectacol[1])
# print(l)
# print(len(l))

def back(k):
    if k==6:
        if x==sorted(x):
            bec=0
            bec1=0
            par=x[-1]%2
            for i in range(len(x)-1):
                if x[i+1]==x[i]+1:
                    bec+=1
                if x[i]%2!=par:
                    bec1+=1
            if bec==0 and bec1!=0:
                    print(*x)

    else:
        for i in range(1,n+1):
            x[k]=i
            if x[k] not in x[:k]: 
                back(k+1)

n=int(input())

x=[0 for i in range(6)]
back(0)