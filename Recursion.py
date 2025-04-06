def fact(n):
    """
    this function is used to find the factorial.

    """
    if n >=1:
        return n * fact(n-1)
    elif n == 0:
        return 1

a = int((input("Enter the number")))
print(fact(a))
print(fact.__doc__)