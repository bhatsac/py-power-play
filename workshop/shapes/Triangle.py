from  workshop.shapes.Polygon import Polygon as Ply
from  workshop.shapes.Shape import Shape
class Triangle(Ply,Shape):
    def area(self):
        return self.get_height()*self.get_width()*1/2