
'''
Создать функцию которая создает фалы для ДЗ
'''


def create_n_files(number_files):
	'''
	Принимает количество файлов которое нужно создать, 
	путь до папки и текст внутри файла изменить можно внутри функции.
	'''
	ind = 1
	while number_files >= ind:
		try:
			with open(f"Repo_python_gb/Python_GB/lesson_5/l5_q{ind}.py", "w") as file_obj: #путь до папки и имя файла-ов!
				file_obj.write(f"'''\nText task {ind} \n'''\n") #Текст в файлах, можно удалить
		except IOError:
			print('Ошибка ввода-вывода!')	

		print(f'Файл №{ind} создан!')
		ind += 1 

create_n_files(7)
