"""
ex3.py

Код для решения третьего практического задания

Основные возможности:
    1. Позволяет каждому транспортному средству возвращать собственное описание 
"""

class Product:
    
    def __init__(self, name: str, category: str, price: int, in_stock: int):
        
        self.name = name
        self.category = category
        self.price = price
        self.in_stock = in_stock
        
class Customer:
    
    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        self._orders = list()

    @property
    def orders_history(self) -> list:
        
        return [order.total() for order in self._orders]
    
    def add_order(self, order: Order) -> None:
        
        self._orders.append(order)

class Order:
    
    def __init__(self, shopping_cart: Shopping_cart, tax, discount):
        
        self.shopping_cart = shopping_cart
        self.tax = tax
        self.discount = discount

    def total(self):
        
        return round(self.shopping_cart.total() * 100 / (100 - self.tax) * (100 - self.discount) / 100, 2)
        
class Shopping_cart:
    
    def __init__(self):
        
        self._cart: list[Product] = list()

    @property    
    def cart_info(self) -> list:
        
        return [[product.name, amount] for [product, amount] in self._cart]
    
    def add_product(self, product: Product, amount) -> None:
        
        if product.in_stock:
            self._cart.append([product, amount])
            
    def remove_product(self, product_index: Product) -> None:
        
        self._cart.pop(product_index)
        
    def total(self) -> int:
        
        return sum(product.price * amount for [product, amount] in self._cart)
    
milk = Product('Молоко 3,2%', 'Молочная продукция', 106, True)
cherry_juice = Product('J7 Вишня', 'Напитки', 145, True)
customer = Customer('Иван', 20)
cart = Shopping_cart()
cart.add_product(milk, 2)
cart.add_product(cherry_juice, 1)
order = Order(cart, 20, 15)
print('Заказ -', cart.cart_info)
print('Сумма продуктов -', cart.total())
print('Стоимость заказа -', order.total())
print('')
customer.add_order(order)
cart2 = Shopping_cart()
cart2.add_product(milk, 1)
cart2.add_product(cherry_juice, 3)
order2 = Order(cart2, 20, 0)
customer.add_order(order2)
print('Заказ -', cart2.cart_info)
print('Сумма продуктов -', cart2.total())
print('Стоимость заказа -', order2.total())
print('История заказов -', customer.orders_history)