class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward
    def annual_salary(self):
        return self.pay*12+self.reward

class Employee:
    def __init__(self,name,position,pay,reward):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay,reward) #composition has relation/partf of, here salary is part of employee
    def final_sal(self):
        return self.final_salary.annual_salary()


e1 = Employee("sac","dev",12,2)
print(e1.final_sal())
