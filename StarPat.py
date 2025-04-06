a = int(input("enter the number"))

b = bool(int(input("Enter 0 for false and 1 for true")))

# boolean treats a string as true but if you don't provide any input it will be false.
# in case of integer, it treats 1 as true and 0 as false.

if b:
    for i in range(0, a):
        for j in range(0, i + 1):
            print("*", end="")
        print("")

else:
    for i in range(a, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print("")

