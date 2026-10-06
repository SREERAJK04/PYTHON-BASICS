n=input("Enter the string: ")
k=""
for i in n:
    if i in k:
        continue
    else:
        k+=i
print(k)