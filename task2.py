def recur(numb, even=0, odd=0):
    if numb == 0:
        return even, odd
    else:
        cur_number = numb % 10
        cur_number // 10
        if cur_number % 2 == 0:
            even += 1
        else:
            odd += 1
        return recur(numb, even, odd)
try:
    number = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе: {recur(number)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")
