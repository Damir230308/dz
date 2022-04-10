# task 1

import re

Email = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def parse_email(email):
    found_info =  Email.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)
parse_email('adddr@gmail.com')

# task 2
from functools import wraps
def typelogger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper

@typelogger
def calc_cube(*args):
   return list(map(lambda x: x ** 3, args))

a = calc_cube(5, 20)
print(a)
