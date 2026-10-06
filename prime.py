m=int(input("Enter the number limit: "))
count=0
sum=0
print("Prime numbers are.....")
for j in range(2,m+1):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(j)
        sum+=j
print("There are ",count," Prime numbers") 
print("Total sum of prime number is: ",sum)       
    