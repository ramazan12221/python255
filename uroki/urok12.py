# типы данных:
# изменяемые: списки (list)
# неизменяемые: число (int), строка (str), вещественное число (float), булевы значения (bool)


# a = {'Tom', 'Bob', 'Alice'}
# a.add('Anna') #добавление элемента
# print(a)
# # b = 'Tom'
# # if b in a:
# #     a.remove(b) #удаление элемента
# # a.discard('Tom') #тоже удаление элемента
# # a.pop() #удаляет первый элемент, но элементы в множестве формируются рандомно  элемента
# a.clear() #полная очистка множества элемента
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b) # возвращает множество объединений множеств a и b (метод)
# c = a | b # другая запись union, (оператор)
# print(c)
# a |= b
# print(a)
# c = a & b # возвращает пересечение множеств(одинаковые элементы из двух множеств)
# print(c)
# a &= b # короткая запись возвращения пересечения множеств, только в этом случае мы перезаписываем переменную a
# print(a)
# c = b - a # поиск уникального элемента который есть в b, но которого нет в a
# print(c)
# c = a ^ b # возвращает множество уникальных элементов из a и b которые не присутствуют сразу в двух множествах(a и b)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(max(s))
# print(min(s))

# s1 = 'Hello'
# s2 = 'How are you'
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# one = drawing ^ music
# print(one)
# two = drawing & music
# print(two)
# drawing = drawing - two
# print(drawing)

# Tun frozenset (замороженное множество)
# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# s = frozenset({'hello', 'world'})
# s = frozenset('hello')
# print(s)


# Словарь dict() - изменяемый тип данных

# lst = ['one', 'two', 'three']
# print(lst)
# print(lst[0])
# d = {"a": "one", "b": "two", "c": "three"}  # значения могут повторяться, но ключи должны быть уникальными
# print(d["a"])

# d = {} # создания пустого словаря
# print(d)
# print(type(d))

# d = {'one': 1, 2: "two"}
# print(d)

# d = dict(short='dict', long='dictionary') # в таком виде записи ключ не должен быть в кавычках если ключом является
# слово и вместо двоеточия используется равно
# print(d)

# users = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('ann@gmail.com', 'Ann')
# )
# print(users)
# d_users = dict(users)
# print(d_users)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2]) # обращение к ключу, но выводит значение
# d[2] = 15
# d[9] = 45**3
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 6, 7], True: 1}
# нельзя использовать список в виде ключа тк ключом должен быть неизменяемый тим данных
# print(d)

#  print(d[42][1]) # 1 способ получения значения в словаре
#  print(d[(1, 2.3)]) # 2 способ получения значения в словаре

#  print('one' in d) # проверка наличия элемента в словаре выдаёт либо True или False
#  print('two' in d)

#  key = 'one'
#  if key in d:
#      del d[key] # удаляет ключ вместе со значением

#  key = 'one'
#  try:
#      del d[key]
#  except KeyError:
#      print('Такого элемента нет в словаре')
#  print(d)

# for key in d:
#     print(key, '->', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = dict()
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')
# d = {i: input('->') for i in range(1, 5)} # более короткий способ записи ключей и значений в словарь
# print(d)
# dislike = int(input('Какой элемент исключить:'))
# del d[dislike]
# print(d)
# print(len(d))


# goods = {
#     '1': ['Core i3-4330', 9, 4500],
#     '2': ['Core i5-4670k', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 4600]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input('Количество'))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], sep="")

# методы для словарей
# d = {'A': 1, 'B': 2, 'C': 3}
# v = d['B']
# print('B =', v)
# value = d.get('E', 'False') # обращение к значению по заданному ключу
# если ключа нет в словаре то выводит none или то значение которое прописанного вторым в методе
# print(value)
# d.clear() # очистка словаря
# print(d)

# d2 = d.copy() # копирует словарь d1 в словарь d2, изменения из одного словаря не влияют на другой словарь
# print('D =', d)
# print('D2 =', d2)
# print()
# d['E'] = 7
# d2['B'] = 5
# print('D =', d)
# print('D2 =', d2)

# d = {'A': 1, 'B': 2, 'C': 3}
# a = d.items() # возвращает ключи и значения в массив из словаря
# print(a)
# b = d.keys() # возвращает ключи в массив из словаря
# print(b)
# c = d.values() # возвращает значения в массив из словаря
# print(c)
# print(d['A'] + d['B'])

# for key, val in d.items():
#     print(key, '->', val)

# item = d.pop('B') # удаляет по ключу, но возвращает значение
# print(item)
# print(d)

# item = d.setdefault('C') # возвращает значение заданного ключа,
# если такого ключа нет к словарю, то этот ключ добавится и вторым параметром можно задать значение этому ключу
# print(item)
# print(d)

# d.update([('R', 7), ('Q', 9)])  # добавляет ключ и значение к словарю
# print(d)
