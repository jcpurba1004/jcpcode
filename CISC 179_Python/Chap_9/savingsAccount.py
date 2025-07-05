from bank import Bank
from savingsaccount import SavingsAccount
bank = Bank()
bank.add(SavingsAccount("Wilma", "1001", 4000.00))
bank.add(SavingsAccount("Fred", "1002", 1000.00))
print(bank)

account = bank.get("Wilma", "1000")
print(account)

account = bank.get("Wilma", "1001")
print(account)

print(bank)
