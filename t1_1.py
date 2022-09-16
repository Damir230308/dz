import random
import timeit
# --------------------------------------------------------------------------------------------------
# Оптимизированный код

def game1(count, number, max_count):
    user_number = int(input('Ваше число: '))
    print(f'experience number: {count}')
    if count == max_count:
        print(f'You lose. Final num - {number}')
        exit(0)
        if user_number == number:
            print(f'You won! Congratulations, the original number: {number}')
            exit(0)
    while count != max_count:
        if user_number > number:
            print('Your number is bigger than the one you made')
        else:
            print('Your number is less than the one you made')
        game1(count + 1, number, 10)
# --------------------------------------------------------------------------------------------------
# Неоптимизированный код
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
# --------------------------------------------------------------------------------------------------
print(timeit.timeit('game1', 'from __main__ import game1', number=100000))
print(timeit.timeit('game', 'from __main__ import game', number=100000))
# --------------------------------------------------------------------------------------------------
"""
0.0008850000000000004 - оптимизированный код
-------------------------------------
0.0008940000000000024 - неоптимизированный код

Что было сделано для оптимизации: Я решил заменить рекурсию на цикл и это в какой-то степени помогло
мне улучшить результат теста в timeit.
"""
