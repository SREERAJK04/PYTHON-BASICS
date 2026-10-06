n=int(input("Enter the number: "))
for i in range (1,21):
    if (n*i)%2==0:
        print(n," X ",i," = ",n*i)
    else:
        print(n," X ",i)