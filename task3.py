class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

a = Position('Антон', 'Зыков', 'Великий Владыка Северных Земель', 1000000, 5000)
print('Имя работника: ', a.get_full_name())
print('Должность работника: ', a.position)
print('полный доход: ', a.get_total_income())