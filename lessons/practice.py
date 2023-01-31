"""practice"""

secret: int = 3
guess: int = 1

if guess == secret:
    print("success")
    print(str(guess) + " is the secret number!")
else:
    guess = guess + 1
    if guess == secret:
        print("success on second try")
    else: 
        print("wrong guess")
        if (guess == secret - 1):
            print("the guess of " + str(guess) + " is off by one number")