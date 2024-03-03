# ============================= MERGE SORT ALGORITHM =============================

import pandas as pd
import time

# MERGE CODE
#======================================================================================================

# Function to perform Merge Sort on DataFrame
def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        Merge_Sort(left)
        Merge_Sort(right)

        x = y = z = 0

        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                arr[z] = left[x]
                x += 1
            else:
                arr[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            arr[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            arr[z] = right[y]
            y += 1
            z += 1

# Read the Excel file
df = pd.read_csv("rugby_players_data-1.csv")



# SORTED CODE
#======================================================================================================
# Perform Merge Sort on the DataFrame based on the 'Age' column
Age_column = df['Age']

start_time = time.time()
#------------------------------------------------------------------------------------------------------

# No need to assign the result to a new variable
Merge_Sort(Age_column.tolist())

#------------------------------------------------------------------------------------------------------
end_time = time.time()

execution_time = end_time - start_time

# Display only the 'Age' column in the sorted DataFrame
print("\nSorted 'Age' column:")
print(pd.Series(Age_column).to_string())

# Display the sorted 'Age' column
print("\nThe sorted 'Age' column is:\n", Age_column.tolist())
print(f"\n\nTime taken to process Merge Sort: {execution_time:.10f} seconds")

        



# UNSORTED CODE
#======================================================================================================
# Get the 'Age' column data
# age_column_unsorted = df['Age'].tolist()

# # Print the original 'Age' column data
# print("Original 'Age' column:", end=" ")
# print(*age_column_unsorted)

# # Timing the execution 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# # Apply Merge_Sort to the 'Age' column
# Merge_Sort(age_column_unsorted)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # using end=" " data gets printed in rows not coluimn
# # Print the sorted 'Age' column data
# print("\nSorted 'Age' column:", end=" ")
# print(*age_column_unsorted)

# # Print the execution time for the unsorted list
# execution_time = end_time - start_time
# print(f"\nExecution Time for Merge Sort algorithm on 'Age' column: {execution_time:.10f} seconds")






# REVERSED CODE
#======================================================================================================
#Perform Merge Sort on the DataFrame based on the 'Age' column

# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# age_column_reverse = df['Age'][::-1]

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()


# process_reverse = end_time - start_time

# print("\nThe 'Age' column in reverse order is:\n", end=" ")
# print(*age_column_reverse)
# print(f"\n\nTime taken to process Reverse Display: {process_reverse:.10f} seconds\n")
    



# # EMPTY CODE
# # ======================================================================================================
# Age_column = []    

# start_time = time.time()
# # ------------------------------------------------------------------------------------------------------

# # Convert the 'Age' column to a list, sort it in descending order, and then assign it back to the DataFrame

# Age_column = Merge_Sort(Age_column.copy())

# # ------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # Display the sorted 'Age' column in descending order
# print("\nSorted 'Age' column:")
# print(pd.Series(Age_column).to_string(index=False))

# execution_time = end_time - start_time 

# print(f"\n\nTime taken to process Merge Sort in descending order: {execution_time:.10f} seconds\n")




# DUPLICATES CODE
# ======================================================================================================
    
# # Get the 'Age' column data
# age_column_unsorted = df['Age'].tolist()

# # Timing the execution
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# # Apply Merge Sort to the 'Age' column
# Merge_Sort(age_column_unsorted)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # Print whether duplicates are found in the 'Age' column after Merge Sort
# duplicates_after_merge_sort = any(pd.Series(age_column_unsorted).duplicated())
# print(f"\nDuplicates in 'Age' column found after Merge Sort? {'Yes' if duplicates_after_merge_sort else 'No'}")

# # Print the sorted 'Age' column data
# print("\nSorted 'Age' column:")
# print(*age_column_unsorted)

# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Merge Sort algorithm on 'Age' column: {execution_time:.10f} seconds")
