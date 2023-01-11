# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print('Вызов функции: ', count)
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(args1, args2):
#         print('Данные:', args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', 'Лаврова')


# def args_decorator(fn):
#    def wrap(*args, **kwargs):
#        print('args', args)
#        print('kwargs', kwargs)
#        fn(*args, **kwargs)
#
#    return wrap


# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#    print(a, b, c, 'изучаю', study, '\n')


# @args_decorator
# def new_func(q):
#    print(q)


# print_full_name('Борис', 'Елизавета', 'Светлана', study='JavaScript')
# print_full_name('Владимир', 'Екатерина', 'Виктор')
# new_func('Новая функция')


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сложение:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def myltiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @myltiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))


# print(int('10'))
# print(int('1010', 2))
# print(int('12', 8))
# print(int('A', 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12

# print(0b10010)
# print(0o22)
# print(0x12)


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
#
# print(e * 3)
# print(e * -3)
#
# print(e in 'I am learn Python')
# print(e in 'I am learn Java')

# s = 'Hello'
# print(s[1])
# print(s[-5])
#
# print(s[1:])
# print(s[-5:-2])
# print(s[0:5:2])
# print(s[::-1])

# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)


# def changeCharToStr(s, c_old, c_new):
#     i = 0
#     s2 = ''
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython.Nython очень интересный язык программирования.'
# str2 = changeCharToStr(str1, 'N', 'P')
# print(str1)
# print(str2)


# print('Привет')
# print(u'Привет')

# print('I\'m learning\nPython')
# print('C:\file.txt')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file\\'[:-1])
# print(r'C:\file' + '\\')
# print('C:\\file\\')


# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}. Мне {age}')


# import math
# print(f'Значение числа pi: {round(math.pi, 2)}')
# print(f'Значение числа pi: {math.pi:.2f}')


# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}')

# a = 74
# print(f'{{{{{a}}}}}')

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print(r'home\{dir_name}\{file_name}')
# print(f'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)


# s = '''<div>
#     <a href="#">content</a>
# </div>
# '''
#
# print(s)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# import math as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
