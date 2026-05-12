import random
Birthday=[]


def leap_year(year):
    
    if year%4==0:
        if year%400==0:
            return "leap"

        elif year%100==0:
            return "not a leap"
        else:
            return "a leap"
        
    else:
        return "a leap"
i=1    
while i<60:    
    year=random.randint(1900,2024)
    feb=leap_year(year)
    month=random.randint(1,12)
    if month%2==0 and month<7:

        if month==2:
            if feb=="leap":
                day=random.randint(1,29)
                
            else:
                day=random.randint(1,28)
            

        else:
            day=random.randint(1,30)
            
        

    elif month%2!=0 and month<=7:
        day=random.randint(1,31)
        

    elif month%2==0 and month>7:
        day=random.randint(1,31)
        
    
    elif month%2!=0 and month>=7:
        day=random.randint(1,30)
        
    
    i=i+1
    Birthday.append(str(day)+" / "+str(month))

Birthday.sort()
print("Day / Month")
for _ in Birthday:
    print(_)
