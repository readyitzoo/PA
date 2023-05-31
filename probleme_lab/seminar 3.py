s="aceasta este prima ora"
#inlocuim a->b e->f
tabel = str.maketrans("ae","bf") # sir 1 = caracterele pe care vrem sa le inlocuim
# sir 2 = caracterele coresp cu care inlocuim ; sir 1 si sir2 tb sa aiba aceeasi lungime
# se va inlocui sir1[i] -> sir2[i]
#se poate apela cu "".maketrans - nu are nev de un obiect pt a fi apelat => il putem apela cu tip.maketrans
print(tabel)
s=s.translate(tabel)
print(s)

