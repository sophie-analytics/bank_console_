from datetime import datetime
from account import Account
from address import Address

class User:
    
    def __init__(self, firstname: str, lastname: str, email: str, phone: str, dob: datetime, address: Address, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.dob = dob
        self.address = address
        self.password = password
        self.accounts: list(Account) =[]

    def add_account(self, account):
        self.accounts.append(account)
    
    def get_accounts(self):
        return self.accounts

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, value):
        self.firstname = value

    def get_lastname(self):
        return self.lastname
    
    def set_lastname(self, value):
        self.lastname = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_phone(self):
        return self.phone

    def set_phone(self, value):
        self.phone = value

    def get_dob(self):
        return self.dob

    def set_dob(self, value):
        self.dob = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

    def get_password(self):
        return self.password

    def set_password(self, value):
        self.password = value

    def __str__(self):
        account_info = "\n".join([str(account) for account in self.accounts])
        full_name = f"{self.firstname} {self.lastname}"
        return f"User: {full_name}, Accounts:\n{account_info}"