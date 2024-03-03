# ============================= INSERT SORT ALGORITHM =============================


import time

def Insert_Sort(setData):
    # Traverse through the entire array starting from the second element
    for x in range(1, len(setData)):

        # Store the current element to be compared
        current_element = setData[x]
        
        # Move elements of array[0..i-1] that are greater than current_element
        # to one position ahead of their current position
        y = x - 1
        while y >= 0 and current_element < setData[y]:
            setData[y + 1] = setData[y]
            y -= 1
        
        # Place the current element at its correct position in sorted order
        setData[y + 1] = current_element


# Example usage
setData = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

print(f"Unsorted array:\n {setData}")

Insert_Sort(setData)

#calculating time taken 
start_time = time.time()

#------------------------------------------------------------------

Insert_Sort(setData)

#------------------------------------------------------------------
end_time = time.time()

# equation for getting correct timing for how long process took
process_time_taken = end_time - start_time

print(f"\nSorted array:\n {setData}")

# will display time in seconds to to 6dp
print(f"\n\nTime taken to process: {process_time_taken:.6f} seconds")


