import random

numbers =[random.randint(1,42) for i in range(5)]
ask1=int(input("Напиши 1 число от 1 до 42, чтобы выиграть в лоторею: "))
ask2=int(input("Напиши 2 число от 1 до 42, чтобы выиграть в лоторею: "))
ask3=int(input("Напиши 3 число от 1 до 42, чтобы выиграть в лоторею: "))
ask4=int(input("Напиши 4 число от 1 до 42, чтобы выиграть в лоторею: "))
ask5=int(input("Напиши 5 число от 1 до 42, чтобы выиграть в лоторею: "))
total=[]
total.append(ask1)
total.append(ask2)
total.append(ask3)
total.append(ask4)
total.append(ask5)
print(total)
a = 0
for i in total:
    if i in numbers:
        a +=1

if a == 3:
    prize=100
elif a ==4:
    prize= 500
elif a ==5:
    prize = 2500
else:
    prize = 0

print(f"Numbers in lottery: {numbers}")
print(f"Your correct answer {a} numbers. Your prize {prize} grn ")