

#citire

def litere(*cuvinte):
    d = {}
    for cuv in cuvinte:
        d[cuv] = {}
        for litera in cuv:
            if litera in d[cuv]:
                d[cuv][litera] += 1
            else:
                d[cuv][litera] = 1
    return d

print (litere("teste", "dictionar", "ele"))

d = litere("teste")
print(d["teste"])
d= d["teste"]
float(n)
l = [(litera, d[litera]) for litera in d.keys() if d[litera] % 2 == 0]
l.sort(key = lambda x: x[0])
print(l)
l.append((l, a))
abs(l)