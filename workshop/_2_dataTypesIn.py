# Python has 2 datatypes , bultin data types and user defined data types.
""""
    # Built-in data are of 5 types
    # None
    # Numeric
    # Sequences
    # Sets
    # Mapping
"""
## None
print(None)  #here the N is cap, equivalent to null in java
x = None
print(type(x))

# Numeric has 3 tyoes Int Float complex bool
a = 50
print(type(a))
b = 50.5656
print(type(b))
c = 50.5656 + 50j
print(type(c))
d = True
e = False
print(type(d))
print(type(e))

# Sequences String, List , Tuple, Range
my_name = "sachin"
my_name_other_format = 'sachin'
print(type(my_name))
print(id(my_name))
print(id(my_name_other_format))

# Lists
my_list = [1,2,3,4,5,6]
print(my_list)
print(type(my_list))
print(my_list[0]) #This is indexing.

# Tuples,
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
# Creating a tuple is as simple as putting different comma-separated values
my_tuples = (0,2,'as')
print(my_tuples)
print(type(my_tuples))
print(my_tuples[0])

# Range
r = range(1,10,2)  # range(1,10,2) : start with 1 , end with 10-1 , with a increment of 2
q = list(r)  # Converting the R to print.
print(r)  # just prints the range
print(q)

range_gen_list=list(range(1,100,5))
print(range_gen_list)

# sets , we cannot index a set as it does not maintain the order, s[0] is not posible
s = {10, 23, 12, 12, 11}
print(s)
print(type(s))
setToList = list(s)
print(setToList)

#Dictionary
dictionary= {10:"sachin",11:"bhat"}
print(dictionary)
#print(dictionary[0]) does not work
print(dictionary[10])


#Literals and identifiers.
k=15 #here 15 is literal and a is identifiers

#There are 3 types pf literals

#Numeric
#Boolean
#String

#Numeric
k=15
g=5.3
i=1010101
s=0X1A12
print(s)