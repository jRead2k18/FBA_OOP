class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(0, 0.02)
    def make_deposit (self, amount):
        self.account.bal += amount
        return self
    def make_withdrawal(self, amount):
        self.account.bal -= amount
        return self
    def display_user_balance(self):
        print(self.name, "- Balance:", self.account.bal)
        return self
    def transfer_money(self, otherUser, amount):
        self.account.bal -= amount
        otherUser.account.bal += amount
        print(self.name, "- Balance:", self.account.bal)
        print(account.name, "- Balance:", account.account.bal)
        return self
class BankAccount:
    def __init__(self, balance = 0, int_rate = 0.0825):
        self.ir = 1 + int_rate
        self.bal = balance
    def deposit(self, amount):
        self.bal += amount
        return self
    def withdraw(self, amount):
        if (self.bal >= amount):
            self.bal -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.bal -= 5
            print(self.bal)
        return self
    def display_account_info(self):
        print("Balance:", self.bal)
        return self
    def yield_interest(self):
        if (self.bal > 0):
            self.bal *= self.ir
        return self

jacob = BankAccount(500)
avery = BankAccount(250)

jacob.deposit(100).deposit(150).deposit(75).withdraw(50).yield_interest().display_account_info()
avery.deposit(200).deposit(345).withdraw(65).withdraw(30).withdraw(85).withdraw(50).yield_interest().display_account_info()