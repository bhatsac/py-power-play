#Basics of Exception Hierarchy
import builtins
help(builtins)

#Basics of Error Handling - try except

try:
    i=0
    j=10/i
except:
    j=0
print(j)
print("End of game!")


try:
    lists=[1,'2']
    sum(lists)
except TypeError:
    print("Type Error occured!")

try:
    div=10/0
    lists=[1,'2']
    sum(lists)
except TypeError:
    print("This except block cannot detect divide by zero error occured!")
except ZeroDivisionError:
    print("This except block can detect divide by zero !")

print("finally not here")

#Error Handling - Puzzles - Exception Details
try:
    div = 10 / 0
    lists = [1, '2']
    sum(lists)
except BaseException:
    print("This is a base execeptions cath")

try:
    div = 10 / 0
    lists = [1, '2']
    sum(lists)
except (TypeError,ZeroDivisionError):
    print("This is a TypeError/ZeroDivisionError execeptions cath")

try:
    div = 10 / 0
    lists = [1, '2']
    sum(lists)
except BaseException:
    print("This is a base execeptions cath")
except ZeroDivisionError:
    print("This is a ZeroDivisionError Execeptions cath")


try:
    div = 10 / 1
    lists = [1, '2']
    sum(lists)
except BaseException as error:
    print(error)
except ZeroDivisionError as error:
    print(error)


#Error Handling - finally and else
try:
    div = 10 / 1

except ZeroDivisionError as error:
    print(error)
else:
    print("This is else, executed when execption is not thrown")
finally:
    print("Finally is always executed.")


try:
    div = 10 / 0

except ZeroDivisionError as error:
    print(error)
else:    #This cannot be used wihtout execept block
    print("This is else, executed when execption is not thrown")
finally: #Try with only finally is allowed.
    print("Finally is always executed.")

#Raising Exceptions
class Currency:
    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount
    def __repr__(self):
        return repr((self.currency,self.amount))
    def __add__(self, other):
        if self.currency!=other.currency:
            raise Exception("Currencies do not match!")
        total_amount=self.amount+other.amount
        return Currency(self.currency,total_amount)

value1= Currency("USD", 2000)
value2= Currency("USD", 2000)

print(value1+value2)


#Raising Custom Exceptions

class CurrenciesDoNotMatchError(BaseException):
    def __init__(self,message):
        print("CurrenciesDoNotMatchError"+message)
class CustCurrency:
    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount
    def __repr__(self):
        return repr((self.currency,self.amount))
    def __add__(self, other):
        if self.currency!=other.currency:
            raise CurrenciesDoNotMatchError("Currencies do not match!")
        total_amount=self.amount+other.amount
        return CustCurrency(self.currency,total_amount)

value3= CustCurrency("USD", 2000)
value4= CustCurrency("INR", 2000)

print(value3+value4)
