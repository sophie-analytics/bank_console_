#!/usr/bin/python3
import re
from account import Account
from random import randint
from datetime import datetime
class Transaction:
    currency = "Naira"

    def __init__(self, account: Account, transaction_status='pending', transaction_pin =0000, transaction_date: datetime= None):
        self.transaction_id = randint(100000000000, 999999999999)
        self.transaction_date = transaction_date if transaction_date else datetime.now()
        self.account = account
        self.transaction_pin = transaction_pin
        self.transaction_status = transaction_status

    def get_transaction_pin(self):
        return self.transaction_pin
    
    def get_transaction_status(self):
        return self.transaction_status
    
    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_pin(self, value):
        self.transaction_pin = value

    def set_transaction_status(self, value):
        self.transaction_status = value
    
    def change_transaction_pin(self, old_pin, new_pin):
        if self.transaction_pin != old_pin:
            raise ValueError("Incorrect old PIN.")
        self.set_transaction_pin(new_pin)
        return "Transaction PIN changed successfully."

    def __str__(self):
        return f"Transaction details >>> Transaction_id: {self.transaction_id}\n Account Number: {self.account.get_account_number()}\n"


class Transfer(Transaction):
    def __init__(self, amount: int,  account: Account, destination_account_no: int,  destination_bank: str,  transaction_pin =0000, transaction_date: datetime= None):
        super().__init__(account, transaction_date, transaction_pin)
        self.destination_account_no = destination_account_no
        self.destination_bank = destination_bank
        self.amount = amount

    def approve_transcation(self):
        try:
            print("Approve transaction called")
            self.validate_transaction()
            account_balance = self.account.get_account_balance() - self.amount
            self.account.set_account_balance(account_balance)
            self.set_transaction_status("Success")
        except ValueError as error:
            print(f"[ Error: {error}] ")
            self.set_transaction_status("Failed")

    def validate_transaction(self):
        pattern_account_no = r'\d{10}'
        if self.amount > self.account.get_account_balance() or self.amount <= 0:
            raise ValueError("You do not have enough money for this transaction")
        print(f"processing {self.destination_account_no}")
        if len(self.destination_account_no) != 10 or not re.match(pattern_account_no, self.destination_account_no):
            raise ValueError("Incorrect destination account number! Kindly check that it is accurate")
         
        if len(self.account.get_account_number()) != 10 or not re.match(pattern_account_no, self.account.get_account_number()):
            raise ValueError("Incorrect account number! Kindly check that it is accurate")
        
        if self.transaction_pin != self.get_transaction_pin():
            raise ValueError("Incorrect transaction pin! Kindly check that it is accurate")
        
    def __str__(self):
        transaction_description = f"\nYour transcation {self.get_transaction_status()}\ntransaction Date: {self.transaction_date}\nTransaction Id: {self.get_transaction_id()}\
        \nAccount Number: {self.account.get_account_number()}\nDestination Account: {self.destination_account_no}\nAmount: {self.amount}{Transaction.currency}\nAccount Balance: {self.account.get_account_balance()}{Transaction.currency}"
        return transaction_description