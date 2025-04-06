class Employee:
    leaves = 12
    _mouse = 10
    __laptop = 13

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

    @classmethod
    def from_str(cls, String):
        return cls(*String.split("-"))

# by default, it is public. for protected, use "_" in starting and for private use "__"

ayush = Employee("Ayush", 60000, "Instructor")

# a protected variable can be accessed using an instance of that class and by deriving the class.
print(ayush._mouse)
#use below code to access private variable.
print(ayush._Employee__laptop)