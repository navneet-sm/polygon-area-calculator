class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        picture = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                picture += ('*' * self.width) + '\n'
            return picture
        else:
            return 'Too big for picture.'
        
    def get_amount_inside(self, shape):
        amount = int(self.get_picture().count('*') / shape.get_picture().count('*'))
        if amount >= 0:
            return amount
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    
class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def set_width(self, width):
        self.side = width
        
    def set_height(self, height):
        self.side = height
        
    def __str__(self):
        return f'Square(side={self.side})'