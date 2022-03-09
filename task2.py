# dz
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for _ in range(len(my_list)):

    element = my_list.pop(0)

    if element.isdigit():
        my_list.extend(['"', '{:02}'.format(int(element)), '"'])

    elif element[0] == '+' and element[1].isdigit():
        my_list.extend(['"', '{:02}'.format(int(element)), '"'])

    else:
        my_list.append(element)

print(' '.join(my_list))
print(my_list)
