'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

my_dect = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять' }

try:

	with open('file_number_four.txt', 'r', encoding='utf-8') as f_r, open('file_fo.txt', 'w', encoding='utf-8') as f_w:
		
		for line in f_r: 
			line = line.lower()
			line = line.split()
			line.insert(0, my_dect.get(line[0]))
			line.pop(1)
			line = ' '.join(line)
			f_w.write(f'{line.title()}\n')

except IOError:
	print('Ошибка с файлом')