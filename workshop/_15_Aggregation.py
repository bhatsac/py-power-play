# This will define has-a relationship ( here both entities can exists independently)
# Aggregation si weak association while composition is strong association
class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return self.pay * 12 + self.reward


class Employee:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal

    def final_sal(self):
        return self.final_salary.annual_salary()


sal = Salary(12, 2)
e1 = Employee("sac", "dev", sal)
print(e1.final_sal())
