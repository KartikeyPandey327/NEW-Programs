import random

x=int(input("Enter the number of die you want to roll:"))
y=int(input("Enter the side each of your cube has:"))

while True:
    z=0
    start=input("Enter to 'roll' to roll the die!")
    if start=="roll":
        while z<x:
            print(random.randint(1,y))
            
            z=z+1

    else:
        break