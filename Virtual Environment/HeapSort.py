# ============================= HEAP SORT PRACTISE =============================


def heapify(dataset, x, i):
    # Find the largest amoung base/root and its dependant
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left child exists and is greater than the root
    if l < x and dataset[i] < dataset[l]:
        largest = l

    # Check if right child exists and is greater than the current largest element
    if r < x and dataset[largest] < dataset[r]:
        largest = r

    # If the root is not the largest, swap with the largest and continue heapifying
    if largest != i:
        dataset[i], dataset[largest] = dataset[largest], dataset[i]
        heapify(dataset, x, largest)


# Function to perform Heap Sort on the given dataset
def heapSort(dataset):
    x = len(dataset)

    # Build max heap (rearrange array)
    # Start from the last non-leaf node and heapify all nodes in reverse order
    for i in range(x // 2, -1, -1):
        heapify(dataset, x, i)

    # One by one extract elements
    for i in range(x - 1, 0, -1):
        # Swap the current root with the last element
        dataset[i], dataset[0] = dataset[0], dataset[i]

        # Heapify the reduced heap (exclude the sorted elements)
        heapify(dataset, i, 0)


# Dataset to be sorted
dataset = [432, 765, 123, 908, 234, 567, 876, 345, 654, 321,
           789, 876, 345, 654, 321, 908, 567, 876, 345, 654,
           432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
           765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
           908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
           321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
           654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
           345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
           876, 345, 654, 321, 908, 765, 432, 789, 123, 890,
           567, 876, 345, 654, 321, 908, 765, 432, 789, 123,
           890, 567, 876, 345, 654, 321, 908, 765, 432, 789,
           123, 890, 567, 876, 345, 654, 321, 908, 765, 432,
           789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
           432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
           765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
           908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
           321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
           654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
           345, 654, 321, 908, 765, 432, 789, 123, 890, 567]

# Call the heapSort function to sort the dataset
heapSort(dataset)

# DISPLAY
#========================================================================================
# Get the length of the sorted dataset
x = len(dataset)

# Print a message indicating that the following values are the sorted dataset
print("Sorted dataset is")

# Iterate through each element in the dataset and print it with a space after each element
for i in range(x):
    # Prints the current element with a space, using the placeholder '%d' for integers
    # The 'end='' argument ensures that the next printed element will be on the same line
    print("%d " % dataset[i], end='')
