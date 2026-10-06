l=0
s=0
for i in range(3):
    n=int(input("Enter the number: "))
    if l<n:
        s=l
        l=n
    else:
        l=l
        if n>s:
            s=n
        else:
            s=s
print(s,"is the second largest number")
