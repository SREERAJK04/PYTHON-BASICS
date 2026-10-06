n=input("Enter the sentence: ")
count=0
k=""
s=""
m=""
for i in n:
    count+=1
    if i==' ':
        if len(k)>len(s):
            s=""
            s=k
            k=""
        elif len(k)==len(s):
            m=""
            m=k
        k=""

    else:
        k+=i
if count==len(n):
    if len(k)>len(s):
        s=k
if len(m)==len(s):
    print("The biggest word is '",s,"' and '",m,"'")
else:
     print("The biggest word is '",s,"'")

