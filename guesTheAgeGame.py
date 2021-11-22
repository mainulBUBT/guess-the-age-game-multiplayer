import random as r
count = 0
count_2 = 0

def myfunc(a, b):
    random_age = r.randint(1, 10)

    if b == 1:
        if a == random_age:
            flag = True
            return flag
    else:
        if a == random_age:
            flag = True
            return flag

print("Guess the age P1 and P2 for Two times try. age between 1-10")
for i in range(2):
    for j in range(2):
        if j % 2 == 0:
            inputs = int(input("P1: "))
            man = myfunc(inputs, 1)
            if man == True:
                count+=1
        else:
            inputs = int(input("P2: "))
            man = myfunc(inputs, 2)
            if man == True:
                count += 1

print("Player 1 "+str(count)+" correct answer")
print("Player 2: "+str(count_2)+" correct answre")
