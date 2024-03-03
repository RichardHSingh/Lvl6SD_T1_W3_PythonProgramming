# ============================= INSERT SORT PRACTISE =============================



def insertion_sort(name):
    # Traverse through the entire array starting from the second element
    for i in range(1, len(name)):
        # Store the current element to be compared
        current_element = name[i]
        
        # Move elements of arr[0..i-1] that are greater than current_element
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and current_element < name[j]:
            name[j + 1] = name[j]
            j -= 1
        
        # Place the current element at its correct position in sorted order
        name[j + 1] = current_element

# use of given data
name = [12, 11, 13, 5, 6]
print("\nUnsorted array:", name)

insertion_sort(name)

print(f"Sorted array: {name}")




