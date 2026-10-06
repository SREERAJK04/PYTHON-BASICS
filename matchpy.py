n=input("enter a symbol")
match (n):
    case '+':
        print("Addition")
    case '-':
        print("Subtraction")
    case '*':
        print("Multiplication")
    case '/':
        print("Division")
    case _:
        print("Invalid symbol")


