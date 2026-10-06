e=int(input("Enter the mark for English (out of 50): "))
m=int(input("Enter the mark for Maths (out of 50): "))
c=int(input("Enter the mark for Chemistry (out of 50): "))
b=int(input("Enter the mark for Biology (out of 50): "))
p=int(input("Enter the mark for Physics (out of 50): "))
if 50>=e>=0:
    sum=0
    sum=e
    if 50>=e>=40:
        print("A grade for English")
    elif 39>=sum>=30:
        print("B grade for English")
    elif 29>=sum>=20:
        print("C grade for English")
    elif 19>=sum>=10:
        print("D grade for English")
    else:
        print("Failed for English")
else:
    print("Invalid Mark")
if 50>=m>=0:
    sum=0
    sum=m
    if 50>=m>=40:
        print("A grade for maths")
    elif 39>=sum>=30:
        print("B grade for maths")
    elif 29>=sum>=20:
        print("C grade for maths")
    elif 19>=sum>=10:
        print("D grade for maths")
    else:
        print("Failed for maths")
else:
    print("Invalid Mark")  
if 50>=c>=0:
    sum=0
    sum=c
    if 50>=sum>=40:
        print("A grade for chemistry")
    elif 39>=sum>=30:
        print("B grade for chemistry")
    elif 29>=sum>=20:
        print("C grade for chemistry")
    elif 19>=sum>=10:
        print("D grade for chemistry")
    else:
        print("Failed for chemistry")
else:
    print("Invalid Mark")
if 50>=b>=0:
    sum=0
    sum=b
    if 50>=sum>=40:
        print("A grade for biology")
    elif 39>=sum>=30:
        print("B grade for biology")
    elif 29>=sum>=20:
        print("C grade for biology")
    elif 19>=sum>=10:
        print("D grade for biology")
    else:
        print("Failed for biology")
else:
    print("Invalid Mark")
if 50>=p>=0:
    sum=0
    sum=p
    if 50>=sum>=40:
        print("A grade for physics")
    elif 39>=sum>=30:
        print("B grade for physics")
    elif 29>=sum>=20:
        print("C grade for physics")
    elif 19>=sum>=10:
        print("D grade for physics")
    else:
        print("Failed for physics")
else:
    print("Invalid Mark")
if 50>=e>=0 and 50>=m>=0 and 50>=c>=0 and 50>=b>=0 and 50>=p>=0:
    sum1=e+m+c+b+p
    sum2=sum1/5
    if 50>=sum2>=40:
        print("A GRADE OVERALLL.....")
    elif 39>=sum2>=30:
        print("B GRADE OVERALLL.....")
    elif 29>=sum2>=20:
        print("C GRADE OVERALLL.....")
    elif 19>=sum2>=10:
        print("D GRADE OVERALLL.....")
    else:
        print("FAILED......")
    print("THE AVERAGE MARK IS:",sum2,"/50......") 
    print("THE TOTAL MARK IS:",sum1,"/250......") 