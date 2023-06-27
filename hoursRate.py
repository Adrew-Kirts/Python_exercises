hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    floatHours = float(hours)
    floatRate = float(rate)
except:
    print("error, please enter a numeric input")
    quit()

print("The total is:")
print(floatHours * floatRate)
