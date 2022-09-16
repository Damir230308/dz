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
