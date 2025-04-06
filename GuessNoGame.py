n = 18
guess = 1
while True:
    a = int(input("Enter a number"))
    if guess < 9 :
        if n > a:
            print("you entered smaller number")
            guess = guess + 1
            print("no. of guesses left are ", 10 - guess)
            continue
        elif n < a:
            print("you entered greater number")
            guess = guess + 1
            print("no. of guesses left are ", 10 - guess)
            continue

        else:
            print("you guessed correctly in ", guess, "guesses")
            break
    else :
        print("game over")
        break


