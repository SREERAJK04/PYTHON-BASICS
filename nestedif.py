n=int(input("Enter a number: "))
if n>0:
    print("The number is positive")
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")