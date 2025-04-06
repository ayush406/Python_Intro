f = open("Ayush.txt")
content = f.read()  # f.read(3) will capture first 3 letters and if subsequent read functions are written, then it will capture after them.


print(content)

"""
we can do this also :- 
for line in f:
    print(line, end = "") . this will print all the lines in that file.
    
and 

print(f.readline()). this will print only one line.
"""
f.close()