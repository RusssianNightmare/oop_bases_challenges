"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
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

    def reduce_balance(self, reduce: float):
        self.reduce = reduce
        current_balance = self.balance - self.reduce
        if current_balance < 0:
            raise ValueError('Отрицательный баланс!')
        return current_balance


if __name__ == '__main__':
    bank = BankAccount("John", 10000.54)
    print(bank.balance_bank())
    print(bank.increase_balance(5252.24))
    print(bank.reduce_balance(3254.56))
    print(bank.reduce_balance(15524.55))
