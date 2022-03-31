# task 1

with open('nginx_logs.txt') as f:
    ip_resouce_count = []
    for line in f:
        split = line.split()
        ip_resouce_count.append((split[0], split[5].replace('"', ''), split[6]))
print(ip_resouce_count)

# task 2
fio_hobby = {}

def fio_hobbyes():
    file1 = open('names.csv', encoding='utf-8').read()
    line = file1.rsplit('\n')
    file2 = open('hobbyes.csv', encoding='utf-8').read()
    line2 = file2.rsplit('\n')
    fio_hobby.update(dict(names=line, hobby=line2))
    new_fio = fio_hobby.get('names')
    new_hobby = fio_hobby.get('hobby')
    Ivan = new_fio[0]
    Petr = new_fio[1]
    hobby_for_ivan = new_hobby[0]
    hobby_for_petr = new_hobby[1]
    for_ivan = {Ivan: hobby_for_ivan}
    for_petr = {Petr: hobby_for_petr}
    fio_hobby2 = f'{for_ivan}, \n{for_petr}'
    fio_hobby3 = for_ivan | for_petr
    file3 = open('dicts.txt', 'w', encoding='utf-8')
    file3.write(f'{for_ivan} \n{for_petr}') # Записываю в файл словари, каждый с новой строки
    print(fio_hobby2) # Сформированные словари
    if len(file2) < len(file1):
        fio_hobby3['Петров,Петр,Петрович'] = 'горные лыжи', None  # Если None
        print(fio_hobby3) # Смотрю fio_hobby3
        file3 = open('dicts.txt', 'w', encoding='utf-8')
        file3.write(f'{for_ivan} \n{for_petr}, \n{fio_hobby3}') # Дозаписываю в файл
    if file1 < file2:
        exit(1)
fio_hobbyes()

# task 3

import sys

# добавить цены
price = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price, + '\n')

numbers = sys.argv[1:]

with open('bakery.csv', encoding='utf-8') as f:
    if len(numbers) > 1:
        start_index = int(numbers[0])
        end_index = int(numbers[1])
    elif len(numbers) == 0:
        start_index = 0
        end_index = sum(1 for line in f)
    else:
        start_index = int(numbers[0])
        end_index = sum(1 for line in f)
        f.seek(0)
    for idx, line in enumerate(f):
        if start_index <= idx + 1 <= end_index:
            print(line.strip())
