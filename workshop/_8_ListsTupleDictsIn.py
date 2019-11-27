lists = ['India', 'usa', 22, '23', 'python']
# List is mutable while looping
print(lists[2])
print(len(lists))
#Insert
lists.insert(0, "yoyo")
print(lists)
#remove
lists.remove(22)
print(lists)
#pop
print(lists.pop())
print(lists)
#Deleting the list
#del lists
#lists.clear()
#Sort
lists.sort()
print(lists) #will throw if there are ints and strings mixed up in the list
#Count
lists.insert(0,'India')
print(lists.count('India'))

"""
We will be discussing on Tuples
Tuples are immutable , so we cannot insert,pop,remove
Tuples are oldered 
"""

tuples =("ewq",2,"sad","bhat","sac",[23,3],3)
tuples2 =(2,3,45,4)
print(tuples[2])
print(tuples.count(3))
tupleConcatenated=tuples+tuples2
print(tupleConcatenated)
#Single element tuple
singlelement=(10,)
print(singlelement)
#Multiplier tuple
singlelement=singlelement*100
print(singlelement)
#Del
del singlelement

#Dictionaries
dicts = {1:"sac",2:"bhatsac",3:"kee",4:"so"}
print(dicts[2])
print(dicts.pop(4))
print(dicts)
print(dicts.items())
dicts[5]="yooooooo"
dicts[2]="sooooooo"
dicts.update({1:"India"})
print(dicts)
print(dicts.keys())
print(dicts.values())

#Indexing, Slicing, Negative Indexing
"""
a[start:end] #items from start to end-1
a[start:] #rest of the array
a[:end]  #items from begining to end-1
a[:] #copy of whole array
a[start:end:step] # start through the end-1 of the array with the specified step. 
|  P  |  Y  |  T  |  H  |  O  |  N  |
|  0  |  1  |  2  |  3  |  4  |  5  |
| -6  | -5  | -4  | -3  | -2  | -1  |
"""
a=[1,2,3,4,5,6,7,8,9,0,12,13,14,15,16,17,18,19]
py ="python"
print(a[3:9])
print(a[:12])
print(a[5:])
print(a[:])
print(a[::2])
print(py[-6::])  #First index should always be smaller than the second one.
print(py[5:0:])  #Does not print anything
print(py[5::-1]) #This prints, it works here because we have negative stepping
print(py[-3:-6:]) # Dosend print anything
print(py[-3:-6: -1])
