class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages+other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __ge__(self, other):
        return self.pages > other.pages


# polymorphic behaviour of the + operator based on the datatypes

num_a = 10
num_b = 20

print("demonstrating number overloading a + b ", num_a + num_b)

str_p = "Hello "
str_q = "World!"

print("demonstrating string overloading a + b ", str_p + str_q)

list_m = [1, 2, 3, 4, 5]
lint_n = [6, 7, 8, 9, 10]

print("demonstrating list overloading a + b ", list_m + lint_n)

# we can overload few internal methods to apply polymorphic behaviour on user defined classes.
b1 = Books(100)
b2 = Books(300)
# this throws an error, since b1 and b2 are objects but we can override to resolve this error using operator overloading
# Internal method we overload to do a.__add(b)
print(b1 + b2)  # What happens here is b1.__add__(b2)
print(b1 * b2)  # What happens here is b1.__mul__(b2)
print(b1 >= b2)  # what happens here is b1.__ge__(b2)
