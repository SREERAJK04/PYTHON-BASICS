sum=0
sum1=0
count=0
count1=0
count2=0
for i in range(10):
    n=int(input("Enter the number: "))
    if n>0:
        count+=1
        sum+=n
    elif n<0:
        count1+=1
        sum1+=n
    else:
        count2+=1
print("There are",count,"positive numbers")
print("The sum of positive numbers are: ",sum)
print("There are",count1,"negative numbers")
print("The sum of negative numbers are: ",sum1)
print("There are",count2,"zeros present")