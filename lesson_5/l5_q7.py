'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста. Ха, думал всегда его используем :-) 
'''
import json

aver_dict = {"average_profit": 0}
my_dict = {}
ind = 0
try:
	with open('file_number_seven.txt', 'r', encoding='utf-8') as file_obj:

		for line in file_obj:
			line = line.split()
			num = float(line[2]) - float(line[3])
			if num > 0:
				ind += 1
				aver_dict["average_profit"] += num			
			my_dict.update({line[0]:round(num,2)})

	aver_dict["average_profit"] = round(aver_dict["average_profit"] / ind, 2)
	my_list = [my_dict, aver_dict]

	with open('my_file.json', 'w') as file_obj: # На данном примере совсем не нашел отличий 
		json.dump(my_list, file_obj)

except IOError:
	print('Ошибка с файлом')