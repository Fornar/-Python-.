# Первое и второе задание
class Square():
    square_list = []
    def __init__(self, s):
        self.s = s
        self.square_list.append(self)
        
    def __repr__(self):
        return "{} на {} на {} на {}".format(self.s, self.s, self.s, self.s)

a_square1 = Square(27)
a_square2 = Square(10)
a_square3 = Square(45)
print(Square.square_list)

print(a_square2)

# Третье задание
def compare(a, b):
    return a is b

print(compare(13, "string"))
square = a_square2
print(compare(square, a_square2))
