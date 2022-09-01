Решите через рекурсию. В задании нельзя применять циклы.
"""
def func_rec(n):
    if n == 1:
        return n
    else:
        return func_rec(n - 1) + n
try:
    n = int(input("Enter a number: "))
    if func_rec(n) == n * (n + 1) / 2:
        print('Equality is true')
except ValueError:
    print("You entered the string ((( instead of a number. Correct yourself")
