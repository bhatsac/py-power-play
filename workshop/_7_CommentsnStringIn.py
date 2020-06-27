# This is how you do comments in python
print("This is 1")
# print("This is 2")
print("This is e")  # this is e
# Below is multi line comment also called doc string used for the purpose of documentation.
"""
This is called doc string comment
This will comment multi lines comment
"""


# String deep dive
""" Check for other string functions available in python  """
x = "hello world"
y = "HELLO WORLD "
print(x.isprintable())
print(x[0])
print(x[1])
print(x[0:6])  # This is called Slicing
print(y * 100)  # Print 100 times
z = "                 INDIA                         "
print(z.strip())
print(z.rstrip())
m = "This is awesome thing"
print(m.split(" "))
n = m.split(" ")
print(type(n))
