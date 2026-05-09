import random

def player():
    p1=input("Enter the name of player 1:")
    p2=input("Enter the name of player 2:")
    return p1,p2
    


def choose():
    words=["tiger", "lion", "elephant", "zebra", "rabbit","red", "blue", "green", "yellow", "black"]
    word = random.choice(words)
    return word

def jumbled(word):
    letters = list(word)
    random.shuffle(letters)
    jumbled = "".join(letters)
    return jumbled


player1, player2 = player()
print(f"Player_1 is:{player1}")
print(f"Player_2 is:{player2}")

print("Let's start the game:")

score1=0
score2=0

while True:
    print("Enter 'stop' to end the game and 'start' to begin!!")
    start=input("Enter:")
    if start=="start":
        print(f"{player1} to guess")
        x=choose()
        print(jumbled(x))
        guess1=input("Enter your guess word:")
        if guess1==x:
            print("You got that!!!")
            score1=score1+1
        else:
            print("Do not give up!! The correct Word was:", x)

        print(f"{player2} to guess")
        y=choose()
        print(jumbled(y))
        guess2=input("Enter your guess word:")
        if guess2==y:
            print("You got that!!!")
            score2=score2+1
        else:
            print("Do not give up!! The correct Word was:", y)

        print(f"Score of {player1} is:",score1)
        print(f"Score of {player2} is:",score2)
        
            
    else:
        break