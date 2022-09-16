import cProfile
from memory_profiler import profile

@profile
def wrapper():
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

wrapper()

"""
Без профилирования - Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     20.5 MiB     20.5 MiB          97   @profile
     5                                         def func_rec(n):
     6     20.5 MiB      0.0 MiB          97       if n == 1:
     7     20.5 MiB      0.0 MiB           1           return n
     8                                             else:
     9     20.6 MiB      0.0 MiB          96           return func_rec(n - 1) + n
     
С профилированием - Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.6 MiB     19.6 MiB           1   @profile
     5                                         def wrapper():
     6     19.7 MiB      0.1 MiB         101       def func_rec(n):
     7     19.7 MiB      0.0 MiB         100           if n == 1:
     8     19.7 MiB      0.0 MiB           1               return n
     9                                                 else:
    10     19.7 MiB      0.0 MiB          99               return func_rec(n - 1) + n
"""
