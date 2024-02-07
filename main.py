#!/usr/bin/python3
from bank import Bank
from user import User
from datetime import date
from address import Address
from transaction import Transaction, Transfer
from account import Account

sophie_bank = Bank('Bank of Sophie', 'Commmercial Bank')
print(f'\nWelcome to {sophie_bank.get_name()}, the customer\'s choice bank. \n\
We are a {sophie_bank.get_bank_type()} helping customers to acheive their savings goals')
while (True):
    print("======================================")
    information = """ 
        SELECT 1:  First Time Regstration
        SELECT 2 : Tranfer
        SELECT 3 : View account balance
        SELECT 4 : Change Transaction Pin
    """
    print(information)
    customer_1_input = input(">>>>  ")
    if customer_1_input == "1":
        print("Begin Registration")
        print("======================================")
        customer_1 = User(
            firstname=input('Kindly enter your first name >>>  '),
            lastname=input('Kindly enter your last name >>> '),
            email=input('Kindly enter your email >>>  '),
            phone=input('Kindly enter your phone number >>>  '),
            dob=date(int(input('Enter year of Birth >>>  ')), int(input('Enter birth month >>> ')), int(input('Enter birth day >>>  '))),
            address=Address(
                city=input('What city do you live in >>>   '),
                state=input('What state do you live in >>>   '),
                country=input('What country do you live in >>>   '),
                street=input('What street do you live on >>>  '),
                house_no=input('What is your house number >>>   ')
            ),
            password=input('Set you account password >>>  ')
        )
        try:
            sophie_bank.register(customer_1)
            print("=====================================")
            print("Registation Successful")
            print(customer_1)
        except (ValueError, AssertionError) as error:
            print(f"[ Error During Registration : {error} \n Register Your Detials Again ] ")

    elif customer_1_input == "2":
        try:
            transfer = Transfer(
            amount=int(input("Enter Amount To be Transfereed >>>  ")),
            account=Account(
                    account_type=input("Enter Account type savings/current >>>> "),
                    account_number=input("Enter Your Account Number >>>  ")
                ),
                destination_account_no=input("Enter The destination Account No >>>>  "),
                destination_bank=input("Enter The Destination Bank >>>  "),
                transaction_pin=input("Enter your transaction pin (default: 0000)>>> ")
            )
            transfer.approve_transcation()
            print(transfer)
        except (ValueError, AssertionError) as error:
            print(f"Error: {error}")
        
    elif customer_1_input == "3":
        account_no = int(input("Enter Your Account No >>> "))
        print(sophie_bank.find_customer(account_no))

    elif customer_1_input == "4":
        account_number = int(input("Enter your account number: "))
        find_result = sophie_bank.find_customer(account_no=account_number)
        if "Account Found" in find_result:
            transaction = Transaction(
                Account(
                    account_type=input("Enter Account type savings/current >>>> "),
                    account_number=account_number
                    )
            )
            try:
                transaction.change_transaction_pin(
                    old_pin=int(input("Enter your current transaction PIN: ")),
                    new_pin=input("Enter your new transaction PIN: ")
                )
                print("PIN changed successfully.")
            except ValueError as e:
                print(e)
        else:
            print("You don't have an account")
