matrix=[[ '_' for i in range(3)] for j in range(3)]
k=None
def won(i,j):
    global k
    
    if matrix[0][0]==matrix[0][1]==matrix[0][2] and  matrix[0][0]!="_":
        won=matrix[0][0]
        print("Game over, Won by", won)
        k=1

    elif matrix[0][0]==matrix[1][0]==matrix[2][0] and  matrix[0][0]!="_":
        won=matrix[0][0]
        print("Game over, Won by", won)
        k=1

    elif matrix[0][0]==matrix[1][1]==matrix[2][2] and  matrix[0][0]!="_":
        won=matrix[0][0]
        print("Game over, Won by", won)
        k=1

    elif matrix[1][0]==matrix[1][1]==matrix[1][2] and  matrix[1][0]!="_":
        won=matrix[1][0]
        print("Game over, Won by", won)
        k=1

    elif matrix[2][0]==matrix[2][1]==matrix[2][2] and  matrix[2][0]!="_":
        won=matrix[2][0]
        print("Game over, Won by", won)
        k=1

    elif matrix[0][1]==matrix[1][1]==matrix[2][1] and  matrix[0][1]!="_":
        won=matrix[0][1]
        print("Game over, Won by", won)
        k=1

    elif matrix[0][2]==matrix[1][2]==matrix[2][2] and  matrix[0][2]!="_":
        won=matrix[2][2]
        print("Game over, Won by", won)
        k=1

    elif matrix[0][2]==matrix[1][1]==matrix[2][0] and  matrix[2][0]!="_":
        won=matrix[0][2]
        print("Game over, Won by", won)
        k=1

        


while k==None:
    
    if any('_' in row for row in matrix):
        print("X to play: ")
        while k==None:
            i=int(input("Enter the row number: "))
            j=int(input("Enter the column number: "))
            i -= 1
            j -= 1
            if  matrix[i][j]=="_":
                matrix[i][j]="X"

                for row in matrix:
                    print(" ".join(map(str,row)))
                won(i,j)
                

                break
        

            else:
                print("The place is already played, play diffent move.")
            


        
        while k==None:
            print("O to play: ")
            i=int(input("Enter the row number: "))
            j=int(input("Enter the column number: "))
            i -= 1
            j -= 1
            if  matrix[i][j]=="_":
                matrix[i][j]="O"
                for row in matrix:
                    print(" ".join(map(str,row)))
                won(i,j)
                
                break
        

            else:
                print("The place is already played, play diffent move.")

                




    else:
        print("draw")
        break

for row in matrix:
    print(" ".join(map(str,row)))
                

            