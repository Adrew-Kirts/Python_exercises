def array_creation():
    user_array = []

    n = int(input("Enter number of elements in array : "))

    for _ in range(n):
        element = int(input("Enter element: "))
        user_array.append(element)
    return user_array


def smallest_number(user_array):
    min1 = user_array[0]
    for i in range(len(user_array)):

        if user_array[i] < min1:
            min1 = user_array[i]

    print("The smallest value in the list is ", min1)


smallest_number(array_creation())