# 1. a)

def citire_matrice(nume_fisier):
    f=open(nume_fisier)
    matr = []
    ok = 0
    cnt = 0
    cnt_last = 0
    for linie in f:     
        matr.append(linie.split())
        for x in linie.split():
            cnt += 1
        if ok:
            if cnt != cnt_last:
                return None
        ok = 1
        cnt_last = cnt
        cnt = 0
    return matr

# b

def multimi (matr, *indici):
    l1 = []
    l2 = []
    for linie in indici:
        for x in matr[linie]:
            x = int(x)
            if x < 0 and x not in l1:
                l1.append(x)
            else:
                inainte = x
                first = x % 10
                while x >= 10:
                    x = x // 10
                last = x
                if first == last and inainte not in l2: 
                    l2.append(inainte)
    return l1, l2


matr = citire_matrice ("test.txt")
# if matr != None:
#     for linie in matr:
#         for x in linie:
#             print(f"{x}".ljust(4), end =" ",)
#         print ()

# c

n = 0
for linie in matr:
    n += 1

l1, l2 = multimi(matr, n-3, n-2, n-1)
for i in l2:
    print(i, end = " ")
print()

l1, l2 = multimi (matr, 0)
l2, l3 = multimi (matr, n-1)
cnt = 0
for x in l1:
    if x in l2:
        cnt += 1

print(cnt)

# 2. a

def modifica_prefix(x, y, prop):
    for cuvant in prop:
        ok = 1
        i = 0
        for litera in x:
            if litera != prop[i]:
                ok = 0
            i += 1
            if ok:
                
