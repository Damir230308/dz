"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для первого скрипта
"""
import cProfile
from memory_profiler import profile

# --------------------------------------------------------------------------------------------------
# Оптимизированный код
@profile
def wrapper():
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
@profile
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
cProfile.run(wrapper())
# --------------------------------------------------------------------------------------------------
"""
Неоптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     19.6 MiB     19.6 MiB           1   @profile
    49                                         def game(count, number, max_count):
    50     19.6 MiB      0.0 MiB           1       user_number = int(input('Ваше число: '))
    51     19.6 MiB      0.0 MiB           1       print(f'experience number: {count}')
    52     19.6 MiB      0.0 MiB           1       if count == max_count:
    53     19.6 MiB      0.0 MiB           1           print(f'You lose. Final num - {number}')
    54     19.6 MiB      0.0 MiB           1           if user_number == number:
    55                                                     print(f'You won! Congratulations, the original number: {number}')
    56                                                     exit(0)
    57                                             else:
    58                                                 if user_number > number:
    59                                                     print('Your number is bigger than the one you made')
    60                                                 else:
    61                                                     print('Your number is less than the one you made')
    62                                                 game(count + 1, number, 10)
------------------------------------------------------------------------------------------------------------------------
Оптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    30     19.5 MiB     19.5 MiB           1   @profile
    31                                         def wrapper():
    32     19.5 MiB      0.0 MiB           1       def game1(count, number, max_count):
    33                                                 user_number = int(input('Ваше число: '))
    34                                                 print(f'experience number: {count}')
    35                                                 if count == max_count:
    36                                                     print(f'You lose. Final num - {number}')
    37                                                     exit(0)
    38                                                     if user_number == number:
    39                                                         print(f'You won! Congratulations, the original number: {number}')
    40                                                         exit(0)
    41                                                 while count != max_count:
    42                                                     if user_number > number:
    43                                                         print('Your number is bigger than the one you made')
    44                                                     else:
    45                                                         print('Your number is less than the one you made')
    46                                                     game1(count + 1, number, 10)
------------------------------------------------------------------------------------------------------------------------
Что было сделано для оптимизации: Я решил заменить рекурсию на цикл и обернуть ф-цию game1 внешней ф-цией wrapper 
это помогло улучшить результат.
Было: 19.6 MiB
Стало: 19.5 MiB
"""
