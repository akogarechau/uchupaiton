"""
ex1.py

Код для решения первого практического задания

Основные возможности:
    1. Расчет зарплаты на основе различных критериев класса
"""

from math import floor

class Employee:    
    
    def __init__(self, expirience: int, working_hours: int =168, penalties: int =0):
        """
        Инициализация сотрудника

        Args:
            expirience (int): опыт работы (смысл тот же, что и разделение на junior/middle/senior).
            working_hours (int, optional): кол-во рабочих часов сотружника в месяц. Defaults to 168.
            penalties (int, optional): кол-во штрафов. Defaults to 0.
        """        
        self.expirience = expirience
        self.working_hours = working_hours
        self.penalties = penalties
        
        def info():
            pass
        
class Manager(Employee):
    
    def __init__(self, expirience: int, working_hours: int =168, penalties: int =0, subordinates: int =5):
        """
        Инициализация менеджера

        Args:
            expirience (int): опыт работы (смысл тот же, что и разделение на junior/middle/senior).
            working_hours (int, optional): кол-во рабочих часов сотружника в месяц. Defaults to 168.
            penalties (int, optional): кол-во штрафов. Defaults to 0.
            subordinates (int, optional): кол-во подчиненных. Defaults to 5.
        """        
        super().__init__(expirience, working_hours, penalties)
        self.subordinates = subordinates
       
        
    def payroll(self) -> int:
        """
        Подсчет зарплаты менеджера

        Returns:
            int: зарплата в рублях
        """        
        return floor(1200 * (1.15 if self.expirience == 2 else 1.25 if self.expirience == 3 else 1))\
            * self.working_hours + (2500 * (self.subordinates - 5))

class Developer(Employee):
    
    def __init__(self, expirience: int, working_hours: int =168, penalties: int =0, outworker: int =0):
        """
        Инициализация разработчика

        Args:
            expirience (int): опыт работы (смысл тот же, что и разделение на junior/middle/senior).
            working_hours (int, optional): кол-во рабочих часов сотружника в месяц. Defaults to 168.
            penalties (int, optional): кол-во штрафов. Defaults to 0.
            outworker (int, optional): работает ли разработчик на удаленке или нет. Defaults to 0.
        """        
        super().__init__(expirience, working_hours, penalties)
        self.outworker = outworker
        
    def payroll(self) -> int:
        """
        Подсчет зарплаты разработчика

        Returns:
            int: зарплата в рублях
        """        
        return floor(1300 * (1.15 if self.expirience == 2 else 1.25 if self.expirience == 3 else 1))\
            * self.working_hours + (5000 * (not self.outworker))
            
employee1 = Manager(1)
employee2 = Developer(2)

print(employee1.payroll())
print(employee2.payroll())