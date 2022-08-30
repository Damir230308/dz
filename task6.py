
"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях

Я решил реализовать что-то по типу калькулятора, но по структуре из задания (возможно будет отличаться)
"""
import time


class QueueClass():
    def __init__(self, *tasks):
        self.task = tasks
        self.min_value = 0
    def vault_of_tasks_and_decicion(self):
        self.vault = []
        self.vault.append(self.task)
        print(self.vault, 'In decicion')
    def vault_of_revision(self):
        vault2 = []
        self.vault2 = vault2
        self.vault2.append(self.vault)
        print(self.vault2, 'In revision')
    def finish_vault(self):
        self.vault3 = []
        self.vault3.append(self.vault)
        print(self.vault3, 'Completed!')
test = QueueClass(1 / 4, 6 + 5, 10 / 2, 10 / 3, 11 - 11)
time.sleep(3)
test.vault_of_tasks_and_decicion()
time.sleep(3)
test.vault_of_revision()
time.sleep(3)
test.finish_vault()
