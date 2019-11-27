#Classes and Objects in Python (OOP)
class Student:
    def __init__(self):
        self.name="Sachin"
        self.age=20
        self.marks=25

    def talk(self):
        print("Name-", self.name)
        print("Age-", self.age)
        print("Marks-", self.marks)

s1 = Student();
s1.talk();
s1.name="Keerthi"
s1.talk();

#Understanding init() Method and 'self ' Parameter
#self contains the memory of the object which is created.


#nm= input("Enter your name: ")
#age= input("Enter your age: ")
#cls= input("Enter your class: ")
class ConstructStu:
    def __init__(self,nm,age,*cls):
        self.name=nm
        self.age=age
        self.cls=cls

    def display(self):
        print(""" name  : {0} \n age   : {1} \n class : {2}
            """.format(self.name,self.age,self.cls))

constu= ConstructStu("sac",22,"Btech")  #ConstructStu(nm,age,cls)
constu.display()

"""
There can be only one constructor in python
we can use an keyword instead of self, which is the standard
Below we use this instead of self
def __init__(this,nm,age,*cls):
"""

#Encapsulation
"""
We can use __ to make variable private
__new__speed
"""
class Speed:
    def __init__(self):
        self.speed=10
        self.__new__speed =80
    def display(self):
        print(self.__new__speed)

    def get_new_speed(self):
        return self.__new__speed
    def set_new_speed(self,new_speed):
         self.__new__speed=new_speed
s= Speed()
#print(s)
s.speed=30
s.display()
print(s.get_new_speed()) # accessing using getter
s.set_new_speed(120) #modifing private variable with public setter
print(s.get_new_speed())


"""
#Public and Private Methods
in python _ is pratially private
whereas __ is private
"""
class PrivateMethodEx:
    def __init__(self):
        print("I am a private constructor")
    def __user_def_pvt_meth(self):
        print("I am a user def pvt method")
    def user_def_pub_meth(self):
        print("I am public, but will invoke a private method here:")
        self.__user_def_pvt_meth()

prv=PrivateMethodEx()
prv.user_def_pub_meth()