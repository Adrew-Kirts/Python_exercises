import random


def get_valid_number():
    while True:
        user_number = input("Enter a positive number: ")
        try:
            int_number = int(user_number)
            if int_number > 0:
                return int_number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a numeric input.")


def guessing_game(i):
    j = 1
    while i != secret_number:

        if i > secret_number:
            j = j + 1
            print("Too big")
            i = get_valid_number()
        elif i < secret_number:
            j = j + 1
            print("Too small")
            i = get_valid_number()
        if j == 20:
            print("Too bad you lost, the secret number was", secret_number)
            return

    print("Winner!")


secret_number = (random.randint(1, 100))
guessing_game(get_valid_number())
