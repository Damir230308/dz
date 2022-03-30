#task 1

def odd_nums(max_value):
    n = 1
    while n <= max_value:
        yield n
        n += 2
odd_to_15 = odd_nums(15)

#task 1.2

max_value = 3
odd_nums_gen = (n for n in range(1, max_value + 1, 2))
print(next(odd_nums_gen))

#task 2

tutors =[
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(next(gen))


from itertools import zip_longest

generator = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)

print(next(generator))

#task 3

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)

#task 4

src1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([x for x in src1 if src1.count(x) == 1])
