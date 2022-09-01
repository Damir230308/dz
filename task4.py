def recur(number, i, n, common_sum):
    if i == n:
        print(f'Sum of the elements: {common_sum}')
    if i < n:
        return recur(i + 1, number / 2 * -1, n, common_sum+number)
try:
    n = int(input("Count of elements: "))
    recur(0, 1, n, 0)
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")
