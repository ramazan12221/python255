# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже:"))
# elevator(n1)

# 1
# 2
# 3
# 4
# 5


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:  # базовый случай (условие выхода)
#         print(lst, "-> lst[0]", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "-> lst[0]", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 3 5 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789"
#     if n < base:
#         return convert[n]  # 3
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 6 5
#
#
# print(to_str(255, 16))  # 356


# def to_str(n, base):  # 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 15
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 15
#
#
# print(to_str(255, 16))  # FF


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
# # print(names[0])
# # print(isinstance(names[0], list))  # False
# # print(names[1])
# # print(isinstance(names[1], list))  # True
# # print(names[1][1])
# # print(isinstance(names[1][1], list))  # True
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))  # False
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:  # ""
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == 'l':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld "))


# Работа с файлами

# 1) Открытие файла
# 2) Выполнение операции с файлом (запись, чтение)
# 3) Закрытие файла

# f = open(r'D:\pathonкурсы\uroki\text.txt', 'r')
#
# # print(f.closed)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # print(*f)
#
# print(f.read(3))
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
#
# print(f.readlines(26))
#
# for line in f:
#     print(line)
#
# f.close()


# f = open(r'text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open("file.txt")
# print(len(f.readlines()))
#
# cnt = 0
# for line in f:
#     cnt += 1
# print(cnt)
#
# cnt = 0
# s = f.readline()
# while s != '':
#     s = f.readline()
#     cnt += 1
# print(cnt)
#
# f.close()


# f = open('xyz.txt', 'a')
# # f.write('Hello \nWorld')
# # print(f.write('\nNew text'))
# lines = ['This is line 1', 'This is line 2']
# f.writelines(lines)
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# # print(lst) ['10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211',
# # '1312', '1413', '1514', '1615', '1716', '1817', '1918']
# for index in lst:
#     f.write(index + "\t")
#
# f.close()


# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файле;")
# my_file.close()
#
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменение строки в списке;\n':
#         read_file[i] = 'Hello World\n'
# print(read_file)
# my_file.close()
#
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()
