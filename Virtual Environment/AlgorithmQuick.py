# ============================= QUICK SORT ALGORITHM =============================

import pandas as pd
import time
import random


def swap(rugbyAgeData, x, y):

    # swaps the element around between pos x and y in given dataset
    temp = rugbyAgeData[x]
    rugbyAgeData[x] = rugbyAgeData[y]
    rugbyAgeData[y] = temp


def partition(rugbyAgeData, lo, hi):

    # pivot is randomly selected, swaps with first element and splits the list into lower/higher values
    # lower/high values is compared to pivot before split occurs
    r = random.randint(lo, hi)
    rugbyAgeData[lo], rugbyAgeData[r] = rugbyAgeData[r], rugbyAgeData[lo]
    
    pivot = rugbyAgeData[lo]
    (i, j) = (lo - 1, hi + 1)
    
    x = lo  # Initialize x before the first loop
    y = hi + 1
    
    while True:
        while True:
            x += 1
            if rugbyAgeData[x] >= pivot:
                break # break occurs when element is > or = to pivot when found on x
        while True:
            y -= 1
            if rugbyAgeData[y] <= pivot:
                break # break occurs when element is > or = to pivot when found on y
        if x >= y:
            return y
        swap(rugbyAgeData, x, y)


def qsort(rugbyAgeData, lo, hi):

    if lo >= hi -1:
        return
    pivot = partition(rugbyAgeData, lo, hi)
    qsort(rugbyAgeData, lo, pivot)
    qsort(rugbyAgeData, pivot + 1, hi)
    

# -> list decodes that the return should be a list
def quick_sort(rugbyAgeData) -> list:
    
    #applies quicksort to dataset privded and returns unsorted list to sorted
    qsort(rugbyAgeData, 0, len(rugbyAgeData) - 1)
    return rugbyAgeData
    
    

if __name__ == '__main__':
    # Read the Excel file into a DataFrame
    df = pd.read_csv("rugby_players_data-1.csv")


# SORTED CODE
#======================================================================================================
    
# # Perform Quick Sort on the 'Age' column
# start_time = time.time()

# # #------------------------------------------------------------------------------------------------------

# # Extract the 'Age' column values as a list and sort it using quicksort
# sorted_age_data = quick_sort(df['Age'].tolist())

# # #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_quick_sort = end_time - start_time

# # Display the sorted 'Age' column
# print("\n The sorted 'Age' column is:\n", sorted_age_data)
# print(f"\n\nTime taken to process Quick Sort Algorithm: {process_quick_sort:.10f} seconds")




# # UNSORTED CODE
# #======================================================================================================
# Perform Merge Sort on the DataFrame based on the 'Age' column

# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# sorted_df = pd.DataFrame(df[['Age']])

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_merge_sort = end_time - start_time

# # Display only the 'Age' column without sorting
# age_column = df['Age']

# # Display the 'Age' column
# print("\nThe 'Age' column is:\n", age_column)

# print(f"\n\nTime taken to process Merge Sort: {process_merge_sort:.10f} seconds")
    



# REVERSED CODE
#======================================================================================================
# Perform Merge Sort on the DataFrame based on the 'Age' column

# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# age_column_reverse = df['Age'][::-1]

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()


# process_reverse = end_time - start_time

# print("\nThe 'Age' column in reverse order is:\n", age_column_reverse)
# print(f"\n\nTime taken to process Reverse Display: {process_reverse:.10f} seconds\n\n\n")
    



# EMPTY START
#======================================================================================================
# Reading the Age column from file
# rugbyAgeData = df['Age'].to_list()
 

# # .copy basically copies the original data nd spits it out
# rugbydata_empty = []

# #calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# quick_sort(rugbydata_empty)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# print(f"\n Empty array:\n {rugbydata_empty}")

# # will display time in seconds to to 6dp
# print(f"\n\n Time taken to process Insert Sort empty: {process_time_taken:.10f} seconds")
    


# DUPLICATES START
#======================================================================================================
# # Identify duplicate values in the 'Age' column
# # Check for duplicates in the 'Age' column
# rugbyAgeData_duplicate = df.duplicated(subset=['Age']).any()

# # Output if there are duplicates
# print(f"Are there duplicates in 'Age' column? {'Yes' if rugbyAgeData_duplicate else 'No'}")

# # Create a copy of the 'Age' column
# rugbydata_duplicate = df['Age'].copy()

# # Calculate time taken for Quick Sort on duplicates
# start_time = time.time()
# # ------------------------------------------------------------------------------------------------------

# # Sort the 'Age' column directly, no need to convert to DataFrame
# sorted_duplicates = quick_sort(rugbydata_duplicate)

# # ------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# # Display the sorted 'Age' column for duplicates
# print("\nThe sorted 'Age' column for duplicates is:\n", sorted_duplicates)
# print(f"\nTime taken to process Quick Sort on duplicates: {process_time_taken:.10f} seconds")