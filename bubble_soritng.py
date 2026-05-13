def bubble(n):
    length= len(n)
    k=0
    while k<=len(n):
        for i in range(length-1):
           x=n[i]
           y=n[i+1]
           if n[i]>n[i+1]:
               n[i]=y
               n[i+1]=x
               k=k+1
           else:
               k=k+1
               continue

    for i in n:
        print(i)

num=[2,1,9,7]
bubble(num)
            
    

