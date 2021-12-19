'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
from random import randint

class ZeroDivisionError_version_2(Exception):

	def __init__(self, txt):
		self.txt = txt


try:
	number = int(input("На скольких будем делить пирог?: "))
	pie = randint(number, number*10)
	if number == 0:
		raise ZeroDivisionError_version_2('Пирог на ноль не делиться!')
except ValueError:
	print('Что за азкорючки? Понимаю только числа.')
except ZeroDivisionError_version_2 as erro:
	print(erro)
else:
	print(f'Отлично пирог поделили, каждому {int(pie / number)} по частей, надеюсь хватит всем!')

