# # ============================= INSERT SORT ALGORITHM PYTEST =============================

# # file name to big, using alias
# import InsertAlgorithm as sert
# import pandas as pd
# import time

# # command for pytest: pytest -s -v


# df = pd.read_csv(r'rugby_players_data-1.csv')

# rugbyAgeData = df["Age"].tolist()
# sorted_data = sorted(rugbyAgeData)  


# # SORTED CODE
# #======================================================================================================
# def test_Sorted():
#     start_time = time.time()
#     # the def needs to match from orignal file you importing from
#     assert sert.Insert_Sort(sorted_data) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Insert Sort SORTED on 'Age' column: {execution_time:.3f} seconds\n")




# # EMPTY CODE
# #======================================================================================================
# def test_Empty():
#     rugbyAgeData = []
#     start_time = time.time()
#     assert sert.Insert_Sort(rugbyAgeData) == []
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Insert Sort EMPTY on 'Age' column: {execution_time:.3f} seconds\n")



# # UNSORTED CODE
# #======================================================================================================
# def test_Unsorted():
#     start_time = time.time()
#     assert sert.Insert_Sort(rugbyAgeData) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Insert Sort UNSORTED on 'Age' column: {execution_time:.3f} seconds\n")

    

# # REVERSED CODE
# #======================================================================================================
# def test_Reversed():
#     reverse_list = sorted(rugbyAgeData)
#     reverse_list.reverse()
#     start_time = time.time()
#     assert sert.Insert_Sort(reverse_list) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Insert Sort REVERSED on 'Age' column: {execution_time:.3f} seconds\n")

    

# # DUPLICATES CODE
# #======================================================================================================
# def test_Duplicate():
#     duplicate = rugbyAgeData * 2
#     start_time = time.time()
#     assert sert.Insert_Sort(duplicate) == sorted(duplicate)
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Insert Sort DUPLICATES on 'Age' column: {execution_time:.3f} seconds\n")