f = open ("matrice.txt")
n, m = [int(x) for x in f.readline().split()]
matr = [[int(x) for x in linie.split()] for linie in f]
print(matr)
s = [[0 for i in range(m)] for j in range (n)]
print(s)

# suma maxima pornind de la (i.j)

for i in range(n-1,-1, -1):
    for j in range (m-1, -1, -1):
        if i == n-1 and j == m-1:
            s[i][j] = matr[i][j]
        elif i == n-1:
            s[i][j] = matr[i][j] + matr[i][j+1]
        elif j == m-1:
            s[i][j] = matr[i][j] + matr[i+1][j]
        else:
            s[i][j] = matr[i][j] + max(s[i+1][j], s[i][j+1])
print(s[0][0])
print(s)

i = j = 0
while i < n and j < m:
        print(i+1, j+1)
        if i == n-1 and j == m-1:
            i += 1
            j += 1
        elif i == n-1:
            j += 1
        elif j == m-1:
            i += 1
        else:
            if s[i+1][j] > s[i][j+1]:
                i += 1
            else:
                j += 1
            