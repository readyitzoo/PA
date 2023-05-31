def dreptunghiuri(D, C):
    # D = [(x_stanga, y_jos), (x_dreapta, y_sus)]
    # D = dreptunghiul curent (lista de 2 tupluri, colt stanga-jos si dreapta-sus)
    # C = lista copaci (tupluri (x,y))
    
    arie_max = 0
    D_max = None
    faraCopaci = True
    for copac in C:
        if D[0][0] < copac[0] < D[1][0] and D[0][1] < copac[1] < D[1][1]:
            
            # dreptungiuri jos / sus fata de copac
            arie1, D1 = dreptunghiuri([D[0], (D[1][0], copac[1])], C)
            arie2, D2 = dreptunghiuri([(D[0][0], copac[1]), D[1]], C)

            # dreptungiuri stanga / dreapta fata de copac
            arie3, D3 = dreptunghiuri([D[0], (copac[0], D[1][1])], C)
            arie4, D4 = dreptunghiuri([(copac[0], D[0][1]), D[1]], C)

            (arie_max, D_max) = max([(arie_max, D_max), (arie1, D1), (arie2, D2), (arie3, D3), (arie4, D4)])
            
            faraCopaci = False

    if faraCopaci == True:
        arie_max = (D[1][0] - D[0][0]) * (D[1][1] - D[0][1])
        D_max = D    

    return arie_max, D_max


f = open("copaci.in")

s = f.readlines()
f.close()
print(s)

padure = [tuple([int(nr) for nr in x.strip().split()]) for x in s[:2]]
print(padure)
copaci = [tuple([int(nr) for nr in x.strip().split()]) for x in s[2:]]
print(copaci)

arie_max, D_max = dreptunghiuri(padure, copaci)
print(arie_max, D_max)
