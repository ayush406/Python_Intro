class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.mail = f"{fname}.{lname}@Google.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    # this is function created to solve the problem.
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set."
        return f"{self.fname}.{self.lname}@google.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


A = Employee("Ayush","Chaudhary")
print(type(A))
print(id(A))
print(dir(A)) # returns the list of methods and valid attributes in that object.
import inspect
print(inspect.getmembers(A))
