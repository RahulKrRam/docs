'''p=1234
c=0
while c!=3:
    c=c+1
    pin=int(input("Enter a pin : "))
    if pin==p:
        print("Transaction Successful")
        break
    else:
        print("Incorrect Pin")
else:
    print("Card Blocked")'''

d1=dict(one="Amit",two="Ajay",three="atul",four="ashish")
print(d1)
for i in d1:
    print(i,d1[i])


def fun1():
    print("Hello Friends")
    print("Hello Fun1")
fun1()
