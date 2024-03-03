import time
import random


# function to run linear search
# used bubble sort to organise the list
def linearSearch(list, targetValue):
    # loop for search through listay and finding intented value
    for x in range(len(list)):
        # x = index to go through until index matches the targeted value
        if list[x] == targetValue:
            return x
        #if the given value isnt found in the list, -1 is the output
    return -1



# EXERCISE 1
#===================================================================================================

# # my dataset to find appropriate value
# list = [12, 24, 30, 42, 55, 63, 75, 82, 91, 99]

# # chosen value
# targetValue = 63

# # start recording the time taken to process everything
# start_time = time.time()

# #--------------------------------------------------------------------------------------

# result = linearSearch(list, targetValue)

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

# # my dataset to find appropriate value
# list = [ "apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "strawberry", "blueberry", "raspberry", "cherry", "pineapple",
#         "mango", "watermelon", "pomegranate", "pear", "plum", "apricot", "fig", "lemon", "lime", "coconut", "avocado", "blackberry", 
#         "cranberry", "guava", "passionfruit", "dragonfruit", "kiwifruit", "papaya" ]

# # chosen value
# targetValue = "boat"

# # start recording the time taken to process everything
# start_time = time.time()

# #--------------------------------------------------------------------------------------

# result = linearSearch(list, targetValue)

# #--------------------------------------------------------------------------------------
# # ending recording the time taken to process everything
# end_time = time.time()

# # calculating the time time taken using simple math
# execution_time = end_time - start_time

# if result != -1:
#     print(f"\nValue {targetValue} found at index {result}. Executed in {execution_time:.10f} seconds\n")
# else:
#     print(f"\nValue {targetValue} not found in the list\n")




# EXERCISE 3
#===================================================================================================

# # my random ataset to find appropriate value
# randomised_list = [random.randint(1, 100) for _ in range(30)]

# # chosen value
# targetValue = 69

# # start recording the time taken to process everything
# start_time = time.time()

# #--------------------------------------------------------------------------------------

# # giving my randomised list a new variable and calling it and defining it as my def name with name of list and what the targets value is
# result_search = linearSearch(randomised_list, targetValue)

# #--------------------------------------------------------------------------------------
# # ending recording the time taken to process everything
# end_time = time.time()

# # calculating the time time taken using simple math
# execution_time = end_time - start_time

# if result_search != -1:
#     print(f"\nValue {targetValue} found at index {result_search}. Executed in {execution_time:.10f} seconds\n")
# else:
#     print(f"\nValue {targetValue} not found in the list\n")
