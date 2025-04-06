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

    @classmethod
    def from_str(cls, String):
        return cls(*String.split("-"))



class Player:
    no_of_games = 4
    leaves = 13
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.Game}."


# below is code for multiple inheritance. Order of writing the class name is relevant as it will look for constructor from the first class.
class CoolProgramme(Employee, Player):
    leaves = 14
    language ="C++"
    def printlang(self):
        print(self.language)


# ayush and sanjay are two instances o Employee class.
ayush = Employee("Ayush", 60000, "Instructor")
sanjay = Employee("Sanjay", 60000, "IAS")

shubham = Player("Shubham", ["cricket", "tennis"])


karan = CoolProgramme("Karan", 670000, "Cool")
karan.printlang()
deet = karan.printdetails()
# Employee and player both have printdetails method but it will run the method of Employee class as it is written first.
# in multiple inheritance, basically the class written first in order of precedence is a parent class but the child class will also implement the properties of other class as well.
print(deet)
print(karan.leaves)
# as leaves is present in all the classes, it will print the leaves of child class. but if child class doesnot have leaves, then it will first look in first class then second class.