#Output Styles in python
print("Hello World")
x=10
y=20
print("Multiplication of x and y is",x*y)

print("Multiplication of {0} and {1} is {2}".format(x,y,x*y))
floats=25.5374324
ints=3
print("This is a sample demo %.2f  and %d" % (floats , ints))

#Input Statements in Python
my_name=input("Please enter your name?\n")
print(my_name)

#Python Built-in Functions and Built-in Module
print(dir(__builtins__))
print(max(45,5,67,7,8))

#modules
help('modules')
import math
print(math.sqrt(2))
print(dir(math))