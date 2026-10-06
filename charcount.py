n=input("Enter the string: ")
d=m=u=l=0
for i in n:
    if i.isalnum():
        if i.isalpha():
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
        elif i.isdigit():
            d+=1
    else:
        m+=1
print("There are ",u,"upper case letters")
print("There are ",l,"lower case letters")
print("There are ",d,"digits")
print("There are ",m,"special characters")