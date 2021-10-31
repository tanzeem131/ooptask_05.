import math
class shape:
    def __init__(self, color='#'):
        self.__color = color

class circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.__r = radius
    def get_area(self):
        return math.pi * self.__r ** 2

class square(shape):
    def __init__(self, length):
        super().__init__()
        self.__l = length
    def get_area(self):
        return self.__l * self.__l

class rectangle(shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__l = length
        self.__b = breadth
    def get_area(self):
        return self.__l * self.__b

C = circle(10)
S = square(10)
R = rectangle(10, 5)

for x in (C,S,R):
    x.get_area()
    print(x.get_area())

