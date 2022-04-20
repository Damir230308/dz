# task 1

class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)
    @classmethod
    def reduction_to_a_number(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)
        return int(date[0]), int(date[1]), int(date[2])
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2000 <= year <= 3000:
                    return f'Все данные введены корректно :)'
                else:
                    return f'Неправильно введен день!'
            else:
               return f'Неправильно введен месяц!'
        else:
           return f'Неправильно введён год!'
    def __str__(self):
        return f'Текущая дата {Data.reduction_to_a_number(self.day_month_year)}'
today = Data('21 - 10 - 2100')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.reduction_to_a_number('12 - 5 - 2045'))
print(today.reduction_to_a_number('25 - 7 - 3000'))
print(Data.valid(1, 11, 2222))


# task 2

class Exception1(Exception):
    def __init__(self, num, num2):
        self.num = num
        self.num2 = num2
    def checking(self):
        try:
            num_exit = self.num / self.num2
            print(round(num_exit))
            if num_exit == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('На ноль делить нельзя! Учи математику!')
exception = Exception1(10, 5)
exception.checking()

# task 3

class Error:
    def __init__(self, *args):
        self.input = []
    def list_all_nums(self):
        while True:
            try:
                new_num = int(input('Вводите значение: '))
                self.input.append(new_num)
                print(f'Список сейчас: {self.input}')
            except:
                if new_num == type(str) or type(bool):
                    print('Неправильно введено значение!')
                    exit(1)
try_except = Error()
try_except.list_all_nums()

# task 4

class OfficeEquipment:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.warehouse1 = []
    def warehouse(self, *args):
        try:
            print(f'Поступило на склад: {self.name}, цена: {self.price}, количество: {self.quantity}')
            quantity_in_warehouse = f'{self.name}, цена: {self.price}, количество: {self.quantity}'
            self.warehouse1.append(quantity_in_warehouse)
            print(f'Сейчас на складе: {self.warehouse1}')
        except:
            return f'Неправильно введены данные!'
class Scanner(OfficeEquipment):
    def scanning(self):
        print(f'Сканирует: {self.name}')
class Printer(OfficeEquipment):
    def print(self):
        print(f'Печатает про: {self.name}')
class Xserox(OfficeEquipment):
    def xsero_copy(self):
        print(f'Копирует данные об: {self.name}')
off = OfficeEquipment('Принтер', 10000, 1)
off.warehouse()
scan = Scanner('Принтер', 10000, 1)
scan.scanning()
printer = Printer('Принтер', 10000, 1)
printer.print()
xserox = Xserox('Принтер', 10000, 1)
xserox.xsero_copy()
# task 5
import math


class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)


print(complex(1, 2)+complex(2, 3))
print(complex(1, 2)*complex(2, 3))
