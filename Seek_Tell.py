# tell function indicates where the file pointer is.
# seek function resets the pointer to a specific location.
f = open("Ayush.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())

f.close()
