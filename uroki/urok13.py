# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)


# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five',
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep="")
#         #sep отвечает за пробелы между объектами в принте


# sales = {
#      "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#      "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#      "Ann": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#      "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# for x in sales:
#      print(x)
#      for y in sales[x]:
#          print('\t', y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# data = int(input("Новое значение: "))
# sales[person][region] = data
# print(sales[person])


# data = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)


# s = 'Hello'
# b = {i: i * 3 for i in s}
# print(b)

# a = list(b) #если приводить словарь в лист так то получаем только ключи
# print(a)
# a = list(b.values())
# print(a)
# a = list(b.items())
# print(a)


# a = ["one", 1, 2, 3, "two", 10, 20, 'three', 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#    if type(i) == str:
#        d[i] = []  # d['one'] = []
#        s = i  # s = i
#    else:
#        d[s].append(i)
# print(d)

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)
# d = zip([12, 1, 2], ['Dec', 'Jan', 'Feb'])
# print(d)
# print(type(d))
# print(dict(d))
# print(list(d))


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = {k: v for k, v in zip(a, b)}
# print(d)


# a = ['a', 'b', 'c', 'd']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# q = zip(a, b, c)
# print(list(q))


# print(list(zip(range(5), range(100))))


# one = {'name': 'Igor', 'last_name': 'Smith', 'job': 'consultant'}
# two = {'name': 'Olga', 'last_name': 'Doe', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)


# Распаковка последовательности
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)


# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в", m, "=", profit)


# one = {'apple': 20, 'orange': 35, 'pepper': 60}
# two = {'pepper': 40, 'onion': 55}
# print([two, one])
# print({**two, **one})


# for i in range(3):
#     print(i)
#
# colors = ['red', 'yellow', 'green']
# j = 1
# for i in colors:
#     print(j, i)
#     j += 1

# colors = ['red', 'yellow', 'green']
# for j, i in enumerate(colors, 1):  # второй параметр показывает с какого числа будет вестись отсчёт
#    print(j, i)


# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i, "Stop"))
# print(next(i, "Stop"))


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # одна * используется для распаковки последовательности с одним типом значения
# print(b)


# def func(*args):  #args - аргументы
#     return args
#
#
# print(func(2))
# print(func(2, 1, 3))
# print(func())


# def summa(*parems):
#     res = 0
#     for i in parems:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(7, 3))


# def to_dict(*parems):
#     return {i: i for i in parems}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def ch(*args):
#     res = []
#     sr_ar = sum(args) / len(args)
#     print(sr_ar)
#     for i in args:
#         if i < sr_ar:
#             res.append(i)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
