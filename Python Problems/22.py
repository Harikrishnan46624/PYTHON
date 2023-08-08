class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.accont_number = account_number

        @property
        def name(self):
            return self.name
        
        @name.setter
        def name(self, name):
            self.name = name

        @property
        def account_number(self):
            return self.account_number
        
        @account_number.setter
        def account_number(self, accont_number):
            self.accont_number = account_number

account = BankAccount("jhon","123978655")
print(account.name)
print(account.accont_number)

account.name = "dasan"
account.accont_number = "6572130347"

print(account.name)
print(account.accont_number)