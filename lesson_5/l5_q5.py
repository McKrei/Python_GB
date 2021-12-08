'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

from random import randint
num = 0
with open('file_number_five.txt', 'w', encoding='utf-8') as file_obj:

	for i in range(111):
		num = randint(1, 1000)
		file_obj.write(f'{num} ')
		if i%11 == 0:			
			file_obj.write('\n')
summ = 0
with open('file_number_five.txt', 'r', encoding='utf-8') as file_obj:

	for line in file_obj:
		for el in line.split():
			summ += int(el)


print(f'Сумма чисел в файле: {summ:,}')

		

		


