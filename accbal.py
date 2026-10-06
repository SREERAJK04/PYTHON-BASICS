n=int(input("Enter the account balance: "))
c=3
while c>0:
    m=int(input("Enter the amount to withdrawn: "))
    s=m
    if s%100==0:
        if n>500:
            l=n
            if (l-m)>500:
                n-=m
                print("The amount is sanctioned ........")
                print("The balance is", n,".......")
            else:
                print("Minimum balance after withdrawal must be ₹500")
                break
        else:
                print("Insufficient balance..........")  
                break 
    else:
         print("Withdrawal must be a multiple of ₹100")    
         break     

    