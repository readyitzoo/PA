p = int(input())
div = []
for i in range(1, p // 2 + 1):
    if p % i == 0:
        div.append(i)

print(div)
cont = 0
l = []

def teava(s, start):
    if s > p:
        return
    if s == p:
        print(*l, sep = "+")
        cont += 1

    else:
        for d in div[start:]:
            l.append(d)
            teava(s + d, div.index(d))
            l.pop()

teava(0, 0)
print(c)
               

