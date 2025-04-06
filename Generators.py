"""
iterable - __iter__() or __getitem__(). Lists, tuples, dictionaries and sets.
iterator - __next__()
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
iteration -
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(4)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())