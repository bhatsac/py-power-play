
#Variables and Python Memory Management
5+6
x=5
y=6
print(x+y)
z=5
print(id(x)) #Here z and x are having same memory address
print(id(z))
print(id(y)) # Here y has different memory address.
print(id(6))

#id() is an inbuilt function in Python.
# As we can see the function accepts a single parameter and is used to return the identity of an object.
# This identity has to be unique and constant for this object during the lifetime.
# Two objects with non-overlapping lifetimes may have the same id() value.