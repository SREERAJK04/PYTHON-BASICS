m=int(input("Enter the lowest boundary: "))
n=int(input("Enter the highest boundary: "))
count=0
for i in range(m,n+1):
    num=i
    pal=0
    while i>0:
        d=i%10
        pal=pal*10+d
        i//=10
    if num==pal and num%3==0:
        count+=1
        print(num)
print("There are ",count,"numbers")
