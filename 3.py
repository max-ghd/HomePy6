import random

numbers=int(input("Write one number: "))

a=[random.randint(1,100) for i in range(100)]

print(a)

count=a.count(numbers)

print(f"Число {numbers} було згенеровано {count} разa")