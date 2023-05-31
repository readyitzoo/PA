import random
import string

def gen_parola():
    p = random.choice(string.ascii_uppercase)
    p1 = "".join(random.choices(string.ascii_lowercase, k=3))
    p2 = "".join(random.choices(string.digits, k=4))

    return p + p1 + p2

f = open("date.in")
g = open("date.out", "w")

for linie in f:
    nume, prenume = linie.split()
    g.write(f"{prenume.lower()}.{nume.lower()}@s.unibuc.ro, {gen_parola()}\n")