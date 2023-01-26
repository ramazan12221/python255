# 1: удаление элемента из текстового документа
# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файле;")
# my_file.close()
#
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# pos = int(input("ВВедите индекс строки для удаления: "))
# if 0 <= pos <= len(read_file):
#     del read_file[pos]      # del - удаление
# else:
#     print("Индекс введен неверно")
# print(read_file)
# my_file.close()
#
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()


# 2: чтение символов из документа, показывает на какой позиции стоит курсор, перемещение курсора на 1 позицию,
# откуда считываем и где оказался курсор после считывания всего файла
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# 3: новые режимы и методы протестировали
# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# print(f.write("-PYTHON-"))
# print(f.tell())
# f.close()


# 4: для with не надо в конце закрывать файл, он делает это сам
# with open("text.txt", 'w+') as f:
#     print(f.write("0123456789"))
#
# with open("text.txt", 'r') as f:
#     for line in f:
#         print(line[:6])


# 5: преобразовали список вещественных чисел в строку и записали его в новый документ,
# к документу мы обратились через переменную.
# метод write работает только с типом данных str
# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# print(get_line(lst))
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")


# 6(задача): из текстового файла(5:) вывели на экран вещественные числа и посчитали их кол-во,
# преобразовали список строк в список вещественных значений
# file_name = "res.txt"
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# num_list = list(map(float, nums.split()))
# print(num_list)
# print(len(num_list))


# 7(задача): функция, которая выводит из файла слово, с самой большой длиной,
# если слов несколько таких, то вывести их список
# with open("test.txt", 'r', encoding='utf-8') as f:
#     w = f.read().split()
#     print(w)
#     # 1
#     max_length = len(max(w, key=len))
#     # 2
#     # max_length = max(len(word) for word in w)
#     print(max_length)
#     res = [word for word in w if len(word) == max_length]
#     print(res)


# 8: работа с 2-мя файлами
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
#
# with open(write_file, 'r') as fw:
#     for line in fw:
#         print(line, end="")


# 9(задача): в текстовом файле посчитать кол-во строк и для каждой строки посчитать слова и символы
# f = open("test.txt", 'r', encoding='utf-8')
# line = 0
# for i in f:
#     line += 1
#     word = 0
#     flag = 0
#     for j in i:
#         if j != " " and flag == 0:
#             word += 1
#             flag = 1
#         elif j == " ":
#             flag = 0
#     print(i, len(i), "символов", word, "сл.")
#
#
# print(line, "строки")
# f.close()


# 10: Модуль os и os.path
# import os
# import os.path
# print("Текущая директория:", os.getcwd())
# print(os.listdir())  # вернулся список файлов и папок, находящихся в текущей директории (по умолчанию) или в
# # директории по указанному пути
# print(os.listdir(".."))

# os.mkdir("folder")  # создает директорию по указанному пути

# os.makedirs('nested1/nested2/nested3')  # создание вложенных папок
# os.makedirs('nested1/nested2/nested4')  # создание вложенных папок

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименование папки (файла)

# os.rename("test.txt", "test/test1.txt")

# os.renames("text.txt", "text/text1.txt")

# os.rmdir("folder")  # удаление пустой папки

# for root, dirs, files in os.walk("test", topdown=True):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"и"
#                   f"Директория {root} удалена/")
#
#
# remove_empty_dirs('test')


# print(os.path.split(r"D:\pathonкурсы\uroki\test\nested2\nested3\1.txt"))  # разбивает путь на кортеж (head, tail)
#
# print(os.path.dirname(r"D:\pathonкурсы\uroki\test\nested2\nested3\1.txt"))  # доступ к пути документа
# print(os.path.basename(r"D:\pathonкурсы\uroki\test\nested2\nested3\1.txt"))  # доступ к самому документу
