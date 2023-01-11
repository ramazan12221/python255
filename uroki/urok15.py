# lamda (анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 4))
#
#
# def get_sun(x, y):
#     return x + y
#
#
# print(get_sun(1, 2))
# print(get_sun(3, 4))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())  #6
# print(summ(10))  #15
# print(summ(10, 20))  #33
# print(summ(10, 20, 30))  #60


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5, 6, 7))
# print(func1('a', 'b', 'c'))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc_'))


# def inc(n):
#    def inner(x):
#        return n + x
#    return inner
#
#
# f = inc(5)
# print(f(2))
#
#
# def inc1(n):
#     return lambda x: n + x
#
#
# f1 = inc(5)
# print(f(2))
#
# inc2 = lambda n: lambda x: n + x
# f2 = inc(5)
# print(f(2))


# print((lambda n: lambda y: lambda x: n + y + x)(4)(2)(6))


# d = {'b': 10, 'a': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1], reverse=True)
# print(list_d)
# print(dict(list_d))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last name'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['rating'])
# print(res3)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](5, 3)
# print(b)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}  #abs(x) - модуль x
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#   1: lambda: print('Понедельник'),
#   2: lambda: print('Вторник'),
#   3: lambda: print('Среда'),
#   4: lambda: print('Четверг'),
#   5: lambda: print('Пятница'),
#   6: lambda: print('Суббота'),
#    7: lambda: print('Воскресенье')
# }
#
# print(d[3])
# d[3]()


# print((lambda a, b: a if a > b else b)(15, 4))


# ---------------------------------
# map(func, *iterables)


# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# print(list(map(lambda t: t * 2, lst)))


# b = ['1', '2', '3', '4', '5']
# c = list(map(int, b))
# print(c)
# print(type(c))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))


# a = [1, 2, 3]
# b = [4, 5, 6]
# print(list(map(lambda x, y: x + y, a, b)))


# -------------------
# res = filter(func => (true or false), *iterables)


# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# import random
# lst = [random.randint(1, 40) for i in range(10)]
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst)
# print('[10; 20] =', res)


#  Декораторы


# def hello():
#     return 'Hello, I am func "hello"'   # 3
#
#
# def bye():
#     return 'BYE!!!!!'   # 2
#
#
# def super_func(func):
#     print('Hello, I am func "super_hello"')     # 2
#     print(func())   # 4
#
#
# super_func(hello)   # 1
# super_func(bye)   # 1


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test)
# test = hello()
# print(test)
# test = hello
# print(test())


# def my_decorator(func):  # 2
#    def func_wrapper():   # 3
#        print('Code before')    # 4
#        func()  # 5
#        print('Code after')    # 8
#    return func_wrapper    # 3
#
#
# def func_test():    # 6
#    print('func_test')  # 7
#
#
# text = my_decorator(func_test)  # 1
# text()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('func_test')
#
#
# @my_decorator
# def hello():
#     print('hello')
#
#
# func_test()
# print()
# hello()
