'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
'''
# Я посторался совсем не трогать втроенный тип "complex" , с ним и класс содовать не нужно :-) 


class ComplexNumber: 

	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary


	def __str__(self):
		sign = '+' if self.imaginary > 0 else '-'
		return f'({self.real}{sign}{abs(self.imaginary)}j)'

	def __add__(self, other):
		return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

	def __sub__(self, other):
		return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

	def __mul__(self, other):
		x1 = self.real
		x2 = other.real
		y1 = self.imaginary
		y2 = other.imaginary
		return ComplexNumber((x1*x2)+((y1*y2)*-1), (x1*y2)+(y1*x2)) 




a = ComplexNumber(1, -3)
b = ComplexNumber(2, 5)
p_a = 1 - 3j
p_b = 2 + 5j
c = a + b
p_c = p_a + p_b
print(f'Мое      {a} + {b} = {c}')
print(f'Проверка {p_a} + {p_b} = {p_c}')
a = c - b 
p_a = p_c - p_b
print(f'Мое      {c} - {b} = {p_a}')
print(f'Проверка {p_c} - {p_b} = {p_a}')
c = a * b
p_c = p_a * p_b
print(f'Мое      {a} * {b} = {c}')
print(f'Проверка {p_a} * {p_b} = {p_c}')
