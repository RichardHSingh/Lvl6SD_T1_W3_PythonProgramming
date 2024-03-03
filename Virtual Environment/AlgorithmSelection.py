# ============================= SELECTION SORT ALGORITHM =============================

import pandas as pd
import time


# SELECTION CODE
#======================================================================================================
def Selection_Sort(rugbyAgeData):
    # getting length of the input list/dataset
    n = len(rugbyAgeData)

    # iterates through list whilst leaving last element alone
    for x in range(n - 1):
        min_index = x

        # loops through unsroted list to find minimum element 
        for y in range(x + 1, n):
            # compares current position against smallest element found thus far then updates it if smaller element found
            if rugbyAgeData[y] < rugbyAgeData[min_index]:
                min_index = y

        #swaps minimum element that has been found with the first one -- unsorted list
        rugbyAgeData[x], rugbyAgeData[min_index] = rugbyAgeData[min_index], rugbyAgeData[x]

    # will return list that has been sorted
    return rugbyAgeData


# EXCEL FILE
#======================================================================================================
df = pd.read_csv("rugby_players_data-1.csv")
# reading excel file provided


# REVERSED START
#======================================================================================================
# Age_column = df['Age'].to_list()
# rugbyData_reversed = Age_column.copy()


## time optimisation
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------
# Age_column_unsorted = Selection_Sort(Age_column.copy())
# rugbyDataReverse = Age_column_unsorted[::-1]
# #------------------------------------------------------------------------------------------------------
# print(rugbyDataReverse)
# end_time = time.time()


# execution_time = end_time - start_time
# print(f"\nExecution Time for Selection Sort algorithm on 'Age' column: {execution_time:.10f} seconds")





# EMPTY START
#======================================================================================================
## to return empty list, use for an empty list
# Age_column = df['Age'].tolist()
# Age_column = []


# # time optimisation
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------
# Age_column = Selection_Sort(Age_column.copy())  # --> use for empty and unsorted
# #------------------------------------------------------------------------------------------------------
# print(pd.Series(Age_column).to_string())
# end_time = time.time()


# execution_time = end_time - start_time
# print(f"\nExecution Time for Selection Sort algorithm on 'Age' column: {execution_time:.10f} seconds")





# # SORTED START
# #======================================================================================================
# Age_column = df['Age'].tolist()

# start_time = time.time()
# # ------------------------------------------------------------------------------------------------------

# Age_column_unsorted = Selection_Sort(Age_column.copy())
# Age_column_sorted = Selection_Sort(Age_column_unsorted.copy())  

# # ------------------------------------------------------------------------------------------------------
# end_time = time.time()

# print(Age_column_sorted)

# execution_time = end_time - start_time
# print(f"\nExecution Time for Selection Sort algorithm on 'Age' column: {execution_time:.10f} seconds")





# UNSORTED START
#======================================================================================================
# Age_column = df['Age'].tolist()

# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Age_column_unsorted = Age_column.copy()  # Use the original unsorted data
# Age_column_sorted = Selection_Sort(Age_column_unsorted.copy())

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# print(Age_column_unsorted)  # use for unsorted


# execution_time = end_time - start_time
# print(f"\nExecution Time for Selection Sort algorithm on 'Age' column: {execution_time:.10f} seconds")




# DUPLICATES START
# ======================================================================================================
# Age_column = df['Age'].tolist()


# selectionSort = any(Age_column.count(item) > 1 for item in Age_column)
# print(f"\nDuplicates in 'Age' column found? {'Yes' if selectionSort else 'No'}")

# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# rugbyDataReverse = Selection_Sort(Age_column.copy())
# rugbyDataReverse = rugbyDataReverse[::-1]  

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# print(pd.Series(rugbyDataReverse).to_string())  # Fixed: Use rugbyDataReverse instead of Age_column_sorted



# execution_time = end_time - start_time
# print(f"\nExecution Time for Selection Sort algorithm on 'Age' column: {execution_time:.10f} seconds")

