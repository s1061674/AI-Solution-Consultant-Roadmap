class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("餘額不能小於 0")
        else:
            self.__balance = value

account = BankAccount("HCK", 1000)


print(f"Owner: {account.owner}")
print(f"Balance: {account.balance}")

account.balance = 1500
print(f"Balance: {account.balance}")

try:
   account.balance = -500
except ValueError as e:
     print(e)

print(f"Balance: {account.balance}")