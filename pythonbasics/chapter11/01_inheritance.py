class Employee:
    company="Turing" 
    def show(self):
        print(f"the name is {self.name}")
        print(f"the age is {self.age}") 
        print(f"the salary is {self.salary}") 
        
# class programmer:
#     company="dell"
#     def show(self):
#         print(f"the name is {self.name}")
#         print(f"the age is {self.age}") 
#         print(f"the salary is {self.salary}")
    
#     def showlanguage(self):
#         print(f"the language is {self.language}")


class programmer(Employee):
    company="Turing" 
    def show(self):
        print(f"the name is {self.name}")
        print(f"the age is {self.age}") 
        print(f"the salary is {self.salary}") 


a=Employee()
b=programmer()
print(a.company)
print(b.company)