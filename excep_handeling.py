cb=10000

while True:  #while loop start 
  wb=int(input("Enter amount to withdraw : ")) #input lene ke liye
  try:
    if(cb<wb):
        raise ValueError() #Exception handling function
    cb=cb-wb
    print("Money Sent")
    print("Current Bal is", cb)
        
  except ValueError:
    print("Insufficient Balance.")
    print("Current Bal is", cb)
        
  finally:
      print("Bye") #Finally ka code chalegahi chalega
