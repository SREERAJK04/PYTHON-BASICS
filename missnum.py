n=int(input("Enter the limit: "))
l=1
s=0
for i in range(1,n):
    m=int(input("Enter the number: "))
    if m==l or m==l+1:
        l=m
    else:
        if m==l+2:
            s=l+1
            l=m

print(s)
