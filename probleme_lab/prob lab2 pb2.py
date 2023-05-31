s="abccabcababcc"
t="abc"
poz = s.find(t)
while (poz!=-1):
    print (poz, end=' ')
    poz = s.find(t, poz + len(t))

print()

poz = -len(t)
while True:
    try:
        poz = s.index(t, poz + len(t))
        print (poz, end =" ")
    except:
        print("gata")
        break

print()

poz = -len(t)
try:
    while True:
        poz = s.index(t, poz + len(t))
        print (poz, end =" ")
except:
    print("gata")
