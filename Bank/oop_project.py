from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")
print("Done".center(20, "-"))
Dave.transfer(500, Sara)
