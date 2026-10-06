name=[]
for i in range(10):
    n=input("Enter the name: ")
    name.append(n)
print(name)
m=input("Enter the new student name: ")
name.append(m)
print(name)
n1=input("The name of student who requested 3rd place: ")
name[2]=n1
print(name)
n2=input("Enter the name of the student that need to withdrawn: ")
name.remove(n2)
print(name)
n3=input("Enter the name to be accepted: ")
if n3 in name:
    print("The student is present in the list")
    print(name.find(n3))
else:
    print("The student is not in the list")
n4=input("Enter the name to be count checked: ")
count=0
for x in name:
    if n3==x:
        count+=1
    else:
        print("The student is not in the list")

