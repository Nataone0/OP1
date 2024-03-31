# Определить класс акаунт имитирующий банковский счет
# Атрибуты:
# - имя клиента
# - Баланс
# методы:
# - пополнение счета
# - снятие, если баланс больше нуля
# - информация о счете

class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your new balance: {self.balance}")
        else:
            print("Amount must be greater than 0")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You succeeded in withdrawal. Your new balance: {self.balance}")
        else:
            print("Insufficient funds")

    def all_balance(self):
        print(f"Name: {self.id}")
        print(f"Balance: {self.balance}")

man = Account("12322", 600)

man.deposit(100)
man.withdraw(800)
man.deposit(10000)
man.all_balance()