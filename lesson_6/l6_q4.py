'''
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''
from random import randint

class Car:

	broadcast = 0 #добавил значение передачи!

	def __init__(self, speed, color, name, is_police=False):  #В моем слуачаее speed это кол-во км\ч на одну передачу!
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
#		self.show_speed() # Текста стало в 2-а раза больше, за то сразу идет проверка на превышение скорости. 
		self.broadcast += 1		
		if self.broadcast == 1: 
			print(f'Автомобиль начал движение {self.speed}км/ч')
		elif self.broadcast >= 5:
			if randint(1, 6) == 6: # Агрессивное вождение, даже в программе должно иметь последствия!
				self.stop()
				return print(f'Водитель не справился с управлением вылетев на встречную полосу движения, {randint(1, 5)} человек погибло!')

			print(f'Досигнута максимальная скорость {self.speed * 5}км/ч') 
		else:	
			print(f'Автомобиль ускорился до {self.speed * self.broadcast}км/ч')

	def stop(self):
		print('Автомобиль остановился!')
		self.broadcast = 0

	def turn(self, direction='право'):
		print(f'Автомобиль повернул на {direction}')

	def show_speed(self):
		print(f'Скорость автомобиля {self.speed * self.broadcast}км/ч')



class TownCar(Car):

	def show_speed(self):
		spe = self.speed * self.broadcast
		if spe > 60:
			print(f'Скорость автомобиля {spe}км/ч Превышение на {spe - 60}км/ч')
		else:
			print(f'Скорость автомобиля {spe}км/ч')


class WorkCar(Car):

	def show_speed(self):
		spe = self.speed * self.broadcast
		if spe > 40:
			print(f'Скорость автомобиля {spe}км/ч Превышение на {spe - 60}км/ч')
		else:
			print(f'Скорость автомобиля {spe}км/ч')

class SportCar(Car):
	pass

class PoliceCar(Car):
	pass
	
my_towncar = TownCar(30, 'red', 'bugatti')
my_workcar = WorkCar(20, 'black', 'Volwo')
my_policecar = PoliceCar(40, 'blue', 'ferari', True)

print(my_policecar.is_police)
my_towncar.go()
my_towncar.turn()
my_towncar.go()
my_towncar.show_speed()
my_towncar.turn('назад')
my_towncar.go()
my_towncar.show_speed()
my_towncar.go()

