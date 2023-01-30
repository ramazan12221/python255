from math import sqrt


class Rectangle:
    def __init__(self, d=0, v=0):
        self.__d = d
        self.__v = v

    def get_d(self):
        return self.__d

    def get_v(self):
        return self.__v

    def set_rectangle_area(self):
        s1 = self.__d * self.__v
        print("Площадь прямоугольника:", s1)

    def square(self):
        s2 = (self.__d + self.__v) * 2
        print("Периметр прямоугольника:", s2)

    def hypotenuse(self):
        s3 = sqrt(self.__d ** 2 + self.__v ** 2)
        print("Гипотенуза прямоугольника:", round(s3, 2))

    def figura(self):
        for i in range(self.__d):
            for J in range(self.__v):
                print("*", end="")
            print()


p = Rectangle(3, 9)
print("Длинна прямоугольника:", p.get_d())
print("Ширина прямоугольника:", p.get_v())
p.set_rectangle_area()
p.square()
p.hypotenuse()
p.figura()
