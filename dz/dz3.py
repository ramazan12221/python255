# a = input('\n1)"r" - Применяет унарный минус'
#           '\n2)"+" - Сложение\n3)"-" - вычитание\n4)"/" - деление с остатком\n5)"*" - умножение'
#           '\n6)"%" - остаток от деления\n7)"<" - минимальное из двух чисел'
#           '\n8)">" - большое из двух чисел\nВВедите знак: ')
# if a == 'r':
#     try:
#         num1 = int(input('Введите число 1: '))
#         num2 = int(input('Введите число 2: '))
#         num1 = - num1
#         num2 = - num2
#         print('Результат: ', num1, 'и', num2)
#     except ValueError:
#         print('Вы ввели не число или число было не целым')
# else:
#     if a == '+':
#         try:
#             num1 = int(input('Введите число 1: '))
#             num2 = int(input('Введите число 2: '))
#             num3 = num1 + num2
#             print('Результат: ', num3)
#         except ValueError:
#             print('Вы ввели не число или число было не целым')
#     else:
#         if a == '-':
#             try:
#                 num1 = int(input('Введите число 1: '))
#                 num2 = int(input('Введите число 2: '))
#                 num3 = num1 - num2
#                 print('Результат: ', num3)
#             except ValueError:
#                 print('Вы ввели не число или число было не целым')
#         else:
#             if a == '/':
#                 try:
#                     num1 = int(input('Введите число 1: '))
#                     num2 = int(input('Введите число 2: '))
#                     num3 = num1 / num2
#                     print('Результат: ', round(num3, 2))
#                 except (ValueError, ZeroDivisionError):
#                     print('Вы ввели не число или число было не целым')
#             else:
#                 if a == '*':
#                     try:
#                         num1 = int(input('Введите число 1: '))
#                         num2 = int(input('Введите число 2: '))
#                         num3 = num1 * num2
#                         print('Результат: ', num3)
#                     except ValueError:
#                         print('Вы ввели не число или число было не целым')
#                 else:
#                     if a == '%':
#                         try:
#                             num1 = int(input('Введите число 1: '))
#                             num2 = int(input('Введите число 2: '))
#                             num3 = num1 % num2
#                             print('Результат: ', num3)
#                         except (ValueError, ZeroDivisionError):
#                             print('Вы ввели не число или число было не целым')
#                     else:
#                         if a == '<':
#                             try:
#                                 num1 = int(input('Введите число 1: '))
#                                 num2 = int(input('Введите число 2: '))
#                                 if num1 > num2:
#                                     print('Результат: ', num2)
#                                 else:
#                                     print('Результат: ', num1)
#                             except ValueError:
#                                 print('Вы ввели не число или число было не целым')
#                         else:
#                             if a == '>':
#                                 try:
#                                     num1 = int(input('Введите число 1: '))
#                                     num2 = int(input('Введите число 2: '))
#                                     if num1 > num2:
#                                         print('Результат: ', num1)
#                                     else:
#                                         print('Результат: ', num2)
#                                 except ValueError:
#                                     print('Вы ввели не число или число было не целым')
#                             else:
#                                 print('Математический знак введён неверно')
