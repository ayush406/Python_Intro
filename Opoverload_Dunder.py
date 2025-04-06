class Employee:
    leaves = 12

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    # class method can only access the instance variable of that class only.
    def changeleaves(cls, new):
        cls.leaves = new

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee {self.name}, {self.salary}, {self.role}"

    def __str__(self):
        return f"Employee details are {self.name}, {self.salary}, {self.role}"

# methods starting and ending with __ are dunder methods.

ayush = Employee("Ayush", 60000, "Instructor")
sanjay = Employee("Sanjay", 60000, "IAS")

print(ayush + sanjay)
print(ayush / sanjay)
print(ayush) # this will prefer str method over repr. to call repr, refer below :-
print(repr(ayush))