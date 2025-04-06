class Employee:
    leaves = 12

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"



ayush = Employee("Ayush", "60000", "Instructor")
sanjay = Employee("Sanjay", "60000", "IAS")

# salary, name, role are the properties of objects.
# ayush.name = "Ayush"
# ayush.salary = 600000
# ayush.role = "Data Scientist"
#
# sanjay.name = "Sanjay"
# sanjay.salary = 650000
# sanjay.role = "IAS"

print(ayush.printdetails())
print(sanjay.printdetails())