# import math
#
#
# def rectangle():
#     print("Введите стороны прямоугольника")
#     a = float(input("1 сторона: "))
#     b = float(input("2 сторона: "))
#     c = a * b
#     print("Площадь: ", round(c, 2))
#
#
# def triangle():
#     print("Введите основание и высоту")
#     a = float(input("Основание: "))
#     b = float(input("Высота: "))
#     c = (a * b) / 2
#     print("Площадь: ", round(c, 2))
#
#
# def circle():
#     print("Введите радиус круга")
#     r = float(input("Радиус круга: "))
#     print("Площадь: ", round(math.pi * r ** 2, 2))
#
#
# print("1-прямоугольник, 2 -треугольник, 3 - круг")
# fig = (input("Выберите фигуру от 1 до 3: "))
#
#
# if fig == '1':
#     rectangle()
#
# if fig == '2':
#     triangle()
#
# if fig == '3':
#     circle()
