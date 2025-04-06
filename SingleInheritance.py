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

    @classmethod
    def from_str(cls, String):

        return cls(*String.split("-"))

#below is code for single level inheritance. Programmer has inherited Employee class. Programmer is child and Employee is parent class.

class Programmer(Employee):

    #even if the child class doesn't have a constructor and the base class have, then also we need to pass the values while delaring the object.
    def __init__(self, aname, asalary, arole, languages):
        # we can directly use super for name, salary and role.
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"the programmer's name is {self.name}. salary is {self.salary}. role is {self.salary}. Knowledge of programming is {self.languages}"


ayush = Employee("Ayush", 60000, "Instructor")
sanjay = Employee("Sanjay", 60000, "IAS")
rajat = Employee.from_str("Rajat-120000-BA") # instead of first creating an object and then passing value we directly value.

shubham = Programmer("Shubham", 70000, "IES", ["Python", "Java"])
karan = Programmer("Karan", 75000, "IFS", ["SQL", "Tableau"])


# print(ayush.printdetails())
# print(sanjay.printdetails())

print(karan.printprog())

print(rajat.printdetails())