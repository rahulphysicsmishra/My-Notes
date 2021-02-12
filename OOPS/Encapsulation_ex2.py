class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

ford = Car(200, 'red')
ford.set_speed(300)
ford.__speed = 400  # not working now bcos speed is private
print(ford.get_speed())  # with set, get method, we can access private attribute speed
#  print(ford.color)  # color is private, we can't access without set,get method


# 2nd example

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def area(self):
        return self.__height * self.__width

rec1 = Rectangle(10,15)
print(rec1.area())

rec1.set_width(25)
rec1.set_height(20)
print(rec1.area())