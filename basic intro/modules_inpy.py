##Math Module and Decimal Class
print(25-0.49999999)  # This is not accurate computation of decimal, so we use decimal class to do accurate computation.
from decimal import Decimal
valueDec1= Decimal('24.6')
valueDec2= Decimal('15.7')
print(valueDec1-valueDec2)

import math
math.pi


#Statistics Module - find mean and median
import statistics
print(statistics.mean((25,23,34,45,65)))


#Collections Module - deque for Queue and Stack
from collections import deque
deq=deque([25,43,1,54,56,34,223])
print(deq.pop())
print(deq)
deq.appendleft(45)
deq.append(101)
print(deq)

#Date Module

import datetime
dte=datetime.datetime.today()
print(dte)
print(dte.day)
print(dte.ctime())
print(datetime.datetime(1987,5,25,19,31))


#Methods and Arguments – Basics
def example_method(mandatory,default="Default",*variable,**keyword):
    print(f"""
              mandatory_args: {mandatory}
              default_args: {default}
              variable_args: {variable}
              keyword_args: {keyword}""")
example_method(24)
example_method(mandatory=24)
example_method(24,15)
example_method(24,15,1,2,3,4,5)
example_method(24,15,1,2,3,4,5,**{'key1':'a','key2':'b','key3':'c'})
example_method(mandatory=24,default=15,*(1,2,3,4,5),**{'key1':'a','key2':'b','key3':'c'})
