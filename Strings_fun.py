str1 = "Ayush is a good boy"
print(str1[4]) #4th index
print(str1[0:4]) # till 4th index(4th is not included)
print(str1[0:]) # complete
print(len(str1))

print(str1[0:19:2]) #skips every other character

print(str1[-1:])

print(str1[::-1]) # used to reverse a string

print(str1.isalnum()) #checks whether string is alphanumeric.
print(str1.endswith("boy"))
print(str1.count("a"))
print(str1.find("is"))
print(str1.upper())
print(str1.lower())
print(str1.replace("is","are"))