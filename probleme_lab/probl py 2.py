n = int(input("n="))

max1 = None
max2 = None

while n > 0:
    x =int (input ("x="))
    if max1 is None or x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and (max2 == None or x > max2):
        max2 = x
    n = n-1

if max2 == None:
    print ("Imposibil")
else:
    print (f"cele doua maxime diferite sunt {max1}, urmat de {max2}")

x=1000
y=x
print (id(x), id(y), sep="\n")