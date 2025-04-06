import sklearn

def printayush():
    return "this is it"

def add(a, b):
    return a + b


# name is equal to main when the original file is executed. if it is imported then it's not true.
print(__name__)
if __name__ == '__main__':
    print("ayush is a good boy")
    print(add(5, 78))

