# ============================= LINEAR SEARCH PRACTISE =============================

import time


# function to run linear search
def linearSearch(arr, targetValue):
    # loop for search through array and finding intented value
    for x in range(len(arr)):
        # x = index to go through until index matches the targeted value
        if arr[x] == targetValue:
            return x
        #if the given value isnt found in the list, -1 is the output
    return -1

# my dataset to find appropriate value
arr = [3, 7, 2, 765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,432, 789, 123,
890, 567, 876, 345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
876, 345, 654, 321, 123, 890, 567, 876, 345, 654, 9, 5, 69, 88]

# chosen value
targetValue= 69

# start recording the time taken to process everything
start_time = time.time()

#--------------------------------------------------------------------------------------

result = linearSearch(arr, targetValue)

#--------------------------------------------------------------------------------------
# ending recording the time taken to process everything
end_time = time.time()

# calculating the time time taken using simple math
execution_time = end_time - start_time

if result != -1:
    print(f"\nValue {targetValue} found at index {result}. Executed in {execution_time:.10f} seconds\n")
else:
    print(f"\nValue {targetValue} not found in the list\n")

