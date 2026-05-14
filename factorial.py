# Factorial of a number using recursion
def fact(n):
    if n==1:
        return(1)
    elif n>1:
        return(n*fact(n-1))
    else:
        print("incorrect value of n")

n=int(input("Enter the number whose factorial u want: "))
print(fact(n))


