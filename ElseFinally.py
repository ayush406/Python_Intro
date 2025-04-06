f1 = open("Ayush.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)

else:
    print("this ill be executed only when except isn't executed.")

# only 1 of except and else will be executed.

# finally will be executed no matter what.
finally:
    print("this will execute anyway.")
    # f.close()
    f1.close()