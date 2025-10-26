"""
ex2.py 

Код для решение второго практического задания: 'Олимпиада'

Основные возможности:
- Определяет позицию из полученного балла
- Определяет, вошел ли пользователь в топ 3
"""

from random import randint

# генерируем список студентов, иммитируя полученный с сайта список
student_scores = []
amount_of_student = 42
repeats = 0
for student_position in range(1,amount_of_student+1+repeats):
    score = randint(1, 100)
    
    # по условию задачи все оценки разные, проверяем это
    if score not in student_scores: 
        student_scores.append(score)
    else:
        repeats += 1 #т.к при повторении оценки она не добавлется в список (для сохранение кол-ва студентов)

# задаем позицию пользователя, иммитируя то, что пользователь знает сколько получил баллов (позицию в списке)
user_position = int(input('напишите вашу позицию в списке оценок: ')) 
# предополагается что список оценок отсоритрован по фамилиям (от А до Я)

def check_winners(scores: list, student_score: int):
    """
    Выводит ответ на вопрос - попал пользователь в топ 3 или нет

    Args:
        scores (list): список оценок студентов
        student_score (int): оценка пользователя
    """
    
    # поверяем попал ли студент в топ 3   
    if student_scores[user_position - 1] in sorted(student_scores, reverse=True)[:3]:
        print('Вы в тройке победителей!')
    
    else:
        print('Вы не попали в тройку победителей.')

check_winners(student_scores, user_position)