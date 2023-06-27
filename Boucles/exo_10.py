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


def reverse_order(a):
    while a > 9:
        print(int(modulo(a)))
        a = a / 10
    print(int(a))


def modulo(one):
    while one >= 10:
        one -= 10
    return one


user_nr = get_valid_number()

reverse_order(user_nr)





