import sys
import file2

print(sys.path) #returns the path where the interpreter searches for module.

print(file2.a)
b = file2.pj()
print(b)

"""
we can also say like :- 

from file2 import a
print(a)
but import method is best as it prohibits the risk of ambiguity error..
"""