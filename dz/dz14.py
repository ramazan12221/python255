# Написать функцию, которая считает площадь фигур
# import math
#
#
# def gem(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         return kwargs['d1'] * kwargs['d2'] / 2
#     if figure_type == 'square':
#         return kwargs['a']**2
#     if figure_type == 'trapezoid':
#         return 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
#     if figure_type == 'circle':
#         return math.pi * kwargs['r']**2
#     if figure_type == 'unknown':
#         print('Invalid data')
#
#
# print(gem('rhombus', d1=10, d2=8))
# print(gem('square', a=5))
# print(gem('trapezoid', a=12, b=3, h=6))
# print(gem('circle', r=18))
# gem('unknown', a=1, b=1, c=3)

# Функцию, ее принимающие аргументы, условия и вывод написал сам.
# Не мог додуматься как правильно прописать return (подсмотрел у вас)
# Не вспомнил, что этот код читается с вызова функции, а потом уже сама функция
# И забыл, что **kwargs возвращает словарь, значения которого можно легко доставать через ключи и использовать
