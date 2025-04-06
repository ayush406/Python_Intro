# Classes - template
# Object - Content inside the class/ Instance of the class.

# pass is used when there is no content inside.
class Student:
    leaves = 9
    pass


ayush = Student()
rishabh = Student()

print(ayush, rishabh) # prints the memory location of the objects.

# Creating the instance variables of the objects.

ayush.name = "Ayush"
ayush.std = 12
ayush.section = "A"

print(ayush.name)