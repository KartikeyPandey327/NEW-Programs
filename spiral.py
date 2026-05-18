def spiral(n):
    
    
    matrix=[]
    num=1
    number=[]

    for i in range(n):
        row=[]
        for j in range(n):
            row.append(num)
            num += 1
        matrix.append(row)
    r1=0
    r2=n-1
    while r1<=r2:
        for j in range(r1,r2+1):
            number.append(matrix[r1][j])
            
        for i in range(r1+1,r2+1):
            number.append(matrix[i][r2])
            
        for j in range(r2-1,r1-1,-1):
            number.append(matrix[r2][j])

        for i in range(r2-1,r1,-1):
            number.append(matrix[i][r1])
            
       
            
            

        r1+=1
        r2-=1
    print(number)    
            
            
    
spiral(4)