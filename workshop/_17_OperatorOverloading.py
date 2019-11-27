class Books:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages+other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __ge__(self, other):
        return self.pages > other.pages

b1 = Books(100)
b2 = Books(300)
# this throws an error, since b1 and b2 are objects but we can override to resolve this error using operator overloading
# Internal method we overload to do a.__add(b)
print(b1 + b2)
print(b1 * b2)
print(b1 >= b2)
