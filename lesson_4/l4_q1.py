
'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
'''
from sys import argv

def salary (h, p, f):
	'''
	Считаем ЗП по часам, переработку, премию, вычитаем налог. 
	'''	
	print(f'Расчет зарплаты {name}')
	h, p, f = int(h), int(p), int(f)
	sal = ower_work = prize = gross = 0 # У меня не получилось в оду строчку сделать их глобальными. Как это сделать? 
	sal = h * 200
	print(f'Оклад: {sal}р.')

	if h > 168: 
		ower_work = (h - 168) * 200
		print(f'Переработка{h - 168}: {ower_work}р.') 

	prize = round(p*0.1 if f/p > 1 else p*0.05)
	gross = round((sal + ower_work + prize) * 0.13, 2)

	print(f'Премия: {prize}р.')
	print(f'Итого зарплата: {sal + ower_work + prize}р.')
	print(f'Налог 13%: {gross}р.')
	print(f'Выплата сотруднику: {round(sal + ower_work + prize - gross)}р.')


_, name, hour, plan, fact = argv
salary(hour, plan, fact)

