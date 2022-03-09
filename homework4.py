price_list = [12.36, 55.03, 45.02, 53.2, 33.34, 22.14,
    12.31, 4.32, 45.3, 71.2, 4.54, 2.07, 13.21, 568.7]

check_id = id(price_list)

copy_price_list = price_list.copy() 

for i in range(len(copy_price_list)):

    cost = copy_price_list.pop(0)  
    kk = cost % 1  
    r = cost - kk  
    copy_price_list.append('{:.0f} руб {:02.0f} коп'.format(r, kk*100))
print(', '.join(copy_price_list))

'''чтобы не менять объекты списка можно применить
не метод sort(), а функция sorted()'''

print('\n',sorted(price_list))  # цены, отсортированные по возрастанию


if check_id == id(price_list):
    print('equal objects')
else:
    print('different objects')

print('\nid of origin list is {}\n\n\
id of sorted list is {}'.format(check_id, id(price_list)))

copy_2_price_list = price_list.copy() # create a 2nd list copy

copy_2_price_list.sort(reverse = 1)

print('\n', copy_2_price_list)

print('\nцены пяти самых дорогих товаров по возрастанию {}'\
    .format(sorted(copy_2_price_list)[-5:]))
