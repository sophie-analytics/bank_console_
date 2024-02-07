import re
from account import Account
from transaction import Transaction
from address import Address
from user import User
from datetime import datetime, date
from random import randint

class Bank:

    def __init__(self, name: str, bank_type: str) -> None:
        self.name = name
        self.customers: list(User) = []
        self.bank_type = bank_type

    def get_name(self):
        return self.name
    
    def get_bank_type(self):
        return self.bank_type
    
    def get_customers(self):
        return self.customers
    
    def register(self, customer: User):
        self.validate_customer_details(customer)
        self.validate_customer_info(customer)
        try:
            account = Account(
                    account_number=randint(1000000000, 9999999999),
                    account_type= input("pick account type (savings/current): ")
                )
            customer.add_account(account)
            self.customers.append(customer)
        except AssertionError as error:
            print(f"Account creation failed: {error}")
         
    def validate_customer_details(self, customer: User):
        # we want to check if the customer's email does not exist before in our record
        # becos we want every users to have unique emails
        for cust in self.customers:
            if customer.get_email() == cust.get_email():
                raise ValueError('Customer with Email already exist')
            if customer.get_phone() == cust.get_phone():
                raise ValueError('Customer with phone number already exist')
        if (datetime.today().year - customer.get_dob().year) < 18:
            raise ValueError('Your age must be greater than 17')
        
    def validate_customer_info(self, customer: User):
        pattern_email = r'^[a-zA-Z0-9._-]+@gmail\.com$'
        pattern_phone_no = r'\d{11}'
        if not re.match(pattern_email, customer.get_email()):
            raise ValueError('Invalid Email')
        if not re.match(pattern_phone_no, customer.get_phone()):
            raise ValueError('Invalid Phone number')

    def find_customer(self, account_no: int):
        for user in self.customers:
            for account in  user.get_accounts():
                if account.account_number == account_no:
                    return f"Account Found for user: {user.firstname} {user.lastname}\
                    \nYour Account Balance is  {account.account_balance} {Transaction.currency}"
        return "Customer Account not found"