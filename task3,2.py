n=int(input("Enter your age: "))
n1=input("Do yo have any id proof?....yes/No: ")
if n>=18 :
    if n1=="yes" or n1=="YES" or n1=="Yes":
        print("Eligible and applicable for driving license")
    else:
        print("Not applicable")
else:
    print("not eligible")