# ls = [chr(i) for i in range(ord("a"), ord("z") + 1)]
# print (ls)

# n =int(input("n="))
# ls = [(i if i % 2 != 0 else -i) for in i range]


ls = [int (x) for x in input("lista numere=").split()]
new_ls = [x for x in ls if x % 2 != 0]
print (ls)
print (new_ls)

l1= [ls[i] for i in range(len(ls)) if i % 2 != 0]
print (l1)