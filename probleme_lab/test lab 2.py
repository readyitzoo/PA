def deviruseaza(propozitie):
    ls = propozitie.split()
    prop_corect = []
    for cuvant in ls:
        l = len(cuvant)
        corect = cuvant[-1] + cuvant[1:l-1] + cuvant[:1]
        prop_corect.append(corect)
    prop_corect.reverse()
    print(*prop_corect)


def prime(n, numar_maxim = 0):
    nrprime = []
    if n > 2:
        nrprime.append(2)
    for i in range (3, n, 2):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
        else:
            nrprime.append(i)
    if numar_maxim == 0:
        return nrprime
    else:
        return nrprime[:numar_maxim]

nrprime = prime(13)
print(nrprime)
deviruseaza("aorectc aropozitip este aceasta")

f = open("intrate.in")
