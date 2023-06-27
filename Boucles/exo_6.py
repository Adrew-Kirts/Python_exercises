def array_creation():
    user_array = []

    n = int(input("Enter number of elements in array : "))

    for _ in range(n):
        element = int(input("Enter element: "))
        user_array.append(element)
    return user_array


def sumArray(user_array):
    sum = 0
    for i in range(len(user_array)):
        sum = sum + user_array[i]
    return sum


user_array = array_creation()
array_sum = sumArray(user_array)

print("The sum of all values in array is: ", array_sum)