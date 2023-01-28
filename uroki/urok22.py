# import os
# print(os.path.join("D:\pathonкурсы", "uroki", "test", "nested2", "nested3", "1.txt"))

# задача: создать дерево директорий и файлов, выполнить обход дерева снизу верх, а затем сверху вниз и вывести результат
# dirs = ['Work/F1', 'Work/F2/F21']
# # for dir in dirs:
# #     os.makedirs(dir)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work\\F2\\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Некоторый текст в файле {file}.")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)


# 2
# print(os.path.exists(r"D:\pathonкурсы\uroki\test\nested2\nested3\1.txt"))  # проверка на существование
# # файла по заданному пути
# path = 'file.txt'
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу (в секундах)
# print(os.path.getmtime(path))  # возвращает время последнего изменения к файлу (в секундах)
# print(os.path.getctime(path))  # возвращает время создания файла (в секундах)
# print(os.path.getsize(path))  # возвращает размер файла (в байтах)


# 3
# import time
# path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1" \
#        r"\plugins\python-ce\helpers\typeshed\stdlib\socket.pyi"
# size = os.path.getsize(path)
# k_size = size // 1024
# print("Размер", k_size, "KB")
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))


# 4 является ли путь фалом или директорией
# print(os.path.isfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1" \
#        r"\plugins\python-ce\helpers\typeshed\stdlib\socket.pyi"))
# print(os.path.isdir(r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1" \
#        r"\plugins\python-ce\helpers\typeshed\stdlib"))


# 5 ООП (объектно-ориентированное программирование)
# Внутри класса могут быть свойства(поля) == переменные, методы == функции и атрибуты = свойства + методы

# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_coords()
# Point.set_coords(p1)
# Point.x = 100
# print(type(p1))
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))
# print(p1.__dict__)
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p2 = Point()
# p2.set_coords()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)
#
# Point.set_coords(p2, 2, 7)
# print(p2.__dict__)


# задача
# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}"
#               f"\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, countre, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = countre
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Полина")
# print(h1.get_name())
# h1.set_birthday("12.04.2021")
# print(h1.get_birthday())
