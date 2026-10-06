n=int(input("Enter the number: "))
n2=n1=n
dcount=1
dsum=0
l=0
s=0
while n>0:
    d=n%10
    dsum+=d
    if l<d:
        l=d
    n//=10
    dcount+=1
s=l
while n1>0:
    d=n1%10
    if s>d:
        s=d
    n1//=10
for k in range(10):
    num=n2
    count=0
    dig=0
    while num>0:
        dig=num%10
        if dig==k:
            count+=1
        num//=10
    if count>0:
        print(k," repeats ",count,"times")
print("There are",dcount,"digits")
print("The sum of digit is ",dsum)
print("The largest number is: ",l)
print("The smallest number is: ",s)
