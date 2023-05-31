def frecv_dict(nume):
    f = open(nume)

    dic = {}

    for s in f:
        print(s)
        for x in s:
            if x in dic:
                dic[x] = dic [x] +1
            else:
                dic[x] = 1

    # for x in dic:
    #     print(f"{repr(x)} apare de {dic[x]} ori")
    return dic
def cmp(x):
    if x.isalnum():
        return False, x
    else:
        return True, x

d1 = frecv_dict("caractere1.in")
print(d1)
d2 = frecv_dict("caractere2.in")
print (d2)

d =  d1.keys() & d2.keys()

for x in sorted(d, key=cmp):
    print(f"{repr(x)} apare de {d1[x] + d2[x]} ori")