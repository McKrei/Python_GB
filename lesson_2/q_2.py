#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el = input('Привет друг, что хочешь добавить в список: ')
your_list = []
while True:
	your_list.append(el)
	print(f'Твой список: {your_list}')
	el = input('Добавим еще или напиши "стоп" слово: ')
	if el == 'стоп' or el == 'Стоп' or el == 'СТОП':	
		break

print(f'Ок, получилось: {your_list}')

l = len(your_list) // 2
i = 1
while l > 0:
	el = your_list[i]
	your_list.insert(i-1, el)
	your_list.pop(i+1)
	i += 2
	l -= 1

print(f'Перемашали: {your_list}')

