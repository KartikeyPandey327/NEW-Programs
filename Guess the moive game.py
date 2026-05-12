import random

movies = [
    "Sholay", "Mughal-e-Azam", "Mother India", "Dilwale Dulhania Le Jayenge", "Lagaan", "3 Idiots", "Dangal",
    "Kabhi Khushi Kabhie Gham", "Pyaasa", "Deewaar", "Dil Chahta Hai", "Queen", "Taare Zameen Par",
    "Bajrangi Bhaijaan", "Gangs of Wasseypur", "Kuch Kuch Hota Hai", "Swades", "Chak De India", "Guide",
    "Amar Akbar Anthony", "My Name Is Khan", "Andhadhun", "Barfi", "PK", "Jawan", "Pathaan", "Stree",
    "12th Fail", "Drishyam", "Om Shanti Om"
    ]


p1=input("Enter the name of player 1: ")
p2=input("Enter the name of player 2: ")

score1=0
score2=0

print("Welcome to the guess the movie game:")

while True:
    start=input("Enter start to start or stop to end the game:")
    if start!="stop":
        movie=random.choice(movies)

        movie_length=len(movie)

        guess=["_"]*movie_length

        movie_letterbyletter=list(movie)
    
        print(f"\n{p1} to guess first\n")
        print(" ".join(guess))

        while True:
            if "_" in guess:
                print("Enter show to show the name!")
                x=input("Guess the letter:")
                if x in movie_letterbyletter:
                    for i in range(movie_length):
                        if movie[i]==x:
                            if guess[i]=="_":
                                guess[i]=x
                                print("Correct!!\n")
                            else:
                                print("The word is used before!\n")
             
                    print(" ".join(guess))

                elif x=="show":
                    print(movie)
                    guess=[0]*movie_length 
        
                else:
                    print(f"{x} not in the name!\n")
                    continue

            elif "0" in guess:
                print("you seen the answer so no added score")
                break

            else:
                print("\nYou have guessed the name!!")
                score1 += 1
                break

        movie=random.choice(movies)

        movie_length=len(movie)

        guess=["_"]*movie_length

        movie_letterbyletter=list(movie)
    
        print(f"\n{p2} to guess first\n")
        print(" ".join(guess))

        while True:
            if "_" in guess:
                print("Enter show to show the name!")
                x=input("Guess the letter:")
                if x in movie_letterbyletter:
                    for i in range(movie_length):
                        if movie[i]==x:
                            if guess[i]=="_":
                                guess[i]=x
                                print("Correct!!\n")
                            else:
                                print("The word is used before!\n")
             
                    print(" ".join(guess))

                elif x=="show":
                    print(movie)
                    guess=[0]*movie_length 
        
                else:
                    print(f"{x} not in the name!\n")
                    continue

            elif 0 in guess:
                print("you seen the answer so no added score")
                break

            else:
                print("\nYou have guessed the name!!")
                score2 += 1
                break

        print(f"Score of {p1} is {score1}")
        print(f"Score of {p2} is {score2}")

    else:
        break
        

        