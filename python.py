print("🍕WELCOME TO PANDEY PIZZA🍕")

#introduction
print(" Dear Pizzanian ")
print("Would u like to know our todays menu or want to place direct order ")
print("TYPE 'M' FOR MENU OR 'O' FOR ORDER ")
x=input(":")

if  x=="M":
    print("Cheese Pizza: 120Rs")
    print("Veg Pizza: 100Rs")
    print("MAHARAJA Pizza: 160Rs")
    k=input("would like to order now?? type 'yes'or'no'")
    if k=="yes":
        print("we are gald to offer you an pizza!!!!!!!!")
        name=input("Please enter your name(First and suraname also):").title().strip()
        first, last=name.split()
        adress=input("Please enter your adress:").title().strip()
        phone=input("Please enter your current mobile number:")
        print(f"please select your order {first}!")
        print("1.Cheese Pizza: 120Rs")
        print("2.Veg Pizza: 100Rs")
        print("3.MAHARAJA Pizza: 160Rs")
        print("Please enter the respective number")
        q=int(input(":"))
        print("Please enter the Quantity!!")
        n=int(input(":"))
        print(f"{first} WOULD YOU LIKE TO HAVE DRINKS??")
        print("TYPE 'Y' FOR YES OR 'N' FOR NO ")
        y=input(":")
        if y=="N":
            print("Your order summary:")
            print(name)
            print(adress)
            if q=="1":
                print(f"Your choiced pizza is Cheese Pizza and quantity is {n} for amount:", n*120)

            
            elif q=="2":
                print(f"Your choiced pizza is Veg Pizza and quantity is {n} for amount:", n*100)

            
            else:
                print(f"Your choiced pizza is MAHARAJA Pizza and quantity is {n} for amount:", n*160)

            print("hope you enjoy our pizza!!! and order again")
        

        else :
            
            print("Your order summary:")
            print(name)
            print(adress)
            if q=="1":
               print(f"Your choiced pizza is Cheese Pizza and quantity is {n} for amount:", n*120)

            
            elif q=="2":
               print(f"Your choiced pizza is Veg Pizza and quantity is {n} for amount:", n*100)
 
            
            else:
               print(f"Your choiced pizza is MAHARAJA Pizza and quantity is {n} for amount:", n*160)

      
        
            print("your pizza and drinks will get to u soon.. order again")

    else:
         print("meet you again")

else:
    print("we are gald to offer you an pizza!!!!!!!!")
    name=input("Please enter your name:").title().strip()
    first, last=name.split()
    adress=input("Please enter your adress:").title().strip()
    phone=input("Please enter your current mobile number:")
    print(f"please select your order {first}!")
    print("1.Cheese Pizza: 120Rs")
    print("2.Veg Pizza: 100Rs")
    print("3.MAHARAJA Pizza: 160Rs")
    print("Please enter the respective number")
    q=int(input(":"))
    print("Please enter the Quantity!!")
    n=int(input(":"))
    print(f"{first} WOULD YOU LIKE TO HAVE DRINKS??")
    print("TYPE 'Y' FOR YES OR 'N' FOR NO ")
    y=input(":")
    if y=="N":
        print("Your order summary:")
        print(name)
        print(adress)
        if q=="1":
            print(f"Your choiced pizza is Cheese Pizza and quantity is {n} for amount:", n*120)

            
        elif q=="2":
            print(f"Your choiced pizza is Veg Pizza and quantity is {n} for amount:", n*100)

            
        else:
            print(f"Your choiced pizza is MAHARAJA Pizza and quantity is {n} for amount:", n*160)

        print("hope you enjoy our pizza!!! and order again")
        

    else :
         print("Your order summary:")
         print(name)
         print(adress)
         if q=="1":
            print(f"Your choiced pizza is Cheese Pizza and quantity is {n} for amount:", n*120)

            
         elif q=="2":
            print(f"Your choiced pizza is Veg Pizza and quantity is {n} for amount:", n*100)

            
         else:
            print(f"Your choiced pizza is MAHARAJA Pizza and quantity is {n} for amount:", n*160)

         
        
         print("your pizza will get to u soon.. order again")

print("thank-you")    