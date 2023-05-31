
f = open("input.txt", "r")
w = f.readline()
print(w)
# for linie in f:
#     for cuvant in linie.split():
#         for i in range(len(w)):
#             if cuvant.startswith(w[:i]):
#                 print(cuvant, end = "\n")
#                 break

cuvant = "masat"
if cuvant.startswith(w):
    print(cuvant)
f.close()