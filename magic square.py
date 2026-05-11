def magic_square(n):
    magic_number=(n*(n*n+1))//2
    print(f"The magic number is {magic_number}")

    magicSquare=[[ 0 for i in range(n)] for j in range (n)]

    

    i=n//2
    j=n-1
    num=n*n
    count =1
    
    while count<=num:
        if i==-1 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1

            if j==n:
                j=0

        if magicSquare[i][j]!=0:
            i=i+1
            j=j-2
            continue

        magicSquare[i][j]=count
        count=count+1

        i=i-1
        j=j+1
                

    for row in magicSquare:
        print(" ".join(map(str, row)))

            
magic_square(3)