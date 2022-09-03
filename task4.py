"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit
import collections

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def my_func():
    count_numbers = collections.Counter(array)
    print(f'Кол-во раз в массиве появлялось: {count_numbers[1]}')

print(func_1())
print(func_2())
my_func()

print(timeit.timeit("func_1()", "from __main__ import func_1", number=100000))
print(timeit.timeit("func_2()", "from __main__ import func_2", number=100000))
print(timeit.timeit("my_func", "from __main__ import my_func", number=100000))

"""
0.08939520000000001 - func_1
0.12460869999999999 - func_2
0.0008693000000000173 - my_func
При расчётах я брал 100 тысяч операций. У меня получилось ускорить задачу путём применения пакета collections, а именно
метода Counter. Пришлось поискать чтобы найти его. Но всё таки поставленная задача выполнена!
"""
