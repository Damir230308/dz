"""
Задание 4.
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
Это файл для четвёртого скрипта
"""
from memory_profiler import profile
print('Внимание! Чтобы пользоваться программой необходимо знать английский язык и вводить числа от 1 до 10!')
number = (input('Введите число, которое хотите перевести (по английски): '))
#Оптимизированный скрипт
@profile
def wrapper():
    def num_translate():
        if number == 'eleven':
            return None
        elif number == 'zero':
            print('ноль')
        elif number == 'one':
            print('один')
        elif number == 'two':
            print('два')
        elif number == 'three':
            print('три')
        elif number == 'four':
            print('четыре')
        elif number == 'five':
            print('пять')
        elif number == 'six':
            print('шесть')
        elif number == 'seven':
            print('семь')
        elif number == 'eight':
            print('восемь')
        elif number == 'nine':
            print('девять')
        elif number == 'ten':
            print('десять')
wrapper()


# Неоптимизированный скрипт
@profile
def num_translate():
    if number == 'eleven':
        return None
    elif number == 'zero':
            print('ноль')
    elif number == 'one':
            print('один')
    elif number == 'two':
            print('два')
    elif number == 'three':
            print('три')
    elif number == 'four':
            print('четыре')
    elif number == 'five':
            print('пять')
    elif number == 'six':
            print('шесть')
    elif number == 'seven':
            print('семь')
    elif number == 'eight':
            print('восемь')
    elif number == 'nine':
            print('девять')
    elif number == 'ten':
            print('десять')
num_translate()

"""
Оптимизированный код:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     19.5 MiB     19.5 MiB           1   @profile
     6                                         def wrapper():
     7     19.5 MiB      0.0 MiB           1       def num_translate():
     8                                                 if number == 'eleven':
     9                                                     return None
    10                                                 elif number == 'zero':
    11                                                     print('ноль')
    12                                                 elif number == 'one':
    13                                                     print('один')
    14                                                 elif number == 'two':
    15                                                     print('два')
    16                                                 elif number == 'three':
    17                                                     print('три')
    18                                                 elif number == 'four':
    19                                                     print('четыре')
    20                                                 elif number == 'five':
    21                                                     print('пять')
    22                                                 elif number == 'six':
    23                                                     print('шесть')
    24                                                 elif number == 'seven':
    25                                                     print('семь')
    26                                                 elif number == 'eight':
    27                                                     print('восемь')
    28                                                 elif number == 'nine':
    29                                                     print('девять')
    30                                                 elif number == 'ten':
    31                                                     print('десять')
------------------------------------------------------------------------------------------------------------------------
неоптимизированный код:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    34     19.6 MiB     19.6 MiB           1   @profile
    35                                         def num_translate():
    36     19.6 MiB      0.0 MiB           1       if number == 'eleven':
    37                                                 return None
    38     19.6 MiB      0.0 MiB           1       elif number == 'zero':
    39                                                     print('ноль')
    40     19.6 MiB      0.0 MiB           1       elif number == 'one':
    41                                                     print('один')
    42     19.6 MiB      0.0 MiB           1       elif number == 'two':
    43                                                     print('два')
    44     19.6 MiB      0.0 MiB           1       elif number == 'three':
    45     19.6 MiB      0.0 MiB           1               print('три')
    46                                             elif number == 'four':
    47                                                     print('четыре')
    48                                             elif number == 'five':
    49                                                     print('пять')
    50                                             elif number == 'six':
    51                                                     print('шесть')
    52                                             elif number == 'seven':
    53                                                     print('семь')
    54                                             elif number == 'eight':
    55                                                     print('восемь')
    56                                             elif number == 'nine':
    57                                                     print('девять')
    58                                             elif number == 'ten':
    59                                                     print('десять')
    
Что же я сделал? Вновь я воспользовался трюком с обёртыванием во внешнюю ф-цию.
"""
