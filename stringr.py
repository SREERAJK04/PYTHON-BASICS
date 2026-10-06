n=int(input("Enter the number: "))
num=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if rev==num:
    print("Palindrome")
else:
    print("not palindrome")