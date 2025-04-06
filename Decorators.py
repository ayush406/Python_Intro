"""
def fun1():
    print("this is just a test")

fun2 = fun1
del fun1
fun2()
"""

def fun1(fun2):
    def exec():
        print("Executing now")
        fun2()
        print("Executed")
    return exec

@fun1
def ayush():
    print("Ayush is a good boy")


"""
ayush = fun1(ayush)
we have one more way to write the above code and that is called decorators.
"""
ayush()