"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

# ООП

class OperationHex():
    def __init__(self, f_num, s_num):
        self.f_num = f_num
        self.s_num = s_num
    def __add__(self, other):
        return list(hex(int(''.join(self.f_num), 16) + int(''.join(other.s_num))))
    def __mul__(self, other):
        return list(hex(int(''.join(self.f_num), 16) * int(''.join(other.s_num))))[2:]

first_number = list(input('Введите первое шестнадцатиричное число: '))
second_number = list(input('Введите второе шестнадцатиричное число: '))

result_sum = OperationHex(first_number, second_number) + OperationHex(first_number, second_number)
result_multiplication = OperationHex(first_number, second_number) * OperationHex(first_number, second_number)

print(f'Сумма:{result_sum}. Произведение:{result_multiplication}')
