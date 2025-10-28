"""
ex4.py

Код для решения четвертого практического задания

Основные возможности:
    Симулятор космического корабля:
        1. CrewMember контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
        2. SpaceShip имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
        3. Mission определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
"""

from random import choice, randint
class CrewMember:
    
    def __init__(self, name: str, age: int, role: str, alive: bool, skills: list, hp: int):
        
        self.name = name
        self.age = age
        self.role = role
        self.alive = alive
        self.skills = skills
        self.hp = hp
            
class SpaceShip:
    
    def __init__(self, name: str, speed: int, fuel: int =350, hull_status: int =100, successful_mission: Mission =list):
        
        self.name = name
        self.speed = speed
        self.fuel = fuel
        self.hull_status = hull_status
        self._storage = []
        self.succesful_mission = successful_mission
        self.members: list[CrewMember] = list()
        
        if self.hull_status > 100:
            self.hull_status == 100
    
    def speed_change(self, number: int):
        
        self.speed += number
        
    def fuel_change(self, number: int):
        
        self.fuel += number
            
    def add_member(self, new_member: CrewMember) -> None:
        
        self.members.append(new_member)
        
    def remove_member(self, member_index: int) -> None:
        
        self.members.pop(member_index)

    def hull_damage(self, damage) -> str:
        
        self.hull_status -= damage
        print(
                f'Кораблю нанесен урон - {damage}%\n'
                f'Текущее хп корабля - {self.hull_status}%\n'
              )
        if self.hull_status < 1:
            print('GAME OVER GAME OVER GAME OVER GAME OVER GAME OVER GAME OVER')
            
    def hull_repair (self, amount) -> None:
        flag = 0
        print(
                f'Попытка ремонта на {amount}%'
        )
        for member in self.members:
            
            if member.role == 'Инженер':
                self.hull_status += amount
                flag = 1
                
                if self.hull_status > 100:
                    self.hull_status = 100
                    
                print(
                    f'Успешно произведена починка корабля до {self.hull_status}%\n'
                )
            if flag == 0:
                print(
                f'Починка корабля не удалась!\n'
            )
                    
    def add_resourse(self, resourses: str, amount: int =1) -> None:
        
        self._storage.append([resourses, amount])
        
    def storage_info(self) -> list:
        
        for [resourse, amount] in self._storage:
            print([resourse, amount])
        
    def role_check(self, needed_role: str) -> bool:
        
        for member in self.members:

            if member.role == needed_role:
                
                return True
            
        return False
    
    def info(self) -> str:
        
        return(
            f'Корабль - {self.name}\nСостояние корабля - {self.hull_status}%\n'
            f'Его скорость - {self.speed} св.ч/д, запас топлива - {self.fuel} Мт.\n'
        )
        
    def member_info(self) ->str:
        
        print('Члены Команды:\n')
        for member in self.members:
            
            print(
                f'{member.name}\nРоль - "{member.role}", возраст - {member.age}\n'
                f'ХР - {member.hp}, Статус - {"ЖИВ" if member.alive else "МЕРТВ"}\n'
                f'{member.skills[1]}'
                '\n'
            )

class Mission:
    
    def __init__(
                self, name: str, 
                goal: str, 
                events: list, 
                resourses: list,
                needed_role: str,
                status: bool =False
                ):
        
        self.name = name
        self.goal = goal
        self.events = events
        self.resourses = resourses
        self.status = status
        self.needed_role = needed_role
        
    def start_mission(self, space_ship: SpaceShip):
        
        space_ship.fuel_change(randint(-25, -10))
        if self.status == False:
            
            current_event = choice(self.events)
            print(
                f'{self.name} - текущее задание\n'
                f'"{current_event[0]}" - событие предстоящее команде\n'
                f'{current_event[1]}% - прогнозируемый урон\n'            
            )
            if space_ship.hull_status > current_event[1] and space_ship.role_check(self.needed_role):
                
                print(
                    f'"{current_event[0]}" - успешно преодолен\n'
                    f'Задание успешно выполнено'
                )
                space_ship.hull_damage(current_event[1])
                space_ship.add_resourse(choice(self.resourses), 2)
                
            else:
                space_ship.hull_damage(current_event[1]*3)
        else: 
            pass


Engineer = CrewMember('Делл Конагер', 47, 'Инженер', True, ['Чинить корабль', '"Ему нравится мастерить вещи"'], 100)
Captain = CrewMember('Камина Дзиха', 42, 'Капитан', True, ['Командовать', '"Его невозможно остановить"'], 100)
space_ship1 = SpaceShip('"ПОБЕДИТЕЛЕЙ"', 350)
space_ship1.add_member(Engineer)
space_ship1.add_member(Captain)
print(space_ship1.info())
print(space_ship1.member_info())
new_mission = Mission('Защита Нибиру', 'Успешно защитить Нибиру',\
    [['Дождь из манадаринов', 50],['Атака мандариновцев', 25], ['План: Linux', 99]],\
    [['Компьютер на Linux'],['Техника вненибирской расы'], ['Оружее вненибирской расы']],\
        'Капитан')

new_mission.start_mission(space_ship1)
space_ship1.hull_repair(25)
print(space_ship1.info())
