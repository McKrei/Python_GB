'''
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра. 
'''
# Чет как то легко по сравнению с остальными. Даже идей для усложнения нету. 
class Stationery:
	def __init__(self, title):
		self.title = title

	def draw(self):
		print(f'{self.title} Запуск отрисовки')

class Pen(Stationery):

	def draw(self):
		print(f'{self.title} Четкие линии, удобно лежит в руке!')

class Pencil(Stationery):

	def draw(self):
		print(f'{self.title} Баланс твердости, дает возможность определять толщину линий нажимом. ')

class Handle(Stationery):

	def draw(self):
		print(f'{self.title} Вечный маркер, от рисованные линии, отлично выделяется на холсте')

pen_1 = Pen('Parker')
pen_1.draw()

pencil_1 = Pencil('Sword TM')
pencil_1.draw()

handle_1 = Handle('wither')
handle_1.draw()
