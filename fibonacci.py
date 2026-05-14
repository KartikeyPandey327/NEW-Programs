n=int(input("Enter the value of the nth fibonacci you want to see"))

fibonacci=[]
i=0

p=0 #first value
q=1 #second value

if i<n:
    r=p+q
    fibonacci.append(r)
    i+=1
    while i<n:
        p=q
        q=r
        r=p+q
        fibonacci.append(r)
        i+=1 
        continue
        

print(fibonacci)
            