class Student :
    pass

# Student is an emmpty class
stu1= Student()
stu2= Student()
stu1.name="Sachin"
stu2.name="keerthi"
print(stu1.name)
print(stu2.name)


#Constructors and how to use it
class Motorbike:
    def __init__(self,maxSpeed):
        self.maxSpeed=maxSpeed # assigning the max speed to the instance object.
        print(f"Motor bike instance created has a max speed {self.maxSpeed}")


honda= Motorbike(250)
ktm= Motorbike(199)


#Constructors puzzels
class Planet:
    # In python we can only have one constructor.

    def __init__(self,name="Earth"):
        self.name=name
        self.id=1



pla=Planet()
print(pla.name)



#Encapsulation, since we can change the state of the objects from outside as done above,instead we need to do it using methods.
class MotorCar:
    def __init__(self,speed):
        self.speed=speed
    def increase_speed(self,speed):
        self.speed+=speed

honda = MotorCar(150)
honda.increase_speed(20)  # calling the method to increase the speed of the vehicle
print(honda.speed)


