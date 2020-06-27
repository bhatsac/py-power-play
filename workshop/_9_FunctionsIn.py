# Functions in Python.
def print_sum(arg1, arg2):
    print(arg1+arg2)

print_sum(2, 3)


def do_multiply(arg1, arg2):
    return arg1*arg2


result = do_multiply(2, 3)
print(result)


def sum_num(arg1, arg2):
    if type(arg1) == type(arg2):
        print(arg1+arg2)
    else:
        print("data types are different!")


sum_num(2, 5)  # sumsup
sum_num(2, 5.0)  # fails
sum_num('2', '5')  # string concats
"""
Arguments
Formal and Actual Arguments (arg, *arg, **karg)

There are 4 types of arguments
1. Positional arguments
2. Keyword Arguments
3. Default Arguments
4. Variable length Arguments


"""

# Positional Arguments


def shop(items, price=7):
    print("Item: ", items)
    print("price: ", price)


shop("banana", 2)

# here position matter and should be called in same order
# Keyword Arguments

shop(price=5, items="guava")


# Default Arguments
shop(items="mango")
shop(items="pineapple", price="20")


# Variable length Arguments
"""
std(name, cls, *marks)
* indicates there can be many values for the variable
** its a dict


"""


def std(name, cls, *marks):
    print("name",name)
    print("class", cls)
    for x in marks:
        print("marks: ", x, end="\t")


std("sac", 10, 100, 99, 100)


def std_map(name, cls, **marks ):
    print("name", name)
    print("class", cls)
    print("map", marks)


std_map(name="sac", marks={"eng": 100, "math": 99, "science": 100}, cls=10)

# Tuple
"""O/P
name sac
class 10
marks (100, 99, 100)
"""


def std_dict(name, cls, **marks):
    print("name", name)
    print("class", cls)
    for x, y in marks.items():
        print(x+"marks: ",   y, end="\t")


std_dict("sac", cls=10, Maths=100, Chemistry=99, Physics=100)

std_dict("sac", cls=11, marks={"Maths": 100, "Chemistry": 99, "Physics": 100})


# Local and Global Variables
m = 10
n = 20


def print_args(m, n):
    print(m)
    print(n)


print_args(30, 40)
print(m, n)