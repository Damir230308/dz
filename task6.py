"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random
def game(count, number, max_count):
    user_number = int(input('Ваше число: '))
    print(f'experience number: {count}')
    if count == max_count:
        print(f'You lose. Final num - {number}')
        if user_number == number:
            print(f'You won! Congratulations, the original number: {number}')
            exit(0)
    else:
        if user_number > number:
            print('Your number is bigger than the one you made')
        else:
            print('Your number is less than the one you made')
        game(count + 1, number, 10)
game(1, random.randint(0, 100), 10)
