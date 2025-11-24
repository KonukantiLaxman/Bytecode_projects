#!/usr/bin/env python
# coding: utf-8

# In[24]:


print("=== Welcome to HDFC Bank ATM ===")
balance=50000
correct_pin="2004"
pin=input("enter Pin:")
n=0
while n<2 and pin!=correct_pin:
    print("Wrong PIN! 2 attempts left")
    pin=input("enter Pin:")
    n+=1
if pin!=correct_pin:
    print("Card Blocked!")
else:
    print("Access Granted!")
    
    print("==Main ATM Menu Loop==")

    print("\n | option |what to do")
    print("| 1 | print current balance |")
    print("| 2 |  Withdraw Cash    |")
    print("| 3 |  Deposit Cash   |")
    print("| 4 |  Change PIN     |")
    print("| 5 |   Exit          |")

    choice=int(input("enter any choice(1-5)"))
    match(choice):
        case 1:
            print("current balance",balance)
        case 2:
            amount=int(input("enter amount to withdraw:"))
            if amount%100==0 and amount<=balance:
                balance-=amount
                print("withdraw successful")
                print("new balance:",balance)
            else:
                print("invalid amount  or insufficient balance")
        case 3:
            amount=int(input("enter amount to withdraw:"))
            balance+=amount
            print("deposit succesful")
            print("new balance:",balance)
        case 4:
            old=int(input("enter old Pin:"))
            if old==correct_pin:
                new_pin=int(input("enter 4-digit new pin:"))
                if len(new_pin)==4 and new_pin.isdigit():
                    correct_pin=int(new_pin)
                    print("pin updated successfully")
                else:
                    print("pin must be 4-digit")
            else:
                print("incorrect old pin!")
        case 5:
            print("Thank you..!")
        case _:
         print("Invalid option..,try again.")

            
        

    
        
            
        

    
        


# In[ ]:





# In[ ]:




