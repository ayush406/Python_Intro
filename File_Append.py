f = open("Germany.txt", "w")
# this will create a new file and if an existing file is used, it will overwrite the contents of that file.
a = f.write("Ayush is going to Germany.")
# to append, use mode 'a'.
print(a) # this will print the number of characters entered.
f.close()


# to read and write both in a single mode.

f1 = open("USA.txt", "r+")
f1.write("it is not feasible to study in USA.")

f1.close()