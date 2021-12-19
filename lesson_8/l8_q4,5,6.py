
'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
'''
# Несколько раз доделывал и переделывал! Классы ошибки удалил, не виду в них смысла, много лишнего кода. А тут и так черт ногу сломит!


class WareHouse:		

	def __init__(self, name, square, location):
		self.name = name
		self.square = square
		self.location = location
		self.object_dict = {}

	def recipt(self, quantity, equipment):
# Принимаем на склад товар, проверяем кол-во на валидность, и наличие товара на складе.
		try:
			quantity = int(quantity)
			if int(quantity) >= 0:
				if self.object_dict.get(equipment) == None:
					self.object_dict.update({equipment: quantity})
					print(f'Товар {equipment}, {quantity}шт. принят на склад {self.name}')

				else:
					self.object_dict[equipment] += quantity
					print(f'Товар {equipment}, {quantity}шт. принят на склад {self.name}, кол-во товара {self.object_dict[equipment]}шт.')
			
			else: print('Некоректные данные')
		except Exception: print('Некоректные данные')

	def send(self, where, quantity, equipment):
# Перенос товара с одного склада на другой, проверка валиднасти данных, для переноса используем иметод recipt
		try:
			quantity = int(quantity)
			if quantity >= 0:
				if where.object_dict.get(equipment) == None: print('Данного товара нет на складе.')

				elif where.object_dict.get(equipment) > quantity:
					where.object_dict[equipment] -= quantity
					self.recipt(quantity, equipment)

				elif where.object_dict.get(equipment) <= quantity:
					self.recipt(where.object_dict.pop(equipment), equipment)

			else: print('Некоректные данные')
		except Exception: print('Некоректные данные')

	@property
	def what_inside(self):
		if self.object_dict == {}: print('Склад пустой')
		else:
			for key, el in self.object_dict.items():
				print(f"Товар: {key}, {el} шт.")


class OficeEquipment:

	def __init__(self, name, price, serial_number):
		self.price = price
		self.name = name
		self.serial_number = serial_number

	@property
	def price(self):
		self.price = __price


	@price.setter
	def price(self, price):

		if type(price) is not int:
			print('Стоимость должно быть число .')
			self.__price = 1

		elif price == 0:
			print('Цена не должна быть меньше 1.')
			self.__price = 1

		else:
			self.__price = abs(price)


	def __str__(self): # ВОТ что это _OficeEquipment__quantity за жесть я 40 минут сидел над этой ошибкой!  
		return f"{self.name} Цена: {self._OficeEquipment__price}; Серийный номер: {self.serial_number}."


class Printer(OficeEquipment):

	def __init__(self, name, price, serial_number, skanner, speed_print):
		super().__init__(name, price, serial_number)
		self.skanner = skanner
		self.speed_print = speed_print

class Skanner(OficeEquipment):

	def __init__(self, name, price, serial_number, color):
		super().__init__(name, price, serial_number)
		self.color = color

class Xerox(OficeEquipment):

	def __init__(self, name, price, serial_number, condition):
		super().__init__(name, price, serial_number)
		self.condition = condition

ware_house_1 = WareHouse('Плохая фантазия', 1000, 'Moskow 84a')
ware_house_2 = WareHouse('Другой склад', 500, 'Архангельск 77ы')
printer_1 = Printer('HP', 50000, 54, True, 5)
skanner_1 = Skanner('samsung', 10000, 4412536, 'red')
xerox_1 = Xerox('XEROX', 25000, 545484, 'norm')

ware_house_1.recipt('ads', printer_1)
ware_house_1.recipt("3", skanner_1)
ware_house_1.recipt(4, skanner_1)
ware_house_2.send(ware_house_1, 7, skanner_1)
ware_house_1.what_inside
ware_house_2.what_inside
