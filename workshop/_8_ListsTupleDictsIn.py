""" This section we will be discussing about list """
lists = ['India', 'usa', 22, '23', 'python']
# List is mutable while looping
print(lists[2])
print(len(lists))

# Insert
lists.insert(0, "gogo")
print(lists)

# Remove
lists.remove(22)
print(lists)

# Add two lists
a = [4, 5, 6]
b = [1, 2, 3]
print("Printing the concatenated list {0}".format(a + b))
# append the list within the list.
b.append(a)
print(b)
# pop
print(lists.pop())
print(lists)

# Deleting the list
# del lists
# lists.clear()
# Sort
lists.sort()
print(lists)  # will throw if there are ints and strings mixed up in the list
m = [1, 22, "sac"]
# print(m.sort())  # this is throwing error since strings and numbers are mixed up

# Count
lists.insert(0, 'India')
print(lists.count('India'))

"""
We will be discussing on Tuples
Tuples are immutable , so we cannot insert,pop,remove
Tuples are oldered 
"""

tuples = ("ewq", 2, "sad", "bhat", "sac", [23, 3], 3)
tuples2 = (2, 3, 45, 4)
print(tuples[2])
print(tuples.count(3))
tupleConcatenated = tuples+tuples2
print(tupleConcatenated)
# Single element tuple
single_element = (10,)
print(single_element)
# Multiplier tuple
single_element = single_element*100
print(single_element)
# Del
del single_element

# Dictionaries
dicts = {1: "sac", 2: "bhatsac", 3: "kee", 4: "so"}
print("Getting values from dict using key ", dicts[2])
print("Popping a value from dictionary using a key ", dicts.pop(4))
print("printing the dicts directly", dicts)
print(dicts.items())
dicts[5] = "yooooooo"
dicts[2] = "sooooooo"
dicts.update({1: "India"})
print(dicts)
print(dicts.keys())
print(dicts.values())

# Indexing, Slicing, Negative dict_items([(1, 'sac'), (2, 'bhatsac'), (3, 'kee')])Indexing

"""
a[start:end] #items from start to end-1
a[start:] #rest of the array
a[:end]  #items from beginning to end-1
a[:] #copy of whole array
a[start:end:step] # start through the end-1 of the array with the specified step. 
|  P  |  Y  |  T  |  H  |  O  |  N  |
|  0  |  1  |  2  |  3  |  4  |  5  |
| -6  | -5  | -4  | -3  | -2  | -1  |
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19]

py = "python"

print(a[3:9])
print(a[:12])
print(a[5:])
print(a[:])
print(a[::2])
print(py[-6::])  # First index should always be smaller than the second one.
print(py[5:0:])  # Does not print anything
print(py[5::-1])  # This prints, it works here because we have negative stepping
print(py[-3:-6:])  # Dose't print anything
print(py[-3:-6: -1])


"""
|  K  |  E  |  E  |  R  |  T  |  H  |  I  |
|  0  |  1  |  2  |  3  |  4  |  5  |  6  |
| -7  | -6  | -5  | -4  | -3  | -2  |  -1 |
"""
name = "keerthi"
print(name[::-1])
print(name[-7::-1])  # prints k
print(name[6::-1])

print(name[6:1:-1])
