'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''

def div(one, two):
	try:
		return round(one / two, 2)		
	except:
		print("На ноль сегодня не делим!")


while True:
	try:
		number_one, nomber_two = int(input('Введите первое число: ')), int(input('Введите второе число: '))
		break
	except:
		print("Попробуй еще раз!")

print(f'Результат деления: {div(number_one, nomber_two)}')

