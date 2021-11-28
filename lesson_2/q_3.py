# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#   Напишите решения через list и через dict.

# По красоте можно сделать без листов просто добавив сезон в словарь, но задание есть задание! 

seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month_all = [None, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0]
months = {
	12: 'Декабрь', 1: 'Январь', 2: 'Февраль',
	3: 'Март', 4: 'Апрель', 5: 'Май',
	6: 'Июнь', 7: 'Июль', 8: 'Август',
	9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь',
}

try:
	month = int(input('Введите номер месяц: '))
except:
	print("Введите номер месяца!")

else:

	if month < 1 or month > 12:
		print('Такого месяца нету!')
	else:  
		print(f"{month} месяц это {months.get(month)}, {seasons[month_all[month]]}!")

# Был еще вариант крассивый вариант в интернете, я сним разобрался кроме строки userOutput = season.capitalize()

monthsBySeason = {
  'winter': [12, 1, 2],
  'spring': [3, 4, 5],
  'summer': [6, 7, 8],
  'autumn': [9, 10, 11]
}

userInput = int(input())
userOutput = ''

for season in monthsBySeason:
  if userInput in monthsBySeason[season]:
      userOutput = season.capitalize()
      break
  else:
      userOutput = 'There is no such month'

print(userOutput)
