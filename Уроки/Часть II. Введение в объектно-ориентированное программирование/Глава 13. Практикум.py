# Третье задание
class Shape():
    def what_i_am(self):
        print("Я - фигура")

# Первое и второе задание
class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.lenght = l
        
    def calculate_perimeter(self):
        return 2 * (self.lenght + self.width)

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self):
        self.s1 = int(input("Введите сторону квадрата: "))

a_rectangle = Rectangle(3, 5)
a_square = Square(4)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
a_square.change_size()
print(a_square.s1)
a_square.what_i_am()
a_rectangle.what_i_am()

# Четвёртое задание
class Horse():
    def __init__(self,
                 name,
                 color,
                 rider):
        self.name = name
        self.color = color
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

a_rider = Rider("Даниил")
lastochka = Horse("Ласточка", "каштановый цвет", a_rider)
print(lastochka.rider.name)






















