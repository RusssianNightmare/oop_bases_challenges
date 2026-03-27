"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

# код писать тут
class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount

class CreditAccount(BankAccount):
    def __init__(self, owner_full_name: str, balance: float):
        super().__init__(owner_full_name, balance)
    def increase_balance(self, amount: float):
        super().increase_balance(amount)
        return self.balance
    def decrease_balance(self, amount: float):
        super().decrease_balance(amount)
        return self.balance
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    user = CreditAccount("Artem", 10525.25)
    print(user.increase_balance(1000))
    print(user.decrease_balance(5000))
    print(user.is_eligible_for_credit())
