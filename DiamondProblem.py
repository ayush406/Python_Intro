class A:
    def met(self):
        print("this is method from class A.")
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.met()