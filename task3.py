
"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def my_revers(num):
    num1 = str(num)
    for el in reversed(num1):
        return el
revers(30)
revers_2(30)
revers_3(30)
my_revers(30)
print(timeit.timeit("revers(30)", "from __main__ import revers", number=10000))
print(timeit.timeit("revers_2(30)", "from __main__ import revers_2", number=10000))
print(timeit.timeit("revers_3(30)", "from __main__ import revers_3", number=10000))
print(timeit.timeit("my_revers(30)", "from __main__ import my_revers", number=1000))

"""
0.0035218000000000003 - revers
0.002515200000000002 - revers_2
0.0020464000000000003 - revers_3
0.00024180000000000035 - my_revers
Вывод: быстрее всех судя по цифрам мой способ с применением ф-ции reversed, на втором месте: срез,
на третьем: цикл while, ну и самый медленный это рекурсия(если я не ошибся на счёт метода),
потому что есть базовый случай(если введён ноль) и шаг рекурсии(если введено другое число).
1) ф-ция reversed
2) срез
3) цикл while
4) рекурсия
"""
