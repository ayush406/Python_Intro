# map function applies a specific operation on whole list.

numbers = ["12", "23", "34", "78"]

print(type(numbers[0]))
"""
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

"""

numbers = list(map(int, numbers))

print(type(numbers[0]))


num = [2, 3, 56, 78, 34]
square = list(map(lambda x : x*x, num))
print(square)

