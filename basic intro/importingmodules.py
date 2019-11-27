# Chap9 - L1
import math
print(math.floor(4.5))
# getting help for math.floor
help(math.floor)
help(math)

# this is not recomended but we can directly use the methods.
from math import *
print(floor(5.5))
print(gcd(7,49))

# Chap9 - L2 -- looping
number = [1,4,6,3,4]
for num in number:
    print(num)

for i,num in enumerate(number):
    print(f"{num}  is at index {i}")

values =list('aeiou')
print(values)
for i,str in enumerate(values):
    print(f"{str}  is at index {i}")

# Chap9 - L3 -- If short cut
isEvenNum=8
isEven=True if isEvenNum%2==0 else False
print(isEven)

# Python is Strongly Typed and Dynamic Language
print(type(2))
print(type(2.5))
print(type("sac"))
str="sac"
print(type(str))
str=2
print(type(str))
str=[1,2]
print(type(str))


# Beginners Mistakes – Shadowing sum here is a bultin fucntion if we declare a
# variable with sum then we will not be able to use global sum function.
print(sum([1,3,5]))
sum=10
print(sum)
del sum
print(sum([1,3,5]))

#PEP 8 python enhancement proposal.
#PEP20 - Zen of Python