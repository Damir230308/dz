# task 1

class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[4, 2], [3, 2], [5, 9], [7, 8]])
matrix_2 = Matrix([[6, 3], [4, 6], [1, 7], [10, 40]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)

# task 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)

# task 3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)
        # return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'РЇС‡РµРµРє РІ РїРµСЂРІРѕР№ РєР»РµС‚РєРµ РјРµРЅСЊС€Рµ РёР»Рё СЂР°РІРЅРѕ РІС‚РѕСЂРѕР№, РІС‹С‡РёС‚Р°РЅРёРµ РЅРµРІРѕР·РјРѕР¶РЅРѕ'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(10)
cell_2 = Cell(24)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(5))
