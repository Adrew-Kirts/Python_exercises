userInput = False

while userInput == False:
    age = input("Enter your age: ")
    try:
        intAge = int(age)
        if intAge > 0:
            userInput = True
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a numeric input.")

if intAge < 2:
    resultAge = "baby"
elif intAge < 12:
    resultAge = "child"
elif intAge < 17:
    resultAge = "adolescent"
elif intAge < 69:
    resultAge = "adult"
else:
    resultAge = "old person"

print("You are a(n)", resultAge)
