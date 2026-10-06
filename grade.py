e=int(input("Enter the mark for English (out of 50): "))
m=int(input("Enter the mark for Maths (out of 50): "))
c=int(input("Enter the mark for Chemistry (out of 50): "))
b=int(input("Enter the mark for Biology (out of 50): "))
p=int(input("Enter the mark for Physics (out of 50): "))
sum=0
sum1=e+m+c+b+p
sum=(e+m+c+b+p)/5
if 50>=e>=0 and 50>=m>=0 and 50>=c>=0 and 50>=b>=0 and 50>=p>=0:
    if 50>=sum>=40:
        print("A GRADE OVERALLL.....")
    elif 39>=sum>=30:
        print("B GRADE OVERALLL.....")
    elif 29>=sum>=20:
        print("C GRADE OVERALLL.....")
    elif 19>=sum>=10:
        print("D GRADE OVERALLL.....")
    else:
        print("FAILED......")
    print("THE TOTAL AVERAGE MARK IS:",sum,"......") 
    print("THE TOTAL MARK IS:",sum1,"/250......") 
else:
    print("Invalid mark entered") 