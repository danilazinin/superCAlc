import os

os.chdir(os.path.dirname(__file__))

def homework_adding(teacher, lesson):
    homework = input(f'{teacher} введите новое домашнее задание по {lesson}: ')
    with open (f'{lesson}.txt', 'a') as file:
        file.write(f'{teacher}; {lesson}; {homework};\n')

homework_adding('руслан', 'математика')
