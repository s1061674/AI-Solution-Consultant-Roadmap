class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            print("正常存款")
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            print("正常扣款")
            self.__balance -= amount
        else:
            print("Invalid withdraw amount")
    @property
    def balance(self):
        return self.__balance

        
account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)
print(account.balance)
