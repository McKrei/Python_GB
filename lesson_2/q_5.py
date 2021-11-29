

# Заморочился и нескоолько раз хотел сдаться, но теперь даже если создать список с помощью ранодома,
# он будет работать нормально и находить себе идеальное место!!

my_list = [100, 200, 300, 400, 500, 900, 800, 700, 600]

while input("Хотите добавить число, в списко введите 'да': ") == 'да':
	l = len(my_list)
	try:
		number = int(input('Введите число от 1 до 1000: '))	
	except:
		print('Просил же чсло, вроде 1 или 55, сложно, что ли?')
		continue

	else:
		if number > max(my_list):
			x = my_list.index(max(my_list))
			my_list.insert(x+1, number)

		elif number < min(my_list):
			x = my_list.index(min(my_list))
			my_list.insert(x, number)

		else:
			number_minus = number
			number_plus = number

			while len(my_list) == l:
				for i in my_list:
					if i == number or i == number_plus:
						x = my_list.index(i)
						my_list.insert(x, number)
						break
					elif i == number_minus:
						x = my_list.index(i)
						my_list.insert(x+1, number)
						break
				number_minus -= 1
				number_plus += 1

		print(my_list)
print('END')

