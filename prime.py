'''x=int(input("Enter a Number"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
        print("Prime")'''
for x in range(1,100):             
  for i in range(2,x):
    if x%i==0:
     break
  else:
      print(x)

