'''
4. Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''

while True:
	try:
		plus_number = int(input("Введите положительное число: "))
	except:
		continue
	while True:
		try:
			minus_number = int(input("Введите отрицательное число: "))
			if minus_number < 0:
				break
			continue
		except:
			continue
	break

def expo(num_1, num_2):
	global number
	number = num_1
	for i in range(1, abs(num_2)):		
		number *= num_1
	return 1 / number

print(f'Получилось: {expo(plus_number, minus_number)}, В виде дроби: 1/{number}') 

# Две строчки по первому варианту

my_func = lambda x, y: x ** y
print(f'Решение питона: {my_func(plus_number, minus_number)}') 

