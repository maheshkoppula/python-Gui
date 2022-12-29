username='mahesh'
password='mahesh07'
name=input('enter your name')
pin=str(input('enter your password'))
if name==username and pin==password:
    print('''
1.add_amount
2.withdrwal
3.ministatment
4.exit
''')
   amount=100000
   option=int(input("select your option"))
   if option==1:
   add=int(input("enter amount"))
    amount+=add
        print("total money:",amount)
    elif option==2:
    wit=int(input("enter the amount"))
   amount-=wit
   print("total amount:",amount)
   elif option==3:
   print("=======ATM======")
   print("user name:"username)
   print("amount:",amount)
   print("thank you")
   print("================")

    
else:
print("please enter your correct details")


