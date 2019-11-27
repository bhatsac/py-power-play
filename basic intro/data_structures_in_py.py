mark1=50
mark2=60
mark3=60
avg= (mark1+mark2+mark3)/3
print(avg)

#so lets say we now have mark4
mark4=70
#here we need to change the denominator in the formula.
marks=[mark1,mark2,mark3,mark4]
new_avg=sum(marks)/len(marks)
print(new_avg)

#here we can append and still the formula is generic.
marks.append(90)

new_avg=sum(marks)/len(marks)
print(new_avg)

print(max(marks))
print(min(marks))

marks.insert(2,99)
print(marks)

print(marks.index(90))
print(marks.remove(90))
for mark in marks:
    print(mark,end=" ")
    print()



#Excercise
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_number_of_marks(self):
        return len(self.marks)
    def get_avg(self):
        return sum(self.marks)/self.get_number_of_marks()
    def get_max(self):
        return max(marks)
    def get_min(self):
        return min(self)


stu1=Student("sac",[65,76,51,99])
print(stu1.get_number_of_marks())
print(stu1.get_avg())
print(stu1.get_max())
#""" quotes allows us to add string in multiple lines.
print(f""" STUDENT [
        total no of subjects attended {stu1.get_number_of_marks()},
        Avg of total marks {stu1.get_avg()}
        Max marks obtained in  {stu1.get_max()}
        ]""")


#Puzzles with string
animals=['Cat','Dog','Elephant']
print(animals[1])
del animals[2]
animals.remove('Dog')
print(animals)
animals.append('Fish')
animals.extend(['Horse','Monkey'])
print(animals)
#Other different ways to append the list.
animals =animals + ['Kangaroo']
animals +=['Deer']
print(animals)
# there is no restriction of data type in the list. we can add anything.
animals.append(10)
print(animals)

#List Slicing
print(animals[2:5]) # starts at index 2 and ends at 5
print(animals[:3]) #starts from beginning and ends at index 3
print(animals[3:]) # starts at index and ends at the end of the list
print(animals[0::2]) #skips every 2nd element and prints rest
print(animals[::-1]) # prints in the reverse order.
del animals[6:7] # deleting the element at particular indexes.
print(animals)
animals.append(10)
print(animals)
animals[5:7]=['Tiger',12] #replaceing part of the  list with another list
print(animals)

#List sorting ,reverrsing, looping
numbers = [1,4,5,2,7,8,0,10,23,55,24,50,12]
print(numbers)
numbers.reverse() # will reverse the list itself
print(numbers)
numbers.reverse()
for rev in reversed(numbers):
    print(rev)

print(numbers)
numbers.sort()
print(numbers) #in place sort, original array is sorted.
for sor in sorted(numbers):
    print(sor,end="|")
print()
special_num=['One','Two','Three','Four','Five','Six']
for sor2 in sorted(special_num,key=len):
    print(sor2, end="!")
print()
for sor3 in sorted(special_num,key=len, reverse=True):
    print(sor3, end="!")
print()
special_num.sort(key=len,reverse=True) #In place reverse
print(special_num)


nums=[]
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
nums.append(6)

print(nums.pop())


print(nums.pop(0))

#custom class for lists
class Country:
    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area
    def __repr__(self):  #This is a kind of toString type method in python
        return repr((self.name,self.population,self.area))


countries =[Country("India",125,300)
            ,Country("USA",0.325,900)
            ,Country("UK",0.02,0.010)]
countries.append(Country("Russia",16,1500))
print(countries)
import operator
#Sort with particular key
countries.sort(key=operator.attrgetter('population'))
print(countries)
countries.sort(key=operator.attrgetter('area'),reverse=True)
print("Hello")
print(countries)

#list Comprehension

print(special_num)
special_nums_of_size_four=[]
for numsof in special_num:
    if (len(numsof)==4):
        special_nums_of_size_four.append(numsof)

print(special_nums_of_size_four)

special_nums_of_size_four=[]
special_nums_of_size_four =[numi for numi in special_num]
print(special_nums_of_size_four)
special_nums_of_size_four=[]
special_nums_of_size_four=[len(numi) for numi in special_num]
print(special_nums_of_size_four)
special_nums_of_size_four=[numi.upper() for numi in special_num]
print(special_nums_of_size_four)
special_nums_of_size_four=[numi for numi in special_num if len(numi)>=4]  # this is called list comprehension.
print(special_nums_of_size_four)
special_nums_of_size_four=[numi for numi in numbers if numi%2==0]
print(special_nums_of_size_four)
special_nums_of_size_four=[numi for numi in numbers if numi%2!=0]
print(special_nums_of_size_four)

#Set in python
set_demo_list_numbers=[1,2,3,2,4,4,5]
print(set_demo_list_numbers)
set_demo=set(set_demo_list_numbers)
print(set_demo)  #Doesnot contain duplicates and does not support index.
print(max(set_demo))
set_demo_list_numbers2=set([4,5,6,7,8,9,10])
print(set_demo | set_demo_list_numbers2) #Union
print(set_demo & set_demo_list_numbers2) #Intersection
print(set_demo - set_demo_list_numbers2) #

#Dictionary , its represented by key value pair
occurances = dict(a=5,b=7,c=4,d=0)
print(occurances)
print(occurances.get('a'))
print(occurances.items()) # returns tuples
occurances['a']=10

for (key,value) in occurances.items():
    print(f"key {key} value {value}")

del occurances['a']
print(occurances.items())

#Excersice
str="This is an awesome occassion, i am having a great vacation year"
char_occurances={}
for individual_char in str:
    char_occurances[individual_char]=  char_occurances.get(individual_char,0)+1

    print(individual_char,end=" ")
print()
print(char_occurances)



#Puzzles
strpuzz="This is an awesome day. I am learining something new"
squares_of_first_ten_numbers=[i*i for i in range (1,11)] #This is list comprehension
type(squares_of_first_ten_numbers)
print(squares_of_first_ten_numbers)

squares_of_first_ten_numbers_set = set(squares_of_first_ten_numbers)
print(squares_of_first_ten_numbers_set) # To convert list to set
squares_of_first_ten_numbers_set2= {i*i for i in range(1,11)} # Set comprehension, this is similar to list comprehension
print(squares_of_first_ten_numbers_set2)
squares_of_first_ten_numbers_dict = {i:i*i for i in range(1,11)} #Dict coprehension
print(squares_of_first_ten_numbers_dict)
print(type([]))
print(type({}))
print(type(()))


#Tuples in python
def tuple_demo():
    return 'sac','kee',1+1
tuple_var=tuple_demo()
print(type(tuple_var))
print(tuple_var)
print(tuple_var[2])
var1,var2,var3 =tuple_var
print(var1)
print(var2)
print(var3)

# create a tuple using one values
var4 = (0,)
print(type(var4))
var5 =0
var6 =1
print(f"bef: var5 : {var5} , var6 : {var6}")
var5, var6= var6,var5
print(f"aft: var5 : {var5} , var6 : {var6}")
#cannot change the value of tuple using index but can access using index, tuple is unmodifiable







