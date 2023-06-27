def array_creation():
    user_array = []

    n = int(input("Enter number of elements in array : "))

    for _ in range(n):
        element = int(input("Enter element: "))
        user_array.append(element)
    return user_array


def closest_to_zero(user_array):
    min1 = user_array[0]
    for i in range(len(user_array)):

        if min1 > abs(user_array[i]):
            min1 = user_array[i]

    print("The value closest to zero in the list is ", min1)


closest_to_zero(array_creation())