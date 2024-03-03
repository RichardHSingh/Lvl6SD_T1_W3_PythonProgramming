# ============================= HEAP SORT ALGORITHM =============================


import pandas as pd
import time

# Function to heapify the subtree rooted at index i in a max heap
def heapify(rugbyAgeData, x, i):
    # Find the largest among the root and its children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left child exists and is greater than the root
    if l < x and rugbyAgeData[i] < rugbyAgeData[l]:
        largest = l

    # Check if right child exists and is greater than the current largest
    if r < x and rugbyAgeData[largest] < rugbyAgeData[r]:
        largest = r

    # If the root is not the largest, swap with the largest and continue heapifying
    if largest != i:
        rugbyAgeData[i], rugbyAgeData[largest] = rugbyAgeData[largest], rugbyAgeData[i]
        heapify(rugbyAgeData, x, largest)

# Function to perform Heap Sort on the given rugbyAgeData
def heapSort(rugbyAgeData):
    x = len(rugbyAgeData)

    # Build max heap (rearrange array)
    # Start from the last non-leaf node and heapify all nodes in reverse order
    for i in range(x // 2, -1, -1):
        heapify(rugbyAgeData, x, i)

    # One by one extract elements
    for i in range(x - 1, 0, -1):
        # Swap the current root with the last element
        rugbyAgeData[i], rugbyAgeData[0] = rugbyAgeData[0], rugbyAgeData[i]

        # Heapify the reduced heap (exclude the sorted elements)
        heapify(rugbyAgeData, i, 0)

# Read the Excel file into a DataFrame
df = pd.read_csv("rugby_players_data-1.csv")



# SORTED START
#======================================================================================================
# Get the 'Age' column data
Age_column = df['Age']

# Convert the 'Age' column to a list
age_list = Age_column.tolist()

# Timing the execution 
start_time = time.time()

#------------------------------------------------------------------------------------------------------
# Perform Heap Sort on the 'Age' column
heapSort(age_list)

#------------------------------------------------------------------------------------------------------
end_time = time.time()

# Print the sorted 'Age' column data
print("\nSorted 'Age' column:")
print(pd.Series(age_list).to_string())

# Print the execution time
execution_time = end_time - start_time
print(f"\nExecution Time for Heap Sort algorithm on 'Age' column: {execution_time:.10f} seconds")



# UNSORTED START
# ======================================================================================================
# # Get the 'Age' column data
# Age_column = df['Age']

# # # Convert the 'Age' column to a list
# age_list = Age_column.tolist()

# # Print the original 'Age' column data
# print("Original 'Age' column:")
# print(pd.Series(Age_column).to_string())

# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # Timing the execution 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_unsorted = heapSort(Age_column.copy())

# # #------------------------------------------------------------------------------------------------------
# end_time = time.time()


# # Print the execution time unsorted list
# execution_time = end_time - start_time
# print(f"\nExecution Time for Heap Sort algorithm on 'Age' column: {execution_time:.10f} seconds")



# REVERSE START
#======================================================================================================
# Get the 'Age' column data
# Age_column = df['Age']

# # # Convert the 'Age' column to a list
# age_list = Age_column.tolist()

# # .copy basically copies the original data and spits it out
# Age_Column_reversed = Age_column.copy()

# # calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_unsorted = heapSort(Age_column.copy())

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# execution_time = end_time - start_time

# # Print the reversed array
# print(f"\nReversed array:\n{Age_Column_reversed[::-1]}")

# # Print the execution time
# print(f"\nExecution Time for Heap Sort algorithm 'Age' column: {execution_time:.10f} seconds")


# EMPTY START
#======================================================================================================
# Get the 'Age' column data
# Age_column = []

# # # Timing the execution 
# start_time = time.time()
# # ------------------------------------------------------------------------------------------------------

# Age_column_empty = heapSort(Age_column.copy())

# # ------------------------------------------------------------------------------------------------------
# end_time = time.time()


# # Print the sorted 'Age' column data
# print("\nEmpty 'Age' column:")
# print(pd.Series(Age_column_empty).to_string())
# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so


# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Heap Sort algorithm on 'Age' column: {execution_time:.10f} seconds")



# DUPLICATES START
#======================================================================================================
# Get the 'Age' column data
# Age_column = df['Age']

# # Check for duplicates in the 'Age' column
# heapSort_duplicates = Age_column.duplicated().any()


# # Print whether duplicates are found in the 'Age' column
# print(f"\n Duplicates in 'Age' column found? {'Yes' if heapSort_duplicates else 'No'}")

# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # Timing the execution 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_sorted = heapSort(Age_column.tolist())

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # Print the sorted 'Age' column data
# print("\Duplicates 'Age' column:")
# print(pd.Series(heapSort_duplicates).to_string())

# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Heap Sort algorithm on 'Age' column: {execution_time:.10f} seconds")
