# n, a, p = input().split()
# n, a, p = int(n), int(a), int(p)
# intr = list(map(int, input().split()))

# def bkt(r, a, i):
#     if a == 0:
#         if r == 0:
#             print(sorted(l))             
#     elif r < 0 or i >= len(intr):   
#         return
#     else: 
#         l.append(i + 1)
#         bkt(r - intr[i], a - 1, i + 1)
#         l.pop()
#         bkt(r, a, i + 1)
        
# l = []
# bkt(p, a, 0)

# n = int(input("n="))
# ciur = [0] * 2 + [1] * (n-1)
# prime = []

# for i in range (2, n+1):
#     if ciur[i] == 1:
#         prime.append(i)
#         for j in range(i*2, n+1, i):
#             ciur[j] = 0
# print(prime)

# def bkt(s, l, i):
#     if s > n or i >= len(prime):
#         return -1
#     elif s == n:
#         print(*l, sep = "+")
#         return -1
#     else:
#         if bkt(s + prime[i], [*l, prime[i]], i) == -1:
#             return
#         if bkt(s, l , i + 1) == -1:
#             return
        
# bkt(0, [], 0)


# m = []
# m = [[int(x) for x in linie.split()] for linie in f]
# n = len(m)
# l = []

# def produs (i):
#     if len(l) == n:
#         print(*l)
#     else:
#         for el in m[i]:
#             l.append(el)
#             produs(i+1)
#             l.pop()

# produs(0)


# S, n, M= input().split()
# S, n, M = int(S), int(n), int(M)
# v = [int(x) for x in input().split()]
# nr = [int(x) for x in input().split()]
# print(S, n, v)
# l = [0] * n

# def monede(s, jmin, c):
#     if c > M or s > S:
#         return
#     if s == S:
#         print(*l, sep = ", ")
#     else:
#         for i in range(jmin, n):
#             if l[i] >= nr[i]:
#                 continue
#             l[i] += 1 
#             monede (s + v[i], i, c + 1)
#             l[i] -= 1

# monede(0, 0, 0)



n = int(input("n="))
l = []
def bkt(i, k):
    if k == n:
        print(*l)
        k -= 1
    else:
        for i in range(1,n+1):
            if i not in l:
                l.append(i)
                bkt(i, k+1)
                l.pop()

bkt(n, 0)

lista_cuvinte = ["acasa", "masa", "este", "scaun"]
lista_rez = [cuv for cuv in lista_cuvinte if cuv[0] == cuv[-1]]
print(lista_rez)
