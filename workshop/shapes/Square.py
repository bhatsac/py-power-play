from workshop.shapes.Polygon import Polygon
from workshop.shapes.Shape import Shape
class Square(Polygon,Shape):
    def area(self):
        return self.get_height()*self.get_width()