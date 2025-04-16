class Employee:
    name="manan" 
    age=22
    salary=100000

    def __init__(self,name,salary,age): #dunder method
        self.name=name
        self.salary=salary
        self.age=age
    
varun=Employee("nan",100000,22)
print(varun.name)           
print(varun.salary)
print(varun.age)