# f = open("date.in")
# g = open("date.out", "w")
# n = int(f.readline())
# v = []
# d = []
# for h in f.readline().split():
#     h = int(h)
#     v.append(h)
#     if len(v) > 1:
#         panta = v[-1] - v[-2]
#         d.append(panta)
#     else:
#         d.append(0) 
# print(d)
# vf = -1
# def divide (i, j):
#     print (i, j)
#     if j - i > 1:
#         if d[(i+j)//2] > 0:
#             vf = divide ((i + j) // 2 , j)
#         else:
#             vf = divide(i, (i + j) // 2 -1)
#     else:
#         vf = max(v[i], v[j])
#     return vf
# vf = divide(0, n-1)
# g.write(str(vf))


# functia divide primeste ca parametrii indicii corespunzatori capetelor vectorului
# din fisierul date.in. Algoritmul foloseste metoda DI deoarece functia sparge vectorul
# in parti egale pana ajunge la 2 numere pe care le poate compara si va returna
# maximul din vector la final, adica varful muntelui

# pbinfo ExistaImpareDivImp


n , m= (input().split())
n, m = int(n), int(m)
matr = []
for i in range(n):
    linie = list(map(int, input().split()))
    matr.append(linie)

def divide (i, st, dr):
    if dr - st >= 1:
        return divide(i, st, (st+dr)//2) + divide (i, (st+dr)//2 +1, dr)
    else:
        if matr[i][st] % 2 == 0:
            return matr[i][st]
        else: 
            return 0

s = 0
for i in range(n):
    s += divide(i, 0, m-1)

print(s)

# v = [int(x) for x in input().split()]
# def divide (st, dr):
#     if dr - st >= 1:
#         return divide(st, (st+dr)//2) + divide ((st+dr)//2 +1, dr)
#     else:
#         if v[st] % 2 != 0:
#             return 1
#     return 0
# ok = divide(0, n-1)
# if ok == 0:
#     print("NU")
# else:
#     print("DA")