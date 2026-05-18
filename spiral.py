import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
t.color("white")

distance=25

t.penup()
t.setpos(-250, 250) 
t.pendown()

t.speed(0.3)
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
    f=0
    while r1<=r2:
        
        if f>=1:
            t.right(90)
            
        for j in range(r1,r2+1):
            t.forward(distance)
            #number.append(matrix[r1][j])
        f+=1
        t.right(90)    
        for i in range(r1+1,r2+1):
            t.forward(distance)
            #number.append(matrix[i][r2])
        t.right(90)    
        for j in range(r2-1,r1-1,-1):
            t.forward(distance)
            #number.append(matrix[r2][j])
        t.right(90)
        for i in range(r2-1,r1,-1):
            t.forward(distance)
            #number.append(matrix[i][r1])
            
       
            
            

        r1+=1
        r2-=1
       
            
            
    
spiral(20)
turtle.done()

    
