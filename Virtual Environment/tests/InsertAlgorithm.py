import pandas as pd
import time


# INSERT CODE
#======================================================================================================
def Insert_Sort(rugbyAgeData):
    totalnum = len(rugbyAgeData)
    for x in range(totalnum):
        y = x
        while y > 0 and rugbyAgeData[y - 1] > rugbyAgeData[y]:
            rugbyAgeData[y], rugbyAgeData[y - 1] = rugbyAgeData[y - 1], rugbyAgeData[y]
            y = y - 1
    return rugbyAgeData



# Read the Excel file into a DataFrame
df = pd.read_csv('rugby_players_data-1.csv')



# SORTED START
#======================================================================================================
# Reading the Age column from file
# rugbyAgeData = df['Age'].to_list()

# print(f"Unsorted array:\n {rugbyAgeData}")


# #calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Insert_Sort(rugbyAgeData)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# print(f"\nSorted array:\n {rugbyAgeData}")

# # will display time in seconds to to 6dp
# print(f"\n\nTime taken to process Insert Sort sorted: {process_time_taken:.10f} seconds")





# UNSORTED START
#======================================================================================================
# rugbyAgeData = df['Age'].to_list()

# print(f"Unsorted array:\n {rugbyAgeData}")


# # .copy basically copies the original data nd spits it out
# rugbydata_unsorted = rugbyAgeData.copy()

# #calculating time taken 
# start_time = time.time()

# #------------------------------------------------------------------------------------------------------

# Insert_Sort(rugbydata_unsorted)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# print(f"\nUnsorted array:\n {rugbyAgeData}")

# # will display time in seconds to to 6dp
# print(f"\n\nTime taken to process Insert Sort sorted: {process_time_taken:.10f} seconds")




# REVERSED START
#======================================================================================================
# Reading the Age column from file
# rugbyAgeData = df['Age'].to_list()

# ##print(f"Reversed array:\n {rugbyAgeData}")


# # .copy basically copies the original data nd spits it out
# rugbydata_reversed = rugbyAgeData.copy()


# #calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Insert_Sort(rugbydata_reversed)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# print(f"\n Reversed array:\n {rugbyAgeData[::-1]}")

# # will display time in seconds to to 6dp
# print(f"\n\nTime taken to process Insert Sort reversed: {process_time_taken:.10f} seconds")



# EMPTY START
#======================================================================================================
# Reading the Age column from file
# rugbyAgeData = df['Age'].to_list()
 

# # .copy basically copies the original data nd spits it out
# rugbydata_empty = []

# #calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Insert_Sort(rugbydata_empty)

# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# print(f"\n Empty array:\n {rugbydata_empty}")

# # will display time in seconds to to 6dp
# print(f"\n\n Time taken to process Insert Sort empty: {process_time_taken:.10f} seconds")





# DUPLICATES START
#======================================================================================================
# Identify duplicate values in the 'Age' column
# rugbyAgeData_duplicate = df.duplicated(subset=['Age']).any()

# print(f"Are there duplicates in 'Age' column? {'Yes' if rugbyAgeData_duplicate else 'No'}")

# # .copy basically copies the original data and spits it out
# rugbydata_duplicate = df['Age'].copy()

# # calculating time taken 
# start_time = time.time()
# #------------------------------------------------------------------------------------------------------

# Insert_Sort(rugbydata_duplicate.tolist())
# #------------------------------------------------------------------------------------------------------
# end_time = time.time()

# process_time_taken = end_time - start_time

# # will display time in seconds to 6 decimal places
# print(f"\nTime taken to process Insert Sort duplicate: {process_time_taken:.6f} seconds")




# OLD FUNCTION CODE
#======================================================================================================
    # # Traverse through the entire array starting from the second element
    # for x in range(1, len(rugbyAgeData)):

    #     # Store the current element to be compared
    #     current_element = rugbyAgeData[x]
        
    #     # Move elements of array[0..i-1] that are greater than current_element
    #     # to one position ahead of their current position
    #     y = x - 1
    #     while y >= 0 and current_element < rugbyAgeData[y]:
    #         rugbyAgeData[y + 1] = rugbyAgeData[y]
    #         y -= 1
        
    #     # Place the current element at its correct position in sorted order
    #     rugbyAgeData[y + 1] = current_element