
number = input("Введите любое натуральное число: ")
len_number = (len(number))
a = int("1"+("0"*(len_number-1)))
number = int(number)
x = 0
y = 0
while a >= 1:
	x = number // a
	print(f'x = {x}')
	if x > y:
		y = x
		print(f'y = {y}')
		if y == 9:
			break			
	number = number - (a * x)
	a = a // 10

print(f"Наибольшая цифра: {y}")