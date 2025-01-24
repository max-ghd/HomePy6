import random
m = [random.randint(1, 10) for i in range(10)]
n = [random.randint(0, 20) for i in range(20) ]
print(m)
print(n)
couple= list(set(m) & set(n))

print(couple)






