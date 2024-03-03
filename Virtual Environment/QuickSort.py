#======================= QUICK SORT PRACTISE ============================================

import time

# function  = find partition and which will determine where pivot be and where element will be directed to
def partition(array, low, high):
    pivot = array[high]
    x = low - 1

    # goes through dataset, compares given/current element with pivot and switches it if needed
    for y in range(low, high):
        if array[y] <= pivot:
            x = x + 1
            array[x], array[y] = array[y], array[x]

    # code ensures that pivot is always in the right position
    array[x + 1], array[high] = array[high], array[x + 1]
    return x + 1


# Performing quicksort on an array/dataset
def quicksort(array, low, high):
    # going through array to see if more than 1 element exists
    # Then find where partition would be and split the array/dataset into two halves
    #  if condition isnt met, function calls itself "recursively" then and creating smaller partitions to continue on with function
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


class LinkedList:
    def __init__(self):
        self.head = None

    # calling function later to print out the dataset given
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    # self call function to perform quicksort on list
    def quick_sort(self, head, tail):
        if head is None or head == tail:
            return head

        pivot = head.data
        less_than_pivot = None
        equal_to_pivot = head
        current = head.next

        # looping through partition cells/elements based around pivot      
        while current != tail.next:
            next_node = current.next

            if current.data < pivot:
                current.next = less_than_pivot
                less_than_pivot = current
            else:
                equal_to_pivot.next = current
                equal_to_pivot = current

            current = next_node

        # calling upon the partitions/ two halves of the one dataset and then merging it
        if less_than_pivot is not None:
            less_than_pivot = self.quick_sort(less_than_pivot, equal_to_pivot)

        equal_to_pivot.next = self.quick_sort(equal_to_pivot.next, tail)

        if less_than_pivot is None:
            return equal_to_pivot

        return less_than_pivot

# Use the same array for both list and linked list
dataset = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
           890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
           432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
           765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
           908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

print(f"\n\nThe unsorted list for Quick Sort is:\n{dataset}\n")

# Function call to sort the array
quicksort(dataset, 0, len(dataset) - 1)

# Print the sorted array
print('Sorted dataset is now:')
for x in dataset:
    print(x, end=" ")

# assigning call variables
linked_list = LinkedList()
linked_list.print_list()

# Calculate the time taken for to sort through data
start_time = time.time()
#------------------------------------------------------------------------------------------------------

linked_list.head = linked_list.quick_sort(linked_list.head, None)

#------------------------------------------------------------------------------------------------------
end_time = time.time()

# Print the sorted linked list
print("\nLinked List after sorting")
linked_list.print_list()

# Display the time taken in seconds to 6 decimal places
process_quick_sort = end_time - start_time
print(f"\n\nTime taken to process Quick Sort: {process_quick_sort:.6f} seconds\n\n\n")
