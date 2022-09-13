"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import collections
import timeit
dict = {
    '3': 'd',
    '4': '3'
}

ordered_dict = collections.OrderedDict()
ordered_dict.__dict__ = {
    '1': '2',
    '2': '3'
}
def dict_common():
    dict.pop('3')
    dict.get('4')
    dict.keys()

def ordered_dict():
    ordered_dict.get('1')
    ordered_dict.pop('2')
    ordered_dict.keys()

print(timeit.Timer(stmt='dict_common', setup='dict_common', globals=globals()).timeit(number=10000))
print(timeit.Timer(stmt='ordered_dict', setup='ordered_dict', globals=globals()).timeit(number=10000))

"""
Полученные рез-ты:
0.00014310000000000017 - обычный словарь
0.00015189999999999995 - OrderedDict
По факту OrderedDict ненамного медленнее чем обычный словарь, но всё же словарь быстрее. Я провёл одинаковые операции с
ними обоими.
Выводы: OrderedDict медленнее чем обыч словарь, однако он всё ещё может пригодится в коде, потому что раньше до Python
3.6 была проблема с упорядоченностью нашего словаря (dict) поэтому и использовали OrderedDict. Чтобы упорядочить его
Ситуация изменилась с приходом Python 3.6. Встроенный класс dict теперь сохраняет упорядоченность своих элементов. 
В связи с этим многие в сообществе Python задаются вопросом, а нужен ли теперь OrderedDict или нет. Ответ очевиден 
конечно же да, потому что OrderedDict предоствляет очень большой функционал в коде.
"""
