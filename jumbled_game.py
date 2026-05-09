import random

# This is a simple jumbled word game where two players can play against each other. The players will be prompted to enter their names, and then they will take turns guessing the jumbled words. The game continues until the players decide to stop it. The scores of both players are displayed after each round.

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

# Main program
# The main program starts by calling the player function to get the names of the two players. Then, it enters a loop where it prompts the players to start the game. If the players choose to start, it randomly selects a word for each player, jumbles it, and asks them to guess the original word. The scores are updated based on whether the guesses are correct or not. The game continues until the players decide to stop it.  

player1, player2 = player()
print(f"Player_1 is:{player1}")
print(f"Player_2 is:{player2}")

print("Let's start the game:")

score1=0
score2=0

# The game loop continues until the players decide to stop it. Inside the loop, it prompts the players to start the game. If they choose to start, it randomly selects a word for each player, jumbles it, and asks them to guess the original word. The scores are updated based on whether the guesses are correct or not. After each round, the scores of both players are displayed.
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
        # After each round, the scores of both players are displayed.
        print(f"Score of {player1} is:",score1)
        print(f"Score of {player2} is:",score2)
        
    # If the players choose to stop the game, the loop breaks and the final scores are displayed.        
    else:
        break