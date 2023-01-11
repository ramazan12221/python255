# Задание 1 объединить 3 словаря в один
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# print({**a, **b, **c})


# Задание 2 изменить зарплату Брэду с 6500 до 8500
# d = {
#      "emp1": {"name": 'Jhon', "salary": 7500},
#      "emp2": {"name": 'Enna', "salary": 8000},
#      "emp3": {"name": 'Brad', "salary": 6500},
# }
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
# for x in d:
#      print(x)
#      for y in d[x]:
#           print(y, ": ", d[x][y], sep="")


# Задание 3 выводить имена студентов, чей балл выше среднего
# stud = int(input("количество студентов: "))
# res = 0
# d = {}
# for i in range(stud):
#     name = input(str(i+1) + '-й' + ' студент ')
#     ball = int(input("Балл :"))
#     res += ball
#     sr_ball = res/stud
#     d[name] = ball
# print('Средний балл: ', round(sr_ball), '. Студенты с баллом выше среднего:', sep='')
# for k, v in d.items():
#     if v > sr_ball:
#         print(k)
