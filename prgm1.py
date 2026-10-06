m="python programming language"
print(m.title())
print(".........................")


l="Python is easy and Python is powwerful"
print(l.count("Python"))
n="student123"
count=0
count1=0
for i in n:
    if i.isalnum():
        count+=1
        if i.isalpha():
            count1+=1
if count==count1:
    print("This string omly contain alphabets")
elif count>count1:
    print("This string both contain alphabets and numbers")
else:
    print("There is no alphanumerics")
print("..............................................")


text="Hello Python Program"
print(text.startswith("Hello"))
print(text.endswith("Programming"))
print("........................................")


t = "python,java,python,c++,java"
print(t.count("python"))
print(t.replace("java","django"))
print(t.split())
print("...........................................")

t1="WELCOME to PYTHON"
print(t1.swapcase())
print(t1.islower())
print(".............................................")


t2= "apple orange banana"
print(t2.find("orange"))
print(t2.replace("orange","grape"))
print("............................................")


s = "  PYTHON programming  "
s1=s.strip()
print(s1.title())
print(s1.isupper())
print("........................................")


a= "python, python, java, django, python"
a1=a.replace(" ","")
print(a1.count("python"))
a2=a1.replace("python","Python")
print(a2.split())
