# Очень сложно, прям потратил в 3 раза больше времени! чем на все остальное. Обидно, что даже при этом кое как на костылях финишировал

goods = int(input("Введите количество наименований товаров: "))
n = 1
my_dict, my_list, name, price, kl, ed = [], [], [], [], [], []
my_analys = {}
while n <= goods:
    my_dict = dict({'Название': input("Введите название: "), 'Цена': input("Введите цену: "),
                    'Количество': input('Введите количество: '), 'eд.': input("Введите единицу измерения: ")})
    print('-'*100)
    my_list.append((n, my_dict))
    name.append(my_dict['Название'])
    price.append(my_dict['Цена'])
    kl.append(my_dict['Количество'])
    ed.append(my_dict['eд.'])
    n += 1

my_analys.update({'Название': name })
my_analys.update({'Цена': price })
my_analys.update({'Количество': kl })
my_analys.update({'eд.': ed })

print(my_list)
for key in my_analys:
	print(key, ': ', my_analys[key])









