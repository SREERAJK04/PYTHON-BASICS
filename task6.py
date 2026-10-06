n=int(input("Enter the first Number: "))
m=int(input("Enter the second number: "))
op=input("Enter the operator: ")
match(op):
    case '+':
        print("The sum is ",n+m)
    case'-':
        if n>=m:
            print("The difference is ",n-m)
        else:
            print("The difference is ",m-n)
    case'*':
        print("The product is ",n*m)
    case'/':
        print("The quotient is ",n/m)
    case _:
        print("Invalid operator")