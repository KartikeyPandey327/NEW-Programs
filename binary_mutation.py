count=0

def binary_search(l,x,start,end):
    l.sort()
    global count
    global found
    if start>end:
        print("Not found")
        return

    count+=1
    mid=(start+end)//2

    
    if l[mid]==x:
        print(f"Found after {count} tries")

    elif l[mid]>x:
        binary_search(l,x,start,mid-1)

    else:
        binary_search(l,x,mid+1,end)
        

    


l=[1,2,3,4,5,6,7,8,9]

                 
binary_search(l,8,0,len(l)-1)