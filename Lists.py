L1 = ["Canada", "Germany", "Australia", "USA"]
print(L1) # prints whole list
print(L1[0])

num = [34, 56, 12, 45, 67, 89, 32]
num.sort()
print(num)
num.reverse()
print(num)

print(num[0:3])

print(len(num))
print(min(num))
print(max(num))
num.append(5)
num.insert(1,70) # inserts 70 at 1st index.
print(num)

#lists are mutable while tuples are immutable.

tp = (1, 2, 3)
#to define a single element tuple, refer below :-
tp1 = (1,)
# tp[1] = 34. this will give error as tuples are immutable.
print(tp[1])