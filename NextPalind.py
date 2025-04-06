
def next_palind(n):
    while not ispalind(n):
        n+=1
    return n


def ispalind(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the number of test cases"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number :"))
        numbers.append(number)

    for i in range(n):
         print(f"Next palindrome for {numbers[i]} is {next_palind(numbers[i])}")