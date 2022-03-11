print('Внимание! Чтобы пользоваться программой необходимо знать английский язык и вводить числа от 1 до 10!')
number = (input('Введите число, которое хотите перевести (по английски): '))

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
