class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length+self.width)


class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

    # def area(self):
    #     return self.length * self.length


square_1 = Square(7)
print(square_1.area())

rectangle_1 = Rectangle(5,7)
print(rectangle_1.perimeter())

