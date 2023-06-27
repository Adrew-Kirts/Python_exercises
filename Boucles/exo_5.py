def arrayCreation():
    array = []

    n = int(input("Enter number of elements in array : "))

    for _ in range(n):
        element = int(input("Enter element: "))
        array.append(element)
    return array

print(arrayCreation())