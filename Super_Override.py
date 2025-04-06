# VERY IMPORTANT VIDEO.
class A:
    var1 = "I'm a class variable in class A"
    var3 = "I'm a class variable."
    def __init__(self):
        self.var3 = "I'm inside class A's constructor."
        self.special = "I'm special."


class B(A):
    var2 = "I'm in class B."
    var3 = "I'm in class B."

    def __init__(self):
        super().__init__() # USE THIS TO RUN CLASS A'S CONCTRUCTOR. we can't use instance variables in class A's constructor without this.
        self.var3 = "I'm inside class B's constructor."
a = A()
b = B()

# first it will look for instance variable in that class and then in derived class and then class variable.
# for below code, it will search for var3 instance variable inside B class and then inside A class.
print(b.var3, b.special)


