# print(ord('a'))
# print(ord('#'))
# print(ord('к'))
#
# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# my_str = 'Test string for me'
# arr = [ord(x) for x in my_str]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in input('-> ')[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print('Количество последних элементов:', arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(7897))
# print(chr(47))


# a = 122
# b = 97
# if a > b:
#     for i in range(b, a+1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')


# print('apple' == 'Apple')
# print('apple' > 'Apple')


# from random import randint
# short = 7
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(short, longest)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль:', random_password())


# s = 'hello, WORLD! I am learn Python.'
# print(s.capitalize())   # Hello, world! i am learn python.
# print(s.lower())   # hello, world! i am learn python.
# print(s.upper())   # HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase())   # HELLO, world! i AM LEARN pYTHON.
# print(s.title())   # Hello, World! I Am Learn Python.


# s = 'hello, WORLD! I am learn Python.'
# print(s.count('h', 1, -3))   # количество искомых символов
# print(s.find('Python'))   # возвращает индекс первого совпадения
# print(s.find('oPython'))   # если подстроки нет, возвращается -1


# string = 'один два'
# one = string[:string.find(' ')]
# two = string[string.find(' ') + 1:]
# print(two + ' ' + one)


# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)


# s = 'hello, WORLD! I am learn Python.'
# print(s.index('Python'))
# print(s.index('oPython'))


# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# ind1 = s.index('(')
# ind2 = s.index(')')
# print(ind1)
# print(ind2)
# print(s[ind1 + 1:ind2])


# s = 'hello, WORLD! I am learn Python.'
# print(s.find('al'))
# print(s.rfind('al'))
# print(s.index('l'))
# print(s.rindex('l'))


# s = "Some content in this message has been blocked because the sender isn't in your Safe senders list"
# item = "o"
# if s.count(item) == 1:
#     print(s.find(item))
# elif s.count(item) >= 2:
#     print(s.find(item), s.rfind(item))


# s = 'hello, WORLD! I am learn Python.'
# print(s.endswith('on.'))
# print(s.endswith('lo', 3, 5))
#
# print(s.startswith('hello'))
# print(s.startswith('I am', 14))

# print('aab123'.isalnum())   # не пустая и состоит из букв или цифр
# print('45%6'.isalnum())
#
# print('ABCabc'.isalpha())   # не пустая и содержит только буквы
# print('123abc'.isalpha())
#
# print('123'.isdigit())   # не пустая и содержит только цифры
# print('ывав1'.isdigit())
#
# print('abc'.islower())   # не пустая и содержит только буквенные символы в нижнем регистре,
# # также содержит спецсимволы и цифры
# print('abc@98'.islower())
#
# print('ABC'.isupper())   # не пустая и содержит только буквенные символы в верхнем регистре,
# # также содержит спецсимволы и цифры
# print('ABC1^q'.isupper())

# print(' \t \n '.isspace())   # строка состоит только из пробельных символов + табуляция и перенос на другую строчку
# print(' a '.isspace())

# print('py'.center(10))
# print('py'.center(11, '-'))
# print('py'.center(2))


# ПРИМЕНЯЕТСЯ ЧАЩЕ, ЧЕМ ТЕ ЧТО БЫЛИ ВЫШЕ
# print('    py'.lstrip())   # py
# print('py    '.rstrip())   # py
# print('     py    '.strip())   # py
#
# print('https://www.python.org/'.lstrip('th/sp:'))
# print('$py.$$$;'.rstrip(';$.'))
# print('$py.$$$;'.strip(';$.'))
# print('https://www.python.org/'.lstrip('th/sp:').rstrip('/.org'))

# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New'
# print(str1.replace('Nython', 'Python', 2))


# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))   # a-b-c
# print('. .'.join(['1', '2']))
# print(':'.join('Hello'))

# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split('.', 1))
# print('www.python.org.ru'.rsplit('.', 1))
# print('www...python...org'.rsplit('.'))

# a = input('-> ').split()
# print(a)


# def name(name):
#     print(f'{name[0]} {name[1][0]}. {name[2][0]}.')
#
#
# a = input('Введите ФИО: ').split()
# name(a)


# s = 'В строке заменить пробелы пробелы символом'
# lst = s.split()
# print(lst)
# st = "*".join(lst)
# print(st)
# # второй способ
# print(s.replace(' ', '*'))
