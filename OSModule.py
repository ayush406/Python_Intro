import os

print(dir(os))
print(os.getcwd()) # prints the current working directory.
# os.chdir("C://") # it will change the current working directory.
print(os.getcwd()) # now if we open any file which is not in this directory, then it will produce error.
# the below code will give error as it is not present in C: drive.
# f = open("Ayush.txt")

print(os.listdir()) # prints the file in the given directory.
print(os.listdir("C://")) # we can give a customese path also.

# os.mkdir("this") # it will create a folder in current directory with name 'this'.
# os.makedirs("this/that") # it will create a directory and a sub directory.

# os.rename("Ayush.txt", "Ayush1.txt")

print(os.environ.get('Path'))

print(os.path.join("C://","Ayush1.txt")) # to join two paths.

print(os.path.isfile("C://")) # returns true or false on the basis of existence of file.
