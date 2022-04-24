class BankAccount:
    Accounts = []
    def __init__(self, interest, balance): 
        self.interest = interest
        self.balance = balance
        BankAccount.Accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("Insufficent Funds Withdraw Declined")
        return self

    def display_account_info(self):
        return(f"Your balance is: {self.balance}")
        

    def interestrate(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest)
        return self

#Not sure what went wrong here
    @classmethod
    def printusers(cls):
        for account in cls.Accounts:
            account.display_account_info()


class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,3000)
        }
        

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

adrien = User("Brody")

adrien.account['checking'].deposit(100)
adrien.display_user_balance()
