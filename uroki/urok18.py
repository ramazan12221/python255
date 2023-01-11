# Регулярные выражения
# import re

# s = 'Я ищу сов[паден]ия в 2021 го-да. И я иx найду в 2 счёта. 45678'
# # reg = r'[201]'
# # print(s.find(reg))
# # print(re.findall(reg, s))   # возвращает список, содержащий все совпадения
# # print(re.search(reg, s))   # возвращает первое совпадение
# # print(re.search(reg, s).span())   # (15, 16)
# # print(re.search(reg, s).start())   # 15
# # print(re.search(reg, s).end())   # 16
# # print(re.search(reg, s).group())   # я
# #
# # print(re.match(reg, s))   # для поиска по заданному шаблону в начале строки
#
# # print(re.split(reg, s))
# # print(re.split(reg, s, 1))
#
# # print(re.sub(reg, '!', s, 1))
#
# # [] - любой из символов
# # print(re.findall(reg, s))
#
# # reg = r'[12][0-9][0-9][0-9]'
# # print(re.findall(reg, s))
#
# reg = r'[А-яё]'
# print(re.findall(reg, s))
#
# reg = r'[А-яё.\[\]-]'
# print(re.findall(reg, s))
#
# s = 'Еда, беду, победа'
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 года. И я иx найду в 2 счёта. 45678'
# reg = r'[^0-9]'
# # [^abc] - вернёт все, за исключением abc
# print(re.findall(reg, s))

# s = 'Час в 24-часовом формате от 00 дл 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09.'
# reg = '[0-2][0-4]:[0-5][0-9]'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 года. И я \tиx найду в 2 счё_та.\n 45678'
# reg = r'20*'
# \d - одна цифра [0-9]
# \w - цифра, буква, символ _ [0-9А-яA-z_]
# \s - пробельный символ (включая табуляцию(\t) и перенос строки(\n))
# \D - все кроме цифр [^0-9]
# \W - все кроме цифр, букв, символа _ [^0-9А-яA-z_]
# \S - все кроме пробельного символа (включая табуляцию(\t) и перенос строки(\n))
# print(re.findall(reg, s))
# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - 0 или 1

# d = 'Цифры: 7, +17, -42, 0013, 0.3'
# reg1 = r'[+-]?[\d.]+'
# print(re.findall(reg1, d))

# s = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub('#.*', '', s))
# print('Дата рождения:', re.sub('-', '.', re.sub('#.*', '', s)))

# s = 'author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831'
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))

# s = '12 сентября 2021 года 789'
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 года. И \tя иx найду в 2 счё_та'
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
#
# text = 'hello world'
# print(re.findall(r'\w+', text, flags=re.DEBUG))

# s = 'Я ищу совпадения в 2021 года. И \tя иx найду в 2 счё_та'
# reg = r'я'
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text, ))
# print(re.findall(r'one$', text, flags=re.MULTILINE))

# print(re.findall("""
# [a-z.-]+   # part1
# @          # @
# [a-z.-]+   # part2
# """, 'text@mail.ru', re.VERBOSE))
