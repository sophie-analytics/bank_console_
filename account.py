class Account:
    def __init__(self, account_type: str, account_number):
        self.account_balance = 20000
        self.account_number = account_number
        assert account_type in ["savings", "current"], "Invalid account type. Only 'savings' or 'current' are allowed."
        self.account_type = account_type
        
    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, value):
        self.account_balance = value

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, value):
        self.account_number = value

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, value):
        if value not in ["savings", "current"]:
            raise ValueError("incorrect account type")
        else:
            self.account_type = value
    
    def __str__(self):
        message = f"Account Number is {self.get_account_number()} and it is {self.get_account_type()}"
        return message
    
