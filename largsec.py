n=int(input("Enter the limit: "))
l=0
sc=0
for i in range(n):
    m=int(input("Enter the number: "))
    if m>sc:
        if m>l:
            sc=l
            l=m
        else:
            sc=m
    else:
        l=l
        sc=sc
print("THE LARGEST NUMBER IS: ",l)
print("THE SECOND LARGEST NUMBER IS ",sc)


