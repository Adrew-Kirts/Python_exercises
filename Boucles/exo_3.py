def modulo(one, two):
    while one >= two:
        one -= two
        #print("one:",one)
    return one

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

nrOne = getValidNumber()
nrTwo = getValidNumber()

print("The remainder of the division is:", modulo(nrOne, nrTwo))
