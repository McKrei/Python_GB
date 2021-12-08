'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''
try:
	with open('file_number_two.txt', 'r', encoding='utf-8') as file_obj:
		content = file_obj.readlines()

	print(f'В этом тексте {len(content)} строк')

	for ind, el in enumerate(content):
		print(f'В {ind+1} строке, {len(el.split())} слов')

except IOError:
	print('Ошибка с файлом')


