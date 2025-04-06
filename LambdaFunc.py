import random

add = lambda x,y : x + y

print(add(4,8))

r = random.randint(0,5) # selects a random number between 0 and 5 including both.
print(r)

random.random() # this chooses a number between o and 1.

L1 = ["NARCOS", "Break Bad", "Heist", "Prison Break"]
c = random.choice(L1)
print(c) # picks a random choice from a list.