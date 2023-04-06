"""
6. Создать (ПРОГРАММНО) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
a = 'weqr4ee'
NEWFILE = open('test.txt', 'w')
NEWFILE.write('сетевое программирование\nсокет\nдекоратор')
NEWFILE.close()

with open('test.txt') as codedFile:
    print(f'Кодировка файла: {codedFile.encoding}')
    for line in codedFile:
        # преобразуем содержимое в utf-8
        encd_line = line.encode('utf-8')
        # декодируем содержимое
        dcd_line = encd_line.decode('utf-8')
        print(dcd_line)