import os 
os.chdir(os.path.dirname(__file__))
def homework_view(lesson):
    with open (f'{lesson}.txt', 'r') as file:
        content = file.read()
        print(content)


who_are_you = int(input('Если Вы ученик введите - 1. Если Вы учитель введите - 2: '))
if who_are_you == 1:
    num = int(input("Выберите предмет: \n английский - 1 \n математика - 2 \n русский - 3 \n"))
    if num == 1:
        lesson = 'английский'
    elif num == 2:
        lesson = 'математика'
    elif num == 3:
        lesson = 'русский'
    homework_view(lesson)
