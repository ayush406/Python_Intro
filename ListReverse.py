print("enter the numbers of list one by one.")
size = int(input("enter the size of list."))
L1 = []

for i in range(size):
    L1.append(int(input("Enter list element")))

print(f"your list is {L1}")

rev = L1[:] # this will create a copy of list.
for j in range(len(rev)//2):
    rev[j], rev[len(rev) - j -1] = rev[len(rev) - j - 1], rev[j]

print(rev)