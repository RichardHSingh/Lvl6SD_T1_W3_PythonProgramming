import pandas as pd
import time
import timeit


# BUBBLE CODE
#======================================================================================================
def Bubble_Sort(rugbyAgeData):
    been_swapped = True  
    while been_swapped:
        been_swapped = False  
        for x in range(len(rugbyAgeData) - 1):  
            if rugbyAgeData[x] > rugbyAgeData[x+1]:  
                rugbyAgeData[x], rugbyAgeData[x+1] = rugbyAgeData[x+1], rugbyAgeData[x]  
                been_swapped = True  
    return rugbyAgeData  

# Read the Excel file into a DataFrame
# df = pd.read_excel('rugby_players_data-1.xlsx')
# df = pd.read_csv('rugby_players_data-1.csv')


# SORTED START
#======================================================================================================
# Get the 'Age' column data
# Age_column = df['Age']


# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # Timing the execution 
# start_time = time.time()

# #------------------------------------------------------------------------------------------------------

# Age_column_sorted = Bubble_Sort(Age_column.tolist())

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # Print the sorted 'Age' column data
# print("\nSorted 'Age' column:")
# print(pd.Series(Age_column_sorted).to_string())

# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Bubble Sort algorithm on 'Age' column: {execution_time:.10f} seconds")




# UNSORTED START
# ======================================================================================================
# # Get the 'Age' column data
# Age_column = df['Age'].tolist()

# # Print the original 'Age' column data
# print("Original 'Age' column:")
# print(pd.Series(Age_column).to_string())

# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # Timing the execution 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_unsorted = Bubble_Sort(Age_column.copy())

# # #------------------------------------------------------------------------------------------------------
# end_time = time.time()


# # Print the sorted 'Age' column data
# print("\nUnsorted 'Age' column:")
# print(pd.Series(Age_column_unsorted).to_string())

# # Print the execution time unsorted list
# execution_time = end_time - start_time
# print(f"\nExecution Time for Bubble Sort algorithm on 'Age' column: {execution_time:.10f} seconds")




# # REVERSE START
# #======================================================================================================
# # # Get the 'Age' column data
# Age_column = df['Age'].tolist()

# # .copy basically copies the original data and spits it out
# rugbydata_reversed = Age_column.copy()

# # calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Bubble_Sort(rugbydata_reversed)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# execution_time = end_time - start_time

# # Print the reversed array
# print(f"\nReversed array:\n{rugbydata_reversed[::-1]}")

# # Print the execution time
# print(f"\nExecution Time for reversing 'Age' column: {execution_time:.10f} seconds")








# EMPTY START
#======================================================================================================
# Get the 'Age' column data
# Age_column = []

# # Print the original 'Age' column data
# print("Empty 'Age' column(empty):")
# print(pd.Series(Age_column).to_string())


# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # # Timing the execution 
# start_time = time.time()
# # #------------------------------------------------------------------------------------------------------

# Age_column_sorted = Bubble_Sort(Age_column.copy())

# # #------------------------------------------------------------------------------------------------------
# end_time = time.time()


# # Print the sorted 'Age' column data
# print("\nEmpty 'Age' column:")
# print(pd.Series(Age_column_sorted).to_string())


# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Bubble Sort empty on 'Age' column: {execution_time:.10f} seconds")






# DUPLICATES START
#======================================================================================================
# Get the 'Age' column data
# Age_column = df['Age']

# # Check for duplicates in the 'Age' column
# bubble_sort_duplicates = Age_column.duplicated().any()


# # Print whether duplicates are found in the 'Age' column
# print(f"\n Duplicates in 'Age' column found? {'Yes' if bubble_sort_duplicates else 'No'}")

# # Apply bubble_sort to the 'Age' column and the data is converted to a list in order to do so

# # Timing the execution 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_sorted = Bubble_Sort(Age_column.tolist())

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# # Print the sorted 'Age' column data
# print("\nSorted 'Age' column:")
# print(pd.Series(Age_column_sorted).to_string())

# # Print the execution time
# execution_time = end_time - start_time
# print(f"\nExecution Time for Bubble Sort algorithm on 'Age' column: {execution_time:.10f} seconds")
