a = input("Enter number 1")
b = input("Enter number 2")

try:
    print("the sum is ", int(a) + int(b))

except Exception as e:
    print(e)
    
print("this will be executed anyhow")