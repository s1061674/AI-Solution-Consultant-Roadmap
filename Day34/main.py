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
    def get_balance(self):
        return self.__balance

        
account = BankAccount(1000)

account.withdraw(-500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
