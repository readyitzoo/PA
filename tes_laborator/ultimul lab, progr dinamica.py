# # ultimul lab, progr dinamica

# 1. Se dă o scară cu n trepte (n citit de la tastatură). Un om aflat la baza scării (pe treapta 0) poate într-un pas să sară cate 1, 2 sau 3 trepte. In cate moduri poate ajunge pe treapta n pornind de pe treapta 0?
# Exemplu: n=3 => 4 moduri (câte 1+1+1 sau 1+2 sau 2+1 sau 3 trepte sărite)
# v[ i ] = nr de moduri in care se poate ajunge pe treapta i
# Subprobleme stiute:
# v[0]=0, v[1] = 1, v[2]=2, v[3]=4
# Pt i>3:
# v[i] = v[i-1] + v[i-2] + v[i-3]

# n= 20
# [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415]

# rezolvare :

# n = int(input("n= "))

# v = [-1] * (n+1)
# print (v)
# v[0], v[1], v[2], v[3] = 0, 1, 2, 4

# for i in range(4, n+1):
#     v[i] = v[i-1] + v[i-2] + v[i-3]
# print(v)
# print(v[n])

# 2. Conjuctura lui Collatz. Se dă o funcție f : N -> N definită astfel:
# f(n) = n / 2, dacă n este par și
#       	3 * n + 1, dacă n este impar
# Pentru orice număr natural, dacă se aplică în mod repetat funcția f se ajunge la valoarea 1.
# Pentru un număr n dat, să se afișeze după câți pași se ajunge prima dată la valoarea 1.
# Exemplu: n=20 => 7 pași (20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
# Idee: Folosim dictionar cu 
# cheie = n, 
# valoare = dupa cati pasi se ajunge de la n la 1, folosind f(n)

# rezolvare:

# d = {1: 0}

# def f(d, n):
#     if n in d:
#         return d[n]
#     if n % 2 ==0:
#         d[n] = 1+ f(d, n//2)
#     else:
#         d[n] = 1 + f(d, 3*n + 1)
#     return d[n]

# n = int(input("n="))
# f(d, n)
# print(d)
# print(f"{d[n]} pasi")

# 3. Subsecvența de sumă maximă a unui șir: Se dă un șir de numere (în fișier, separate prin spații). Să se afișeze o subsecvenţă de sumă maximă a șirului (formată cu elemente consecutive)  
# date.in
# date.out
# v = 1 -2 3 -1 5 2 -6 1 3
# s = 1 -1 3  2 7 9  3 4 7  
# 3 -1 5 2 

# v = vectorul cu numerele primite la input 
# s[ i ] = suma maxima a unei secvente care se termina pe pozitia i
# Subprobleme deja stiute: 
# s[0] = v[0]
# Recurenta, pt 1 <= i < n
# s[i] = max {v[i], s[i-1] + v[i]}

# rezolvare: 

# f = open ("date.in")
# g = open ("date.out", "w")
# v = [int(x) for x in "1 -2 3 -1 5 2 -6 1 3".split()]


# s = [-1]*len(v)
# s[0] = v[0]

# for i in range(1, len(v)):
#     s[i] = max(v[i], s[i-1] + v[i])

# pozmax = s.index(max(s))
# print(f"subsecventa are suma: {s[pozmax]}")

# print(v)
# print(s)


# p=pozmax
# while s[p] != v[p] and p>=0:
#     print(v[p], end = " ")
#     p -= 1
# print(v[p])