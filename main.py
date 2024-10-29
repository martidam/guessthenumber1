import random

random_num = random.randint(1, 10)

while True:

    guess = int(input("Guess a number between 1 and 10: "))

    if guess > random_num:

            print("Too high! Try again.")
    elif guess < random_num:

        print("Too low! Try again.")
    else:

        print("Congratulations! You've guessed the number.")

        break
