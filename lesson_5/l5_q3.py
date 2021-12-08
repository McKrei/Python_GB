'''
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

try:
	with open('file_number_three.txt', 'r', encoding='utf-8') as file_obj:
		content = file_obj.readlines()

	average = 0
	print('Зарплата ниже 20000: ')
	for el in content:
		el = el.split()
		average += int(el[1])
		if int(el[1]) < 20000:
			print(*el)

	print(f'Фонд заботной платы: {average:,}\nCредняий оклад: {int(average / len(content))}')

except IOError:
	print('Ошибка с файлом')
''' 
Решил оставить данный код, я взял Фамилию из википедии и у меня был вид:  4. Рябов
Ну и оклад тоже писать лень. Я же программист :-) 

import random

with open('file_number_three.txt', 'r', encoding='utf-8') as file_obj:
	content = file_obj.readlines()

my_list = []

for el in content:
	el = el.replace('\n', '')
	el = el.split()
	my_list.append(f'{el[1]} {random.randint(16000, 28000)}\n')

with open('file_number_three.txt', 'w', encoding='utf-8') as file_obj:
	file_obj.writelines(my_list)

'''
