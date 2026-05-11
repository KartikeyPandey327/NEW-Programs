import random
import string


symbols=[]
symbols=list(string.ascii_letters)
same=random.choice(symbols)

def shuffle(x):
       
    x=[0]*5
    while True:
           
        index=random.randint(0,len(x)-1)
        if x[index]==0:
              
            x[index]=random.choice(symbols)

        else:
                
           
            if (x[0]!=0 and x[1]!=0 and x[2]!=0 and x[3]!=0 and x[4]!=0 and x[0]!=x[1]!=x[2]!=x[3]!=x[4]!=same):
                x[random.randint(0,len(x)-1)]=same
                print(x)
                 
                break
            else:
                      
                continue
            
        

print("Welcome to Dobble game, \nLets get started")

i=1
j=100

while True:

    shuffle(i)
    shuffle(j)
    
    
    print("\nEnter stop to end the game")
    user_input=input("Enter the reapted word")
    if user_input==same:
        print("Correct!!!\n")
        i += 1
        j += 1
        same=random.choice(symbols)

    elif user_input=="stop":
        print("Game Over!!!\n")
        break
    else:
        print("Enter the correct value!\n")
