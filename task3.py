# dz
list_words = ['инженер-конструктор Ваня', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор алита']

for word in list_words:

    word = word.split(' ')[-1]
    print('Привет, {}!'.format(word.title()))
