# Задание №1 
print('Задание №1')

name = input('Как тебя зовут? ')
age = int(input('Сколько тебе лет? '))
city = input('Из кого ты города?  ')
print(f'Привет, {name} из {city}, {age} лет!')

# Задание №2
print('-'*50)
print('Задание №2')

time = int(input("Сколько времени в секундах? "))

time = time % (24 * 3600)
h = time // 3600
time = time % 3600
m = time // 60
time = time % 60

print(f"Сделал Сам: {h}:{m}:{time}")
print("Подглядел в интернетах: %02d:%02d:%02d" % (h, m, time))

# Задание №3 
print('-'*50)
print('Задание №3')

n = input("Введите число от 1 до 10: ")

nn = int(n + n)
nnn = int(n + n + n)
n = int(n)

print(f"{n} + {nn} + {nnn} = {n + nn + nnn}")

# Задание №4 Самая сложная, Срузу нашел решение без цикла на 1 строчку!
print('-'*50)
print('Задание №4')

number = input("Введите любое натуральное число: ")
len_number = (len(number))
a = int("1"+("0"*(len_number-1)))
number = int(number)
x = 0
y = 0
while a >= 1:
	x = number // a
	if x > y:
		y = x
		if y == 9:
			break			
	number = number - (a * x)
	a = a // 10

print(f"Наибольшая цифра: {y}")

# Задание №5
print('-'*50)
print('Задание №5')

profit = int(input("Какая прибыль компании?: "))
loss = int(input("Какие расходы?: "))

if profit > loss:
	result = profit - loss
	cof = result / profit
	cof = round(cof, 2)	
	print(f'Компания заработал: {result}, рентабельность выручки: {cof}!')
	staff = int(input("Сколько сотрудников работают в компании?: "))
	print(f'Прибыль на каждого сотрудника составила: {round(result / staff)}!')

elif profit == loss:
	print('Компания работает в НОЛЬ!')

else:
	print(f'Компания в ушла в минус на: {loss - profit}')

# Задание №6
print('-'*50)
print('Задание №6')

km_1 = int(input("Результат пробежки первого дня?: "))
km_2 = int(input("Какая твоя цель?: "))
day = 1

while km_1 < km_2:
	day += 1
	km_1 *= 1.1

print(f'Бегай каждый день и через {day} дней, ты пробежишь {km_2} км.')

