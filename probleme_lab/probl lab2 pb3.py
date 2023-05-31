# s = "1G10o4l"
# L=""
# nrcifre = 0
# for i in range (len(s)):
#     if s[i].isdigit():
#         nrcifre += 1
#     elif s[i].isalpha():
#         nr = int(s[i-nrcifre : i])
#         cuv = s[i]*nr
#         L += cuv
#         nrcifre = 0

# print(L)
# rezultat = "".join(L)
# print(rezultat)

#b
s2 = "Goooooooooollll"
rezultat2 = ""
oldcar= s2[0]
i=0

for car in s2:
    if car == oldcar:
        i += 1
    else:
        rezultat2 += str(i) + oldcar
        i = 1
        oldcar = car
rezultat2 += str(i) + oldcar

print (rezultat2)
