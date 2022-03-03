# dz2
cubes = []
i = [0]
for num in range(1, 1000, 2):
    cubes.append(num ** 3)
print(cubes)
numbers = []
for cube in cubes:
    int(cube) == cube
    sum = 0
    while (cube != 0):
        sum = sum + cube % 10
        cube = cube // 10
    str(sum) == sum
    numbers.append(sum)
print(numbers)
division = []
for seven in numbers:
    if seven % 7 == 0:
        division.append(seven)
print(division)
list_plus_seventeen = []
for element in division:
    element = element + 17
    list_plus_seventeen.append(element)
print(list_plus_seventeen)
