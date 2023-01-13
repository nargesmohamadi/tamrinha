b=[]
a=int(input("enter a num:"))
while (a!=0):
    b.append(a)
    a=int(input("enter a num:"))
    print(b[::-1])
