# here workshop.shapes.Square is a file name and import Square is the file name
# from workshop.shapes.Square import Square
from workshop.shapes.Triangle import Triangle

from workshop.shapes.Square import Square


# https://stackoverflow.com/questions/34384205/python-module-object-is-not-callable

s1 = Square()
s1.set_value(8,15)
s1.set_color("Blue")
print(s1.area() , s1.get_color())
t1 = Triangle()
t1.set_value(8,15)
s1.set_color("Red")
print(t1.area(),t1.get_color())


