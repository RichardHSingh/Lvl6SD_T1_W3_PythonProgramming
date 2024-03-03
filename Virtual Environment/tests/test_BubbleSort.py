# # ============================= BUBBLE SORT ALGORITHM PYTEST=============================


# # file name to big, using alias
# import BubbleAlgorithm as bub 
# import pandas as pd
# import time

# # command for pytest: pytest -s -v


# df = pd.read_csv('rugby_players_data-1.csv')
# rugbyAgeData = df["Age"].tolist()
# sorted_data = sorted(rugbyAgeData)  


# # SORTED CODE
# #======================================================================================================
# def test_Sorted():
#     start_time = time.time()
#     # the def needs to match from orignal file you importing from
#     assert bub.Bubble_Sort(sorted_data) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Bubble Sort SORTED on 'Age' column: {execution_time/2:.3f} seconds")



# # EMPTY CODE
# #======================================================================================================
# def test_Empty():
#     rugbyAgeData = []
#     start_time = time.time()
#     assert bub.Bubble_Sort(rugbyAgeData) == []
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Bubble Sort EMPTY on 'Age' column: {execution_time:.3f} seconds")



# # UNSORTED CODE
# #======================================================================================================
# def test_Unsorted():
#     start_time = time.time()
#     assert bub.Bubble_Sort(rugbyAgeData) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Bubble Sort UNSORTED on 'Age' column: {execution_time:.3f} seconds")

    

# # REVERSED CODE
# #======================================================================================================
# def test_Reversed():
#     reverse_list = sorted(rugbyAgeData)
#     reverse_list.reverse()
#     start_time = time.time()
#     assert bub.Bubble_Sort(reverse_list) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Bubble Sort REVERSED on 'Age' column: {execution_time:.3f} seconds")

    

# # DUPLICATES CODE
# #======================================================================================================
# def test_Duplicate():
#     duplicate = rugbyAgeData * 2
#     start_time = time.time()
#     assert bub.Bubble_Sort(duplicate) == sorted(duplicate)
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Bubble Sort DUPLICATES on 'Age' column: {execution_time:.3f} seconds")