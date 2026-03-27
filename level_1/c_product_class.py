"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int | str, weight: int):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight
    def get_info_product(self):
        return f'Информация о продукте: {self.name}, {self.description}, {self.price} р., {self.weight} гр.'


if __name__ == '__main__':
    product = Product("Bananas", "They are yellow, from tropical countries, very tastye", 30, 100)
    print(product.get_info_product())
