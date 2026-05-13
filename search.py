import random

def search(x,n):
    if x<n:
        guess=random.randint(0,n)
        count=0
        while guess!=x:
            if guess<x:
                guess=random.randint(guess,n)
                count=count+1
                continue
            else:
                guess=random.randint(0,guess)
                count=count+1
                continue

    else:
        print("invalid input")

    print(f"Found the number {x} from {n} numbers ,in {count} tries")

search(6,60)