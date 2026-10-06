count=1
while count<3:
    n=int(input("Enter the number: "))
    if n>0:
        if n%2==0:
            print("It is an positive even number")
        else:
            print("It is an positive odd number")
    elif n<0:
        print("It is an Negative number")
    else:
        break