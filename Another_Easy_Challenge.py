class Circle:
    '''
    Attributes May Not Be Set To Private In Parent Class.
    Because By Then, They Will Be Uninheritable By Child Class.
    '''
    def __init__(self, radius = 3.5, color = 'Red'):
        self.rad = radius
        self.color = color

    def set_rad(self, input):
        self.rad = input

    def get_rad(self):
        return float(self.rad)

    def set_color(self, color_in):
        self.color = color_in

    def get_color(self):
        return self.color

    def get_area(self):
        import math
        return float(math.pi * (self.rad ** 2))

    def __str__(self):
        return f"Circle Properties:\nRadius = {self.rad}\nColor = {self.color}\nArea = {self.get_area()}"


class Cylinder(Circle):
    def __init__(self, radius = 3.5, color = 'Red', height = 5.5):
        super().__init__(radius, color)
        self.__height = height

    def set_height(self, new):
        self.__height = new

    def get_height(self):
        return self.__height

    def get_volume(self):
        import math
        return math.pi * (self.rad ** 2) * self.__height

    def to_string(self):
        return f"Cylinder Properties:\nRadius = {self.rad}\nColor = {self.color}\nHeight = {self.__height}"











    

    