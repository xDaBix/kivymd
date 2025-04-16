class Employee:
    name="manan" 
    age=22
    salary=100000

    def getinfo(self):
        print(f"salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("hello")

varun=Employee()
varun.getinfo()  
varun.greet() 