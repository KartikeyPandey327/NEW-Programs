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
        #print(row)
        print(" ".join(map(str, row)))

            
magic_square(3)

#Steps

#1) In any magic square, 1 is located at position (n/2, n-1).

#2) Let's say the position of 1 i.e. (n/2, n-1) is (p. q), then next number which is 2 is located at (p-1, q+1) position. Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0.

#3) If the calculated position already contains a number then decrement the column by 2 and increment the row by 1.

#4) If anytime row position becomes -1 and column becomes n, switch it to (0, n-2).
