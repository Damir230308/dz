
"""
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
"""

# О(n)

users = {'user1': {'password': '1111', 'activation': True},
         'user2': {'password': '1111', 'activation': False},
         }
def web_system(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать!"
        if value['password'] == user_password and not value['activation']:
            return "Статус активации: Неактивен. Хотите пройти активацию?"
        if value['password'] != user_password and value['activation']:
            return "Пароль не верный"
    return 'Такого пользователя нет'

# Второй алгоритм:

# О(1)

def web_system1(users, user_name1, user_password1):
    users.get(user_name1)
    if users[user_name1]['password'] == user_password1 and users[user_name1]['activation']:
        return "Добро пожаловать!"
    if users[user_name1]['password'] != user_password1 and users[user_name1]['activation']:
        return "Пароль не верный!"
    if users[user_name1]['password'] == user_password1 and not users[user_name1]['activation']:
        return "Статус активации: неактивен. Хотите пройти активацию?"
    return "Такого пользователя не существует"

print(web_system(users, 'user1', '1111'))
print(web_system1(users, 'user12', '1111'))
