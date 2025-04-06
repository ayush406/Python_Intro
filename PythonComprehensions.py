# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# print(ls)

# list comprehension
ls = [i for i in range(100) if i%3 == 0]
print(ls)

# dictionary comprehension

dict1 = {j:f"item{j}" for j in range(100) if j%4 == 0 }
dict1 = {value:key for key,value in dict1.items()} # use this to reverse the key value pairs.
print(dict1)

dress = {dress for dress in ["dress1", "dress2"]}
print(dress)