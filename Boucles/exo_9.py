def getValidNumber():
    while True:
        userNumber = input("Enter a positive number: ")
        try:
            intNumber = int(userNumber)
            if intNumber > 0:
                return intNumber
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a numeric input.")


def total_nr(nr_input):
    n = 0
    for i in range(nr_input+1):
        n = n + i

    print("Total of all int in number is: ", n)


number = getValidNumber()
total_nr(number)