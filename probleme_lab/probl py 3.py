n= int (input("n="))

x = 0
sf = 1 << n
sf -= 1



while x <= sf:
    aux = x
    cnt = 1
    ok = 0
    print ("{", end = '')
    while aux:
        if aux & 1:
            if ok == 0:
                print (f"{cnt}", end = '')
            elif aux:
                print (f", {cnt}", end = '')
            ok = 1
        cnt += 1
        aux = aux >> 1
    print ("}")

    x += 1









