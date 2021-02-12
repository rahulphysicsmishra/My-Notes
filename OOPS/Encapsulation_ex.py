class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

print(ford.get_speed())
ford.set_speed(300)
print(ford.get_speed())

# To make our attribute private so that we won't be able to change
# the data through set_speed method, we will make our attribute private
# using double underscore

# 2nd example

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 15
        self.__c = 20

    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Hello('Rahul')
print(hello.a)  # a is a public member variable and shows that we can use it inside as well as outside of class
hello.public_method()  # this proves that we can use private member inside the public method of class and we can use
                       # we can call private method inside class... but we cannot call private method outside the class
#  hello.__private_method() ---- This will throw error

