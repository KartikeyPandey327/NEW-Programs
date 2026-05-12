year=int(input("Enter the year: "))

if year%4==0:
    if year%400==0:
        print("its a leap year")

    if year%100==0:
        print("its not a leap year")
    else:
        print("its a leap year")
        
else:
    print("its not a leap year")
    
    
