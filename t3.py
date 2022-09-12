"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
import collections
import timeit
lst = ['23', '22', '21']
deque_vs_lst = collections.deque('231')
def list_class():
    for i in lst:
        lst.append(i)
        print(lst)
        break
    for i in lst:
        lst.pop()
        print(lst)
        break
    for i in lst:
        lst.extend(i)
        print(lst)
        break
def deque_class():
    for i in lst:
        deque_vs_lst.append(i)
        print(deque_vs_lst)
        break
    for i in lst:
        deque_vs_lst.pop()
        print(deque_vs_lst)
        break
    for i in lst:
        deque_vs_lst.extend(i)
        print(deque_vs_lst)
        break
def deque_class2():
    for i in lst:
        deque_vs_lst.appendleft(i)
        print(deque_vs_lst)
        break
    for i in lst:
        deque_vs_lst.popleft()
        print(deque_vs_lst)
        break
    for i in lst:
        deque_vs_lst.extendleft(i)
        print(deque_vs_lst)
        break
def index_list():
    for i in lst:
        print(lst[0])
        break
def index_deque():
    for i in deque_vs_lst:
        print(deque_vs_lst[0])
        break

print(timeit.Timer(stmt='list_class', setup='list_class', globals=globals()).timeit(number=10000))
print(timeit.Timer(stmt='deque_class', setup='deque_class', globals=globals()).timeit(number=10000))
print(timeit.Timer(stmt='deque_class2', setup='deque_class2', globals=globals()).timeit(number=10000))
print(timeit.Timer(stmt='index_list', setup='index_list', globals=globals()).timeit(number=10000))
print(timeit.Timer(stmt='index_deque', setup='index_deque', globals=globals()).timeit(number=10000))
"""
1) Операции append, pop, extend:
0.00011999999999999858 - список

0.00012090000000000017 - deque
Оказалось что список чуть быстрее по сравнению деком.
------------------------------------------------------------------------------------------------------------------------
2) Операции к деку(appendleft, extendleft, popleft) и списку(append, pop, extend) по факту одни и те же операции.

0.00012979999999999936 - list

0.00012190000000000117 - deque
И в этом случае дек быстрее чем список.
------------------------------------------------------------------------------------------------------------------------
3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее.
получение по индексу:

0.00011989999999999917 - list

0.0001497000000000026 - deque

Дек медленнее чем список.

Вывод: Документация врать не может т.к дек и список. 
Из документации:

Вот основное правило: 
если вам нужно. Что-то быстро дописать или вытащить, используйте deque. Если вам нужен быстрый случайный доступ, 
используйте list.
Список используется для быстрого доступа к элементами, а в дек можно быстрее записать это показали (если верить) числа
в timeit'e 
"""
