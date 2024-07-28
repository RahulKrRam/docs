Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p=1234
>>> c=0
>>> while c!=3:
...     c=c+1
...     pin=int(input("Enter a pin"))
...     if pin==p:
...         print("Transaction Successful")
...         break
...     else:
...         print("Incorrect Pin")
... else:
...     print("Card Blocked")
>>> [DEBUG ON]
>>> [DEBUG OFF]
