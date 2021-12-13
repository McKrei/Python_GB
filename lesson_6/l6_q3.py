'''
3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
ink = {"wage": 40000, "bonus": 20000}

class Worker:

	_income = ink["wage"] + ink["bonus"]  # Честно скажу так и не понял, что от меня хотят, с сылками на словарь! 

	def __init__(self, name, surname, position):

		self.name = name
		self.surname = surname
		self.position = position
		
# my_worker = Worker('Евгений', 'Валерьевич','Менеджер')
# print(my_worker.name, my_worker.surname, my_worker.position, my_worker._income)
	

class Position(Worker):

	def full_name(self):
		print(self.name, self.surname)

	def print_income(self):
		print(self._income)

manager = Position('Евгений', 'Валерьевич','Менеджер')
manager.full_name()
manager.print_income()
