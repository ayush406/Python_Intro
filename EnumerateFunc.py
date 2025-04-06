L1 = ["Banana", "Mango", "Strawberry", "Cherry", "Watermelon", "Apple", "Kiwi"]

# i = 1
#
# for item in L1:
#     if i%2 != 0:
#         print(item)
#

for index, item in enumerate(L1):
    if index%2 == 0:
        print(item)
