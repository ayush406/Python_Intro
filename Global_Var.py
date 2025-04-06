a = 10 # here a is a global variable.
c = 15
def function(n):
    a = 5 # here a is a local variable. it has a global scope so it is a read only variable here. we can't change it.
    # to change a global variable inside local scope, we use 'global' keyword.
    b = 8 # here b is a local variable and it doesn't have any global scope. therefore, it can't be accessed outside this function.
    global c
    c = c+45
    print(c)
    print(a)
    print(n, "I have printed")

function("Hi Ayush!")
print(a)
print(c)
# print(b). this will give an error.