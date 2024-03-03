# ============================= MERGE SORT PRACTISE =============================


import time

# Function to perform Merge Sort
def merge_sort(arr, low, high):
    # Check if there is more than one element in the array
    if low < high:
        
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Recursively sort the left and right halves of the array
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        
        # Merge the sorted halves
        merge(arr, low, mid, high)

# Function to merge two sorted subarrays
def merge(arr, low, mid, high):
    # Create temporary arrays L and R
    L = arr[low:mid + 1]  # Left subarray from low to mid
    R = arr[mid + 1:high + 1]  # Right subarray from mid+1 to high

    # Initialize indices for merging
    x = y = 0
    k = low  # Initial index of merged subarray

    # Merge the temporary arrays back into arr
    while x < len(L) and y < len(R):
        if L[x] <= R[y]:
            arr[k] = L[x]  # Copy element from L
            x += 1
        else:
            arr[k] = R[y]  # Copy element from R
            y += 1
        k += 1

    # Copy any remaining elements of L and R
    while x < len(L):
        arr[k] = L[x]
        x += 1
        k += 1
    while y < len(R):
        arr[k] = R[y]
        y += 1
        k += 1

# Function to print the elements of the list
def printList(arr):
    for element in arr:
        print(element, end=" ")  # Print each element followed by a space
    print()  # Move to the next line after printing all elements

if __name__ == '__main__':
    # Example array to be sorted
    arr = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
           890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
           432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
           765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
           908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

    print(f"\n\nThe unsorted list for Merge Sort is:\n{arr}\n")

    # Calculating time taken for Merge Sort
    start_time = time.time()
    merge_sort(arr, 0, len(arr) - 1)
    end_time = time.time()

    # Calculate the time taken for the sorting process
    process_merge_sort = end_time - start_time

    # Print the sorted list and the time taken
    print("\nThe sorted list for Merge Sort is:\n", arr)
    print(f"\n\nTime taken to process Merge Sort: {process_merge_sort:.6f} seconds\n\n\n")
