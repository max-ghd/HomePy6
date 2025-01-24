import random

a=[random.randint(1,20) for i in range(20)]
couple=[]
for i in range(len(a)):
    if i % 2 == 0:
        couple.append(a[i])

print(couple)
