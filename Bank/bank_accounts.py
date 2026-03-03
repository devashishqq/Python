class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\nAccount '{self.acctName}' created.\nBalance = {self.balance}")

    def getbalance(self):
        print(f"\nAccount '{self.acctName}' balance is: {self.balance}")