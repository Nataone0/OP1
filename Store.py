# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также
# существуют общие характеристики, такие как адрес, название
# и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
#  Шаги:
#  1. Создай класс Store:
#  -Атрибуты класса:
#  name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара,
# а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
#  __init__ - конструктор, который инициализирует н
#  азвание и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию.
# Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными
# названиями, адресами и добавь в каждый из них несколько товаров.

class Store:
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        return self.items.get(name, None)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price

    def info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Items: {self.items}")


store1 = Store("Market 1", "Adress 1", {'apples': 0.5, 'bananas': 0.75})
store2 = Store("Market 2", "Adress 2", {'oranges': 0.6, 'pineapples': 0.8})
store3 = Store("Market 3", "Adress 3", {'grapes': 0.7, 'strawberries': 0.9})

store1.add_item("oranges", 0.6)
store2.add_item("pineapples", 0.8)
store3.add_item("strawberries", 0.9)
store1.update_price("oranges", 0.65)
store2.update_price("pineapples", 0.85)
store3.update_price("strawberries", 0.95)

store1.info()
store2.info()
store3.info()

store2.remove_item("pineapples")
store3.remove_item("strawberries")

store1.info()
store2.info()
store3.info()
