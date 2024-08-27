#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:18:15 2023

@author: yusufhagimohamed
"""

print("*******WELCOME TO OUR BANK*******")

user_name=input(("Please enter your name"))

balance = 1000
op=True
 #student completes while loop
while True:
    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit:")
    choice = input("Please choose transactions:")
    if choice == "1":
        deposit = float(input("Plese enter a depoist amount"))
        while (deposit>0):
            print ("deposit = ", deposit)
            balance = deposit + balance
            print ("You have deposited £", deposit)
            break
        else:
            print ("Please enter a valid amount to deposit")
            
        #'user chooses deposit'
        
        
    elif choice == "2":
        withdrawal = float(input("Please enter the amount you wish to withdraw"))
        while (withdrawal<=1000):
            print ("Withdrawal =", withdrawal)
            balance = balance - withdrawal
            print ("You have withdrew £", withdrawal)
            break
        else:
            print ("Please enter a valid amount to withdraw")
       #User chooses 'withdrawal' 
       
        
    elif choice =="3":
        print("Your balance is £", balance)
        
        
        #User chhoses 'check balance'
      
    elif  choice =="Q" or "q":
        
    #user chooses 'exit'
        
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op= False
        
    
        print(" You have entered an invalid transaction. Try again.")
        #Uswe enters an invalid menu option
        