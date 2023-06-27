def getValidNumber():
    while True:
        userNumber = input("Enter a number between 50 and 100: ")
        try:
            intNumber = int(userNumber)
            if 50 < intNumber < 100:
                return intNumber
            else:
                print("Please enter a number between 50 and 100.")
        except ValueError:
            print("Please enter a numeric input.")

userNumber = getValidNumber()
print("You entered", userNumber)
