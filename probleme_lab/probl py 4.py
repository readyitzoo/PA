x = int (input("x="))
k = int (input("k="))

print (bin(x))
print (bin(k))

bit = ~(1 << (k-1))
print (bin(bit))

x = x >> k
x = x << k-1
x -= bit

print (f"{x} este numarul fara al k-lea bit")