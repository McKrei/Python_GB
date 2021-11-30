'''
3. Реализовать функцию my_func(), которая принимает три (сколько угодно) позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''

numbers = (input(f'Введите ряд чисел через пробел: ')).split()
list = []
def my_summ():
	for i in numbers:
			try:			
				list.append(int(i))
			except:
				continue
	a = max(list)
	list.remove(max(list))
	return a + max(list)

print(f"Сумма наибольших чисел: {my_summ()}")

