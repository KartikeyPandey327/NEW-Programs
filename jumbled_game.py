# Jumbled Game
player_1=input("Player 1, enter your name: ")
player_2=input("Player 2, enter your name: ")
print(" \n Welcome to the Jumbled Game, " + player_1 + " and " + player_2 + "!")
print(" \n You will give jumbled words to each other and the other player has to guess the correct word.")
print(" \n Let's start the game! ")
import random
rounds=int(input("Enter the number of rounds to be played:"))
print(player_1,"to guess\n")
x=0
score_1=0
while x<rounds:
    user_input=input("\nEnter the name to guess:")
    jumbled_list = random.sample(user_input, len(user_input)) # random.sample() is used to shuffle the characters of the input word
    result = "".join(jumbled_list)# join() is used to convert the list of characters back into a string after shuffling
    print(result)
    guess=input("Enter your guess")
    if guess==user_input:
        print("You got it\n")
        score_1=score_1+10
    else:
        print("ohh!! the correct guess was!!\n", user_input)

    x=x+1

print(player_2,"to guess\n")    
y=0
score_2=0
while y<rounds:
    user_input=input("Enter the name to guess:")
    jumbled_list = random.sample(user_input, len(user_input))
    result = "".join(jumbled_list)
    print(result)
    guess=input("\nEnter your guess")
    if guess==user_input:
        print("You got it\n")
        score_2=score_2+10
    else:
        print("ohh!! the correct guess was!!\n", user_input)

    y=y+1     
# Final Scores
print(f"score of {player_1} is ", score_1)
print(f"\nscore of {player_2} is ", score_2)

if score_1>score_2:
    print(f"\n{player_1} is the winner")

elif score_1<score_2:
    print(f"\n{player_2} is the winner")    
    
else:
    print("\nDraw")
