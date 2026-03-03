class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\nAccount '{self.acctName}' created.\nBalance = {self.balance}")

    def getbalance(self):
        print(f"\nAccount '{self.acctName}' balance is: {self.balance}")

    def debit(self):
        amount = int(input("how much to add:\t"))
        self.balance += amount
        print(f"\nusername: {self.acctName} has added {amount}, total is {self.balance}")

    def credit(self):
        amount = int(input("how much money you want:\t"))
        if self.balance < amount:
            print("\nYou don't have enough money!")
        else:
            self.balance -= amount
            print(f"\nusername: {self.acctName} has taken {amount}, total is {self.balance}")
            self.getbalance()

    def transfer(self, amount, accountName):
        print(f"your account name is: {self.acctName} and its balance is: {self.balance}")
        self.credit()
        accountName.debit()
