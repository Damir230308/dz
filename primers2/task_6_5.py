"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

with open('44444', 'rb') as file:
    CONTENT = file.read()

print(detect(CONTENT))
ENCODING = detect(CONTENT)['encoding']
print(ENCODING)

with open('44444', 'r', encoding=ENCODING) as file:
    CONTENT = file.read()
print(CONTENT)