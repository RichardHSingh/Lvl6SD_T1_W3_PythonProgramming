# ============================= BINARY SEARCH EXERCISE =============================

import time
import random

# optimised version
def bubble_sort(mydata):  
    has_swapped = True  
  
    while(has_swapped):  
        has_swapped = False  
        for i in range(len(mydata) - 1):  
            if mydata[i] > mydata[i+1]:  
                # Swap  
                mydata[i], mydata[i+1] = mydata[i+1], mydata[i]  
                has_swapped = True  
    return mydata  
  
mydata = [ "apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "strawberry", "blueberry", "raspberry", "cherry",
         "pineapple", "mango", "watermelon", "pomegranate", "pear", "plum", "apricot", "fig", "lemon", "lime", "coconut", "avocado", 
       "blackberry", "cranberry", "guava", "passionfruit", "dragonfruit", "kiwifruit", "papaya" ]

print("\nThe unsorted list is: ", mydata)  
print("\n\nThe sorted list is: ", bubble_sort(mydata))

#==DATA NEEDS TO BE SORTED BEFORE BINARY SEARCH CAN BE ACHIEVED==#

def binarySearch(dataset, targetValue):
    left = 0
    right = len(dataset) - 1

    # splits the dataset down the middle --> left is low values --> right is high values
    while left <= right:
        mid = (left + right) // 2

        if dataset[mid] == targetValue:
            return mid
        
        if dataset[mid] < targetValue:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# EXERCISE 1
#===================================================================================================

# # my dataset list
# dataset = [12, 24, 30, 42, 55, 63, 75, 82, 91, 99]

# # my targeted value in list
# targetValue = 12

# # start recording the time taken to process everything
# start_time = time.time()

# #--------------------------------------------------------------------------------------

# result = binarySearch(dataset, targetValue)

# #--------------------------------------------------------------------------------------
# # ending recording the time taken to process everything
# end_time = time.time()

# # calculating the time time taken using simple math
# execution_time = end_time - start_time

# if result != -1:
#     print(f"\nValue {targetValue} found at index {result}. Executed in {execution_time:.10f} seconds\n")
# else:
#     print(f"\nValue {targetValue} not found in the list\n")



# EXERCISE 2
#===================================================================================================

# # my dataset list
# dataset = [ "apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "strawberry", "blueberry", "raspberry", "cherry",
#         "pineapple", "mango", "watermelon", "pomegranate", "pear", "plum", "apricot", "fig", "lemon", "lime", "coconut", "avocado", 
#         "blackberry", "cranberry", "guava", "passionfruit", "dragonfruit", "kiwifruit", "papaya" ]

# # my targeted value in list
# targetValue = "papaya"

# # to add another value
# # targetValue2 = "value" and call in formated string as needed

# # Sort the dataset
# sorted_data = bubble_sort(dataset.copy())

# # Start recording the time taken to process everything
# start_time = time.time()

# # Perform binary search on the sorted dataset
# result = binarySearch(sorted_data, targetValue)

# # End recording the time taken to process everything
# end_time = time.time()

# # Calculate the time taken using simple math
# execution_time = end_time - start_time

# if result != -1:
#     print(f"\nValue {targetValue} found at index {result}. Executed in {execution_time:.10f} seconds\n")
# else:
#     print(f"\nValue {targetValue} not found in the list\n")



# # EXERCISE 3
# #===================================================================================================

# # my random ataset to find appropriate value
# randomised_list = [random.randint(1, 100) for _ in range(30)]

# # chosen value
# targetValue = 69

# # start recording the time taken to process everything
# start_time = time.time()

# #--------------------------------------------------------------------------------------

# # giving my randomised list a new variable and calling it and defining it as my def name with name of list and what the targets value is
# result_search = binarySearch(randomised_list, targetValue)

# #--------------------------------------------------------------------------------------
# # ending recording the time taken to process everything
# end_time = time.time()

# # calculating the time time taken using simple math
# execution_time = end_time - start_time

# if result_search != -1:
#     print(f"\nValue {targetValue} found at index {result_search}. Executed in {execution_time:.10f} seconds\n")
# else:
#     print(f"\nValue {targetValue} not found in the list\n")
