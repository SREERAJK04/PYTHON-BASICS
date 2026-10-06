n=int(input("Enter the units consumed: "))
m=0
if n>200:
    m=n*5
elif n<=100:
    m=n*2
else:
    m=n*3
print("The electricity bill is: ",m)

    