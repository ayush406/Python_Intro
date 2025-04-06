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
B = Employee("Rishabh", "Chaudhary")
print(A.explain())

A.fname = "ABC"
print(A.fname)
print(A.email) # now, we have written property decorator in the method so we don't need to call this like a method. we call it like an attribute.

# if we change the name, then it will be changed but mail id was initialised at the time of object creation so it doesn't change. to solve this problem, we use setters.

A.email = "xyz.pqr@gmail"
print(A.fname)
print(A.lname)
print(A.email)

del A.email

print(A.fname)
print(A.lname)
print(A.email)