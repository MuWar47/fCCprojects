class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    self.area = self.width * self.height
    return self.area
  
  def get_perimeter(self):
    self.perimeter = 2 * self.width + 2 * self.height
    return self.perimeter
  
  def get_diagonal(self):
    self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return self.diagonal
  
  def get_picture(self):
    str1 = ''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      for lines in range(self.height):
        str1 += '*' * (self.width) + '\n'
    return str1
  
  def get_amount_inside(self, shape):
    area = self.get_area()
    shape_area = shape.get_area()
    if shape_area >= area:
      no_of_times = 0
    else:
      no_of_times = int(area / shape_area)
    return no_of_times

  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  
  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def __str__(self):
    return 'Square(side={})'.format(self.width)


