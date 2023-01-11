# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print("c =", c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# c = []  # 1 3 ... 4
# for i in a:
#     if i not in c:
#         c.append(i)
#     else:
#         if i in c:
#             i = c.index(i)  # УДАЛЯЕТ ПОВТОРНУЮ 6 ПОСЛЕ 1 И 2 ИЗ СПИСКА C
#             del c[i]
# print(c)
