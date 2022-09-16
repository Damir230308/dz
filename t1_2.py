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
Это файл для второго скрипта
"""

import random
import timeit
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def wrapper():
    def lst(my_list):
        for _ in range(len(my_list)):

            element = my_list.pop(0)

            if element.isdigit():
                my_list.extend(['"', '{:02}'.format(int(element)), '"'])

            elif element[0] == '+' and element[1].isdigit():
                my_list.extend(['"', '{:02}'.format(int(element)), '"'])

            else:
                my_list.append(element)
def lst1(my_list):
    for _ in range(len(my_list)):

        element = my_list.pop(0)

        if element.isdigit():
            my_list.extend(['"', '{:02}'.format(int(element)), '"'])

        elif element[0] == '+' and element[1].isdigit():
            my_list.extend(['"', '{:02}'.format(int(element)), '"'])

        else:
            my_list.append(element)

# print(' '.join(my_list))
# print(' '.join(my_list))

print(timeit.timeit('wrapper', 'from __main__ import wrapper', number=100000))
print(timeit.timeit('lst1', 'from __main__ import lst1', number=100000))

"""
Замеры:
---------------------------------------------------------------------------------------------------------
0.0008856999999999997 - оптимизированный код
---------------------------------------------------------------------------------------------------------
0.0008867000000000024 - неоптимизированный код
---------------------------------------------------------------------------------------------------------

Что было сделано для оптимизации: Я решил обернуть ф-цию lst другой ф-цией wrapper,
и результаты стали лучше.
"""
