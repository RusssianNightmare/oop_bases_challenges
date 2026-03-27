"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance
    def balance_bank(self):
        return self.balance
    def increase_balance(self, income: float):
        self.income = income
        return self.balance + self.income

if __name__ == '__main__':
    bank = BankAccount("John", 10000.54)
    print(bank.balance_bank())
    print(bank.increase_balance(5252.24))
