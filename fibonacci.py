#while loop can be used as recurstion in the same program broooooooooooo...


fibonacci_series=[]
i=0
def fibonacci(p,q,n):
    global i
    
    if i==0:
        fibonacci_series.append(p)
        i+=1

    if i==1:
        fibonacci_series.append(q)
        i+=1
              
    if i<n:
        r=p+q
        fibonacci_series.append(r)
        
        i +=1
        fibonacci(q,r,n)

    else:
        print(fibonacci_series)
        i=0
        fibonacci_series.clear()
        
        
        

fibonacci(0,1,6)
fibonacci(0,1,2)
fibonacci(0,1,8)