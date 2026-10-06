balance=20000
n=int(input("1.Deposit    2.Withdraw   3.balance  :   "))
match (n):
    case 1:
        n1=int(input("Enter the amount to deposit  :  " ))
        balance+=n1
        print("The balance amount is ",balance)
    case 2:
        n2=int(input("Enter the amount to withdraw  :  " ))
        if balance>=n2:
                print("money granted")
                balance-=n2
                print("balance is ",balance)
        else:
            print("Not sufficient balance")
    case 3:
        print("The balance amount is ",balance)
    case _:
          print("Invalid")