class Employee:
    leaves = 12

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    #class method can only access the instance variable of that class only.
    def changeleaves(cls, new):
        cls.leaves = new




ayush = Employee("Ayush", 60000, "Instructor")
sanjay = Employee("Sanjay", 60000, "IAS")


ayush.changeleaves(67)
print(ayush.printdetails())
print(sanjay.printdetails())

#class method runs on the class so it will change the class properties.
sanjay.leaves = 45 # if an instance of class is declared then it can't be changed.
print(ayush.leaves)
print(Employee.leaves)
print(sanjay.leaves)