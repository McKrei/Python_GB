'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''

class Data:

	def __init__(self, time):
		self.time = time

	@classmethod # Зачем тут клас метод когда удобнее по self обращается?  
	def extraction(cls, time):
		list = [int(el) for el in time.split('-')]
		return list

	@staticmethod
	def check_data(param):
		if param[0] > 31 or param[0] < 1: return 'Не верные день!'
		elif param[1] > 12 or param[1] < 1: return 'Не верные месяц!'
		else: return 'С датой все норм!'

day = Data('7-04-1994')
print(day.time)
print(Data.extraction(day.time))
print(day.check_data(Data.extraction(day.time))) # Шикарная конструкция 


