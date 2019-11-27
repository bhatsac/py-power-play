#Inheritance
class Ploygon:
    __width = None
    __height = None
    def set_value(self,height,width):
        self.__height=height
        self.__width=width

    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width

class Square(Ploygon):
    def area(self):
        return self.get_height()*self.get_width()



s1=Square()
s1.set_value(10,5)
print(s1.area());