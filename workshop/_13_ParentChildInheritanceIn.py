class Parent:
    def __init__(self):
        print("Parent class init method")
class Parent2:
    def __init__(self):
        print("Parent2 class init method")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child class init method")


class Child2(Parent,Parent2):
    def __init__(self):
        super().__init__(self) #This super calls Parent and not Parent2 since it depends on how the sequence is refered Child2(Parent,Parent2)
        print("Child class init method")


c1= Child()
print(Child.__mro__)
print(Child2.__mro__)
