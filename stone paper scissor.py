import getpass

game=["stone","paper","scissor"]


def stone_paper_scissor():
    
    p1=getpass.getpass("Player 1 Enter stone paper or scissor")
    while True:
        if p1 not in game:
            p1=getpass.getpass("Player 1 Enter stone paper or scissor again correctly: ")
        else:
            break
    p2=getpass.getpass("Player 2 Enter stone paper or scissor")
    while True:
        if p2 not in game:
            p2=getpass.getpass("Player 2 Enter stone paper or scissor again correctly: ")
        else:
            break

    if p1 == "stone" and p2 == "scissor":
        print("won by player 1")
    elif p1 == "stone" and  p2 == "paper":
        print("won by player 2")   
    elif p1 == "stone" and  p2 == "stone":
        print("draw")

    elif p1 == "paper" and  p2 == "stone":
        print("won by player 2")
    elif p1 == "paper" and  p2 == "scissor":
        print("won by player 2")   
    elif p1 == "paper" and  p2 == "paper":
        print("draw")

    elif p1 == "scissor" and  p2 == "paper":
        print("won by player 1")
    elif p1 == "scissor" and  p2 == "stone":
        print("won by player 2")   
    else :
        print("draw")

while True:
    start=input("enter start to start the game and stop to end the game:")
    if start!="stop":
        stone_paper_scissor()

    else:
        break
        
