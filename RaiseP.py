# a = input("Enter your name")
# b = input("how much do you earn")
#
# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 hence stopping the program.")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hi! {a}")

c = input("Enter your name")

try:
    print(a)

except Exception as e:
    if c == "harry":
        raise ValueError("harry is blocked")

    print("exception handled")

