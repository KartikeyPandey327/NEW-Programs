import random

cups=["_"]*3

while True:
    cups=["_"]*3
    Start=input("Enter start to start and stop to end the game:")
    if Start!="stop":
        print(" ".join(cups))
        x=random.randint(0,len(cups)-1)
        choose=int(input("Enter the cup number which u choose(0,1,2): "))
        
        print(f"You have choosen {choose} number of cup")
        removed_cup=random.randint(0,len(cups)-1)
        while True:
            if removed_cup==choose:
                removed_cup=random.randint(0,len(cups)-1)
                continue

            elif  removed_cup==x:
                removed_cup=random.randint(0,len(cups)-1)
                continue

            else:
                break
        original_choose=choose
        print(f"If i remove the {removed_cup} cup, will you swap your answer")
        swap=input("enter y/n")
        if swap=="y":
             choose=random.randint(0,len(cups)-1)
             while True:
                 if choose==original_choose:
                     choose=random.randint(0,len(cups)-1)
                     continue

                 elif choose==removed_cup:
                     choose=random.randint(0,len(cups)-1)
                     continue

                 else:
                     break
             if choose==x:
                 print("won")
             else:
                 print("lost")

        else:
            if choose==x: 
                print("won")
            else:
                print("lost")
    else:
        break
                     
                     
            