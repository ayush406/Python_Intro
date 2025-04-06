a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = input("Enter the operation")

if c == "*":
    if a == 45 and b ==3:
        print("answer is 555")
    else:
        print("answer is ",a*b)
elif c == "+":
    if a == 56 and b == 9:
        print("answer is 77")
    else:
        print("answer is ",a+b)
elif c == "/":
    if a == 56 and b == 6:
        print("answer is 4")
    else:
        print("answer is ",a/b)
elif c == "-":
   print("answer is ",a-b)
else:
    print("Wrong input")