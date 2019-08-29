# Первое задание
class Apple:
    def __init__(self, w, s, c, t):
        """вес в граммах"""
        self.weight = w
        """размер в сантиметрах"""
        self.size = s
        self.color = c
        self.taste = t
        print("Создано!")
Apple = Apple(200, 10, "красное яблоко", "сладкий вкус")

# Второе задание
import math
class Circle:
    def __init__(self, r):
        self.radius = r
        print("Круг создан")
    def area(self):
        pi = math.pi
        return round(pi*float(self.radius)**2.0, 2)

Circle = Circle(2)
print(Circle.area())

# Третье задание
class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.height = h
    def area(self):
        return self.a / 2 * self.height

Triangle = Triangle(4, 3)
print(Triangle.area())

# Четвёртое задание
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
Hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(Hexagon.calculate_perimeter())

















