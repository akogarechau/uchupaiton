"""
ex3.py

Код для решения третьего практического задания

Основные возможности:
    • Реализация онлайн-магазина:
        1. Создайте модель для онлайн-магазина с
            классами Product, Order, Customer, и
            ShoppingCart.
        2. Product включает информацию о цене, наличии
            на складе и категории товара. Order
            обрабатывает процесс покупки, включая расчет
            цены с учетом скидок и налогов.
        3. Customer управляет информацией о пользователе
            и его истории заказов.
        4. ShoppingCart позволяет добавлять, удалять и
            обновлять количество товаров перед
            оформлением заказа.
"""

class Product:
    
    def __init__(self, name: str, category: str, price: int, in_stock: int):
        """
        Инициализация продукта

        Args:
            name (str): название
            category (str): категория
            price (int): цена
            in_stock (int): налицие в магазине
        """        
        self.name = name
        self.category = category
        self.price = price
        self.in_stock = in_stock
        
class Customer:
      
    def __init__(self, name: str, age: int):
        """
        Инициализация покупателя

        Args:
            name (str): имя
            age (int): возраст
            _orders (list): список заказов
        """        
        self.name = name
        self.age = age
        self._orders = list()

    def add_order(self, order: Order) -> None:
        """
        добавление заказа в историю

        Args:
            order (Order): заказ
        """        
        self._orders.append(order)
        
    @property
    def orders_history(self) -> list:
        """
        Получение истории заказов пользователя

        Returns:
            list: история заказов, их стоимость
        """        
        return [order.total() for order in self._orders]

class Order:
    
    def __init__(self, shopping_cart: Shopping_cart, tax, discount):
        """
        Инициализация заказа

        Args:
            shopping_cart (Shopping_cart): корзина
            tax (_type_): налог
            discount (_type_): скидка
        """        
        self.shopping_cart = shopping_cart
        self.tax = tax
        self.discount = discount

    def total(self) -> int:
        """
        получение суммы заказа с учетом скидки и налога 

        Returns:
            int: сумма заказа с учетом скидки и налога
        """        
        return round(self.shopping_cart.total() * 100 / (100 - self.tax) * (100 - self.discount) / 100, 2)
        
class Shopping_cart:
    
    def __init__(self):
        """
        Инициализация корзины с товарами
        
        Args:
            _cart (list): корзина
        """         
        self._cart: list[Product] = list()
    
    @property    
    def cart_info(self) -> list:
        """
        Выводит список продуктов находящихся в корзине

        Returns:
            list: список продуктов находящихся в корзине
        """        
        return [[product.name, amount] for [product, amount] in self._cart]
    
    def add_product(self, product: Product, amount: int) -> None:
        """
        Добавлет продукт в корзину

        Args:
            product (Product): выбранный продукт
            amount (int): кол-во выбранного продукта
        """        
        if product.in_stock:
            self._cart.append([product, amount])
            
    def remove_product(self, product_index: Product) -> None:
        """
        Удаление продукта из корзины

        Args:
            product_index (Product): Позиция продукта в корзине
        """        
        self._cart.pop(product_index)
        
    def total(self) -> int:
        """
        Получение суммы цен всех продуктов с учетом кол-ва каждого выбраного продукта

        Returns:
            int: сумма цен всех продуктов с учетом кол-ва каждого выбраного продукта
        """        
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