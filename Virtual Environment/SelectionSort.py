#======================= SELECTION SORT PRACTISE ============================================

import time

# Selection sort algorithm
def Selection_Sort(setData):
    n = len(setData)

    for x in range(n - 1):
        # Assume the current index is the minimum
        min_index = x

        for y in range(x + 1, n):
            # Find the index of the minimum element in the unsorted part
            if setData[y] < setData[min_index]:
                min_index = y

        # Swap the found minimum element with the first element of the unsorted part
        setData[x], setData[min_index] = setData[min_index], setData[x]

# EGIVEN DATASET
setData = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
           890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
           432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
           765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
           908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

print(f"\n\nThe unsorted list for Selection Sort is:\n{setData}\n")

# Calculating time taken to process dataset
start_time = time.time()
#------------------------------------------------------------------------------------------------------

Selection_Sort(setData)

#------------------------------------------------------------------------------------------------------
end_time = time.time()

process_selection_sort = end_time - start_time

print("\nThe sorted list for Selection Sort is:\n", setData)

# Will display time in seconds to 6 decimal places
print(f"\n\nTime taken to process Selection Sort: {process_selection_sort:.6f} seconds\n\n\n")

