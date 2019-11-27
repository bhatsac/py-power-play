#compile time error
#Runtime error
#Logical error

x = 1
if x == 1:
    print("Hello world!")
    
    
#          Base Exception
#                |
#            Exception
#                |
#                |
#  ______________|_________________
# |                                |
# Standard Error                Warning
#
# Arithmetic Error              Deprecated Warning
# AssertionError                RuntimeWarning
# etc...

import builtins
help(builtins)  # this will show all the avilable exceptions.
x = 10
y = 0
result = None
try:
    result = x / y
except BaseException as e:
    print("Error in the code", e)
    print(type(e))

print(result)

m = input("Enter a number: ")
n = input("Enter a number: ")

try:
    m = int(m)
    n = int(n)
    result = m / n
except TypeError as e:
    print("Error in the code", e)
    print(type(e))
except ValueError as e:
    print("Error in the code", e)
    print(type(e))


#Try, Except, Else and Finally
# try:
#     <code goes here>
# except:
#     < code goes here >
#
# else:
#     < code goes here >
#
# finally:
#    < code goes here >
print("\n Try, Except, Else and Finally Demo:\n")

r = input("Enter a number: ")
s = input("Enter a number: ")
computed_value = None
try:
    r = int(r)
    s = int(s)
    computed_value = r / s
except TypeError as e:
    print("Error in the code", e)
    print(type(e))
except ValueError as e:
    print("Error in the code", e)
    print(type(e))
else:
    print("Program executed successfull without exception and valuse is : ",computed_value)
finally:
    print("resetting all the variables in finally")
    r = None
    s = None
    computed_value = None
# User defined Exception

class TeaException(Exception):
    def __init__(self,msg):
        self.msg = msg

# Raising Exception
i = input("Quantity: ")
j = input("Temperature: ")
raising_eceptions = None
def make_tea(i,j):
    i = int(i)
    j = int(j)

    if i <= 0:
        raise TeaException("Quantity should be greater than 0")
    elif j < 0 or j > 100:
        raise Exception("Temperature be in range 0 to 100")
    else:
        print("Tea done for ", i)

make_tea(i,j)