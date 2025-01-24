import random
a=[random.randint(0, 200) for i in range(200)]
print(a)
b=0
c=0
d=0
for i in a:
    if 0<= i <= 9:
        b +=1
    if 10<= i<=99:
        c +=1
    if 100<= i <=200:
        d +=1    

total=len(a)
print(total)

one=(b/total)*100
ten=(c/total)*100
hundred=(d/total)*100

print(f"Однозначиних чисел {b} і їх відсоток становить {one}%")
print(f"Двохзначних чисел{c} і їх відсоток становить {ten}%")
print(f"Трьохзначних чисел{d} і їх відсоток становить {hundred}%")