class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print("{} deposited to account name {}".format(amount, self.name))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        print("{} withdrawn to account name {}".format(amount, self.name))


account = Account("awes", 0)
account.deposit(1000)
print(account.balance)
account.withdraw(100)
print(account.balance)
