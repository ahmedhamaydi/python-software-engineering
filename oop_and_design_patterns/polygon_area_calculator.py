import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height 
    
    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return math.sqrt((self.width**2 + self.height**2))
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            result = ''
            result = ('*'*self.width + '\n') * self.height
            return result
    
    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width 
        height_fit = self.height // shape.height

        number_of_fits = width_fit * height_fit

        return number_of_fits
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.width = side_length
        self.height = side_length

    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length
    
    def set_height(self, side_length):
        self.width = side_length
        self.height = side_length
    
    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f'Square(side={self.width})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))