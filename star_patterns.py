'''for i in range(5):
    print("*")'''
'''for i in range(5):
    print("A",end='')
    for j in range(3):
     print("B",end='')
    print()'''
'''for i in range(5):
    for j in range(5):
      if j<=i:
             print("*",end='')
      else:
            print('',end='')
    print()'''
'''for i in range(5):
    for j in range(5):
      if j<=4-i:
             print("*",end='')
      else:
            print('',end='')
    print()''' 
'''for i in range(1,5):
    for j in range(1,8):
      if j> =5-i and j<=3+i:
             print("*",end='')
      else:
            print('',end='')
    print()'''
'''for i in range(1,5):
    for j in range(1,8):
      if j> =5-i and j<=3+i:
             print("*",end='')
      else:
            print('',end='')
    print()'''

'''p=int(input("Enter srarting range:"))
q=int(input("Enter ending range:"))
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
            print(x,end=' ')'''

p=int(input("Enter srarting range:"))
q=int(input("Enter ending range:"))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
            print(x,end=' ')
            h.append(x)
print(h)
length=len(h)
mid=length//2
print(h[mid]+h[mid-1])
  
