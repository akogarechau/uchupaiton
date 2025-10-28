"""
ex2.py

Код для решения второго практического задания

Основные возможности:
    1. Позволяет каждому транспортному средству возвращать собственное описание 
"""

class Vehicle:
    
    def __init__(self, name: str, weight: int, price: int):
        """
        Инициализация транспорта

        Args:
            name (str): марка
            weight (int): масса
            price (int): цена
        """        
        self.name = name
        self.weight = weight
        self.price = price

    def info(self) -> str:
        """
        поллучение информации о транспорте

        Returns:
            str: информация о транспорте
        """        
        return(
                f'{self.name}:'
                f'Масса - {self.weight}'
                f'Цена - {self.price}'
            )
        
class Air_Vehicle(Vehicle):
    
    def __init__(self, name: str, weight: int, price: int):
        """
        Инициализация воздушного транспорта

        Args:
            name (str): модель
            weight (int): масса
            price (int): цена в млн. долларов
        """        
        super().__init__(name, weight, price)
        
    def info(self) -> str:
        """
        Получение информации о воздушном транспорте

        Returns:
            str: информация о водушном транспорте
        """        
        return(
                f'{self.name}:\n'
                'Воздушный траспорт\n'
                f'Масса - {self.weight} т.\n'
                f'Цена - {self.price} млн. долларов\n'
                )
        
class Ground_Vehicle(Vehicle):
    
    def __init__(self, name: str, weight: int, price: int):
        """
        Инициализация наземного транспорта

        Args:
            name (str): модель
            weight (int): масса
            price (int): цена
        """        
        super().__init__(name, weight, price)
        
    def info(self) -> str:
        """
        Получение иформации о наземном транспорте

        Returns:
            str: информация о наземном транспорте
        """        
        return(
                f'{self.name}:\n'
                'Наземный траспорт\n'
                f'Масса - {self.weight} т.\n'
                f'Цена - {self.price} тыс. долларов\n'
                )

class Water_Vehicle(Vehicle):
    
    def __init__(self, name: str, weight: int, price: int):
        """
        Инициализация водного транспорта

        Args:
            name (str): марка
            weight (int): масса
            price (int): цена
        """        
        super().__init__(name, weight, price)
        
    def info(self) -> str:
        """
        Получение информации о водном транспорте

        Returns:
            str: информация о водном траспорте
        """        
        return(
                f'{self.name}:\n'
                'Водный траспорт\n'
                f'Масса - {self.weight} т.\n'
                f'Цена - {self.price} млн. долларов\n'
                )
        
def get_info(vehicle):
    return vehicle.info()

vehicle1 = Air_Vehicle('Пассажирский самолет', 340.4, 39.7)
vehicle2 = Ground_Vehicle('4х местный автомобиль', 2.3, 18.3)
vehicle3 = Water_Vehicle('Пассажирское судно', 520.9, 41.1)

print(get_info(vehicle1))
print(get_info(vehicle2))
print(get_info(vehicle3))

vehicle2.info()