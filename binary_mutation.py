import random
import time

def evolution():

    target=[1,1,1,1,1,1,1,1,1,1]

    original=[random.randint(0,1) for _ in range(10)]

    evolution=0

    while original != target:

        evolution += 1

        index=random.randint(0,9)

        old_value=original[index]

        if original[index]==0:
            original[index]=1

        else:
            original[index]=0

        if original[index]<old_value:
            original[index]=old_value

        else:
            if original[index]!=old_value:
                print(f"Gen {evolution}: {original} (Success!)")

        time.sleep(0.2)         

    print(f"--- Evolution Complete in {evolution} generations! ---")