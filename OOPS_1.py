class Employee:
    leaves = 12
    pass

ayush = Employee()
sanjay = Employee()

# salary, name, role are the properties of objects.
ayush.name = "Ayush"
ayush.salary = 600000
ayush.role = "Data Scientist"

sanjay.name = "Sanjay"
sanjay.salary = 650000
sanjay.role = "IAS"


sanjay.leaves = 45 # this will change the value of leaves only for Sanjay but if you want to change the value of leaves per se, then refer below code
print(sanjay.leaves)
print(ayush.leaves)

Employee.leaves = 60

print(sanjay.leaves)
print(ayush.leaves)

print(sanjay.__dict__) # this returns the properties of instance variable in the form of a dictionary.
print(ayush.__dict__)
print(Employee.__dict__)