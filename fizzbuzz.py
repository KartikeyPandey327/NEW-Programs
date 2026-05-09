'''

for i in range(1,51):
    if i%3==0:
        if i%5==0:
            print(i," = fizzbuzz")
        else:
            print(i," = fizz")

    elif i%5==0:
        if i%3==0:
            print(i," = fizzbuzz")
        else :
            print(i," = buzz")
    else:
        print(i)
'''
#else

def fizz_buzz(r):
    for i in range(1,r):
        if i%3==0 and i%5==0:
            print("fizzbuzz")

        elif  i%3==0:
            print("fizz")

        elif i%5==0:
            print("buzz")

        else:
            print(i)
         
fizz_buzz(51)        
    
      
