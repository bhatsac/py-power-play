class Fan:
    def __init__(self,make,radius,color):
        self.make=make
        self.radius=radius
        self.color=color
        self.is_on=False
        self.speed=0
    def __repr__(self):
        return repr((self.make,self.radius,self.color,self.is_on,self.speed))
    def switch_on(self):
        self.is_on=True
        self.speed=1
    def switch_off(self):
        self.is_on=False
        self.speed=0

fan1=Fan("Crompton","60cms","brown")
print(fan1)
fan1.switch_on()
print(fan1)

#Object composition. Object contains intance of another book

class Book:
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author
        self.reviews=[]

    def __repr__(self):
        return repr((self.id,self.name,self.author,self.reviews))
    def add_review(self,review):
        self.reviews.append(review)

class Review:
    def __init__(self,id,description,rating):
        self.id=id
        self.description=description
        self.rating=rating
    def __repr__(self):
        return repr((self.id,self.description,self.rating))

book1=Book(1,"Awesome Book","sac")
review1_1= Review(1,"Awesome Book Review",5)
review1_2=Review(2,"Awesome Book Review",4)
book1.add_review(review1_1)
book1.add_review(review1_2)
print(book1)



#Inheritance
class Animal:
    def bark(self):
        print("bark")

class Pet(Animal):
    def groom(self):
        print("groom")
pet1=Pet();

pet1.bark()
pet1.groom()

# Multiple Inheritance example
#Amphibian
class LandAnimal:
    def __init__(self):
        super().__init__()
        self.walking_speed=5
class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed=10
class Amphibian(LandAnimal,WaterAnimal):
    def __init__(self):
        super().__init__()


amphi= Amphibian()
print(amphi.swimming_speed)
print(amphi.walking_speed)


# Abstract base class
from abc import ABC,abstractmethod
class AbstractAnimal:
        @abstractmethod
        def sound(self): pass
class Dog(AbstractAnimal):
        def sound(self):
            print("Bow Bow!")
class Cat(AbstractAnimal):
        def sound(self):
            print("Meow Meow!")
dog =Dog()
dog.sound()
cat = Cat()
cat.sound()
#Template Method Pattern with Recipe Class
from abc import ABC,abstractmethod
class AbstractReceipe(ABC):
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

        @abstractmethod
        def prepare(self):pass

        @abstractmethod
        def recipe(self):pass

        @abstractmethod
        def cleanup(self):pass
class Dalitoy(AbstractReceipe):
    def prepare(self):
        print("soaking dal and steaming in pressure cooker")
    def recipe(self):
        print("add: oil 2 tbsp,tumeric 1 tbsp,green chills 3-5 , salt to taste, coriander for garnishing")
    def cleanup(self):
        print("clean up the vessels")

toy=Dalitoy()
toy.execute(); #This will execute all the overridden methods .


