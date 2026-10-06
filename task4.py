n=4625
n1=int(input("Enter The pin: "))
bal=5000
if n1==n:
    n2=int(input("Enter the amount: "))
    if bal>=n2:
        print("money granted")
        bal-=n2
        print("balance is ",bal)
    else:
        print("Not sufficient balance")
else:
    print("Incorrect pin")    