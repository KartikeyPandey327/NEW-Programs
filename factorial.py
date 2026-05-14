n=int(input("Enter the number whose factorial u want: "))

# using for loop
answer=1
for i in range(n+1):
    if i!=0:
        answer=answer*i
print(answer)        
        

#using while loop    
factorial=n
while n!=0:
    n=n-1
    if n==0:
        break
    else:
        factorial=factorial*n
        continue
print(factorial)
    
for i in range(n):
    print (i)
    
