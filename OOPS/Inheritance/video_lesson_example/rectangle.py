from polygon import Polygon
from video_ex_multiple_inheritance import Shape

class Rectangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()