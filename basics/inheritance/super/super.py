
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length + 2 * self.width)


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
        print(locals())


square = Square(4)
print(hex(id(square)))

area = square.area()
print(area)

perimeter = square.perimeter()
print(perimeter)
