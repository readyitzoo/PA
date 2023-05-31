n, p = input().split()
n, p = int(n), int(p)
v = []
for i in range(n):
    v.append(tuple(int(x) for x in input().split()))
v.sort(key = lambda x: x[0], reverse=True)

s = []
for i in range(n):
    s.append(v[i][0])

print(v)

maxglb = s[0]

u = []

for i in range(1,n):
    maxim = s[i]
    ult = -1
    for j in range(i-1, -1, -1):
        if v[i][1] != v[j][1]:
            if  s[i] + s[j] > maxim:
                maxim =  s[i] + s[j]
                ult = j
    if maxim > maxglb:
        maxglb = maxim
    s[i] = maxim
    u.append(ult)

print(s)
print(u)
p = s.index(maxglb)

fin = []

for i in range(p, -1, -1):
    fin.append(v[u[i]])
for i in range(len(fin) -1, -1, -1):
    print(*fin[i])
print(s.count(maxglb))