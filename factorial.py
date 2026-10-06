n=int(input("Enter the number: "))
num=n
a=0
b=1
if n==1:
    print("The factorial of 1 is 1")
else:    
    while n>1:
        a=n*(n-1)
        b*=a
        n=n-2
    print("The factorial of ",num,"is",b)
