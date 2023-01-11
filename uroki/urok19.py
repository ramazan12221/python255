import re
#
# text = """Python,
# python,
# PYTHON"""
# reg = '(?mi)^python'
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python_ma5st#er'))


# greedy - захватывает максимально возможное число символов
# ? - lazy - захватывает минимальное возможное число символов

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>изображение <img alt='картинка' src='bg.jpg' width='100'> - фон страницы</p>"
# # reg = '<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = "Методы этой группы[16] выполняют[17] преобразование регистра[18][19] строки"
# print(re.findall(r'\[.*?]', text))

# s = 'Петр, Ольга и Виталий отлично учатся'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r'(?:int|float)\s*=\s*\d[.\w+]*'
# reg = r'(int|float)\s*=\s*(\d[.\w+]*)'
# print(re.findall(reg, s))

# (?: ...) - обозначает, что эта группирующая скобка является не сохраняющей

# s = '127.0.0.1'
# # 192.255.255.255
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = 'Word2016, PS6, AI5'
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s, ))

# a = '31-08-2000'
# reg = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))


# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# # print(m[0])
# # print(m[1])
# # print(m[2])
# # print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))

# text = """
# Самара
# Москва
# Сочи
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print('<select>')
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))
# print('</select>')

# s = "<p>изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*(src=)(?P<q>[\'"])(.+)(?P=q)>'
# # (?P<name>)  (?P=name)
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.findall(reg, s))
# print(re.sub(reg, r"\2.\1.\3", s))

# s = 'google.com and google.ru'
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))


# def validate_phone(name):
#     reg = r'^\+?7[ (]*\d+[ )]*[\d -]{8,10}$'
#     return re.search(reg, name).group()
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))
