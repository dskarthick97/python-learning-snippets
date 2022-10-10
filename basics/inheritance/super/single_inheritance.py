
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # print(self)
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length + 2 * self.width)


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Rectangle):

    def __init__(self, length):
        # Rectangle.__init__(self, length, length)
        super(Square, self).__init__(length, length)
        # super().__init__(length, length)
        print(locals())


class RightPyramid(Square, Triangle):

    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + area


pyramid = RightPyramid(3, 5)
pyramid_area = pyramid.area()
print(pyramid_area)
