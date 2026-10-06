n=input("Enter the string: ")
count=d=u=l=0
for i in n:
    if i.isalnum():
        if i.isalpha():
            count+=1
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
        elif i.isdigit():
            d+=1
if count>=8 and u>=1 and l>=1 and d>=1:
    print("It is a valid password")
else:
    print("INVALID PASSWORD")     
