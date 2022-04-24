class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0


    def make_deposit(self, amount):

        self.balance += amount

        return self

    def make_withdraw(self, amount):

        self.balance -= amount

        return self

    def Greeting(self):
        print(f"Howdy My Name is {self.name}! I have ${self.balance} in my account.")

#Did not work but attempted for a bit
    #def transfer(self, other_user, amount):
        #self.balance - amount
        #other_user + amount



Brody = User("Brody", "12345")
Brynn = User("Brynn", "ABCDE")
Jett = User("Jett", "Password")
Sage = User("Sage", "123ABC")

Brynn.make_deposit(1000).make_deposit(1000).make_deposit(777).make_withdraw(250).Greeting()
Brody.make_deposit(10).make_deposit(100).make_withdraw(25).make_withdraw(40).Greeting()
Sage.make_deposit(420).make_withdraw(69).make_withdraw(69).make_withdraw(69).Greeting()

#Brody.transfer(Brynn, 100)