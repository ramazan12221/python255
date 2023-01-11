# 1 задание создать лямбда-выражение, которое возвращает произведение 3 чисел
# print((lambda a, b, c: a * b * c)(2, 5, 5))


# 2 отсортировать список
# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
# res1 = sorted(students, key=lambda item: item['name'])
# res2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res1)
# print(res2)


# 3 максимальная и минимальная оценка
# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# print(max(students, key=lambda s: s['final']))
# print(min(students, key=lambda s: s['final']))


# 4 в квадрат и в куб
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(list(map(lambda t: t ** 2, nums)))
# print(list(map(lambda t: t ** 3, nums)))
