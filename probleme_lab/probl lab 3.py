# a
# ls = [chr(i) for i in range(ord("a"), ord("z") + 1)]
# print (ls)

# b
# n =int(input("n="))
# ls = [(i if i % 2 != 0 else -i) for in i range]



# c
# ls = [int (x) for x in input("lista numere=").split()]
# new_ls = [x for x in ls if x % 2 != 0]
# print (ls)
# print (new_ls)

# d
# l1= [ls[i] for i in range(len(ls)) if i % 2 != 0]
# print (l1)



# e
# ls = [2,4,1,7,5,1,8,10]
# l1 = [ls[i] for i in range (len(ls)) if ls[i] % 2 == i % 2]
# print (l1)

# f
# l2 = [(ls[i], ls[i+1]) for i in range(len(ls)-1)]
# print (l2)

# g
# def tabla_inmultirii(n):
#     matr = [[f"{x} * {y} = {x*y}"for y in range (1, n+1)] for x in range (1, n+1)]
#     return matr

# def afisare(matr):
#    l_max =  max([max([len(str(x)) for x in linie ]) for linie in matr])
#    for linie in matr:
#         for x in linie:
#            print (f"{x}".rjust(l_max), end = "\t")
#         print()


# def matr_to_str(matr):
#     sir = "\n".join(["\t".join(linie) for linie in matr])
#     return sir

# n = int(input ("n="))
# M = tabla_inmultirii(n)
# # afisare(M)

# print (matr_to_str(M))

# # h
# sir = input ("s=")

# ls = [sir[i:]+sir[:i] for i in range(len(sir)) ]
# print (ls)

# #i
# def lista(n):
#     ls = [[i for j in range (i)] for i in range (n)]
#     return ls

# ls = lista(int(input("n=")))
# print (ls)

#have a nice day

# sortari
ls = [44, 221, 3, 123333, 71471, 0, 2711, 98, 334]
# ls.sort(reverse = True)
print (ls)

# ls1 = sorted(ls)
# print (ls1)

# #1
# def crit(x):
#     return str(x)

# # ls2 = sorted (ls, key = crit)
# # print (ls2)

# ls2 = sorted (ls, key = lambda  x : str(x))
# print (ls2)

#b
ls3 = sorted (ls, key = lambda  x : str(x)[::-1])
print (ls3)

#c
ls4 = sorted (ls, key = lambda  x : len(str(x)) )
print (ls4)

#d
ls5 = sorted (ls, key = lambda  x : len(set(str(x))) )
print (ls5)

#e

ls6 = sorted (ls, key = lambda  x : (len(set(str(x)), x)) )
print (ls6)

def criteriu(x):
    return len(str(x)), x
ls7 = sorted (ls, key = criteriu)
print (ls7)