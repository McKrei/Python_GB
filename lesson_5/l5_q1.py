'''
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
'''
import os

try: 
	with open("file_number_one.txt", 'w+', encoding="utf-8") as file_obj: # без UTF - 8  у меня тарабарщина :-( 
		while True:
			text_line = input('Введите сроку: ')
			if text_line == '':				
				break
			file_obj.write(text_line + '\n')

		file_obj.seek(0)
		content = file_obj.read()
		print('-'*50 + '\n' + content)

except IOError:
	print('Ошибка с файлом')

if 'y' == input('Сохранить файл "y" '):
	print('Файл сохранен')

else:
	os.remove('file_number_one.txt')
	print('Файл удален')



