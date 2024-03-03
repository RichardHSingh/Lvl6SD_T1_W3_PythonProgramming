# ============================= BINARY SEARCH PRACTISE =============================

import time

def binarySearch(arr, targetValue):
    # initialise  left and right side for bianary search
    left = 0
    right = len(arr) - 1

    # splits the dataset down the middle --> left is low values --> right is high values
    while left <= right:
        mid = (left + right) // 2

        # checks the median element is the target value and returns it
        if arr[mid] == targetValue:
            return mid
        
        # if target value is larger than median --> look on right side or else look on left side
        if arr[mid] < targetValue:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# my dataset list
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# my targeted value in list
targetValue = 15

# start recording the time taken to process everything
start_time = time.time()

#--------------------------------------------------------------------------------------

result = binarySearch(arr, targetValue)

#--------------------------------------------------------------------------------------
# ending recording the time taken to process everything
end_time = time.time()

# calculating the time time taken using simple math
execution_time = end_time - start_time

if result != -1:
    print(f"\nValue {targetValue} found at index {result}. Executed in {execution_time:.10f} seconds\n")
else:
    print(f"\nValue {targetValue} not found in the list\n")
