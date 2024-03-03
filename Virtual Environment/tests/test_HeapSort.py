# #============================= HEAP SORT ALGORITHM PYTEST =============================

# # file name to big, using alias
# import HeapAlgorithm as hp
# import pandas as pd
# import time

# # command for pytest: pytest -s -v


# df = pd.read_csv("rugby_players_data-1.csv")

# rugbyAgeData = df["Age"].tolist()
# sorted_data = sorted(rugbyAgeData.copy()) 


# # SORTED CODE
# #======================================================================================================
# def test_Sorted():
#     start_time = time.time()    
#     data_copy = sorted_data.copy()
#     hp.heapSort(data_copy)
#     assert data_copy == sorted_data    
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"Execution Time for test_Sorted: {execution_time} seconds")




# # EMPTY CODE
# #======================================================================================================
# def test_Empty():
#     rugbyAgeData = []
#     start_time = time.time()
#     assert hp.heapSort(rugbyAgeData) == []
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Quick Sort EMPTY on 'Age' column: {execution_time:.3f} seconds\n")



# # UNSORTED CODE
# #======================================================================================================
# def test_Unsorted():
#     start_time = time.time()
#     assert hp.heapSort(rugbyAgeData) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Quick Sort UNSORTED on 'Age' column: {execution_time:.3f} seconds\n")

    

# # REVERSED CODE
# #======================================================================================================
# def test_Reversed():
#     reverse_list = sorted(rugbyAgeData)
#     reverse_list.reverse()
#     start_time = time.time()
#     assert hp.heapSort(reverse_list) == sorted_data
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Quick Sort REVERSED on 'Age' column: {execution_time:.3f} seconds\n")

    

# # DUPLICATES CODE
# #======================================================================================================
# def test_Duplicate():
#     duplicate = rugbyAgeData * 2
#     start_time = time.time()
#     assert hp.heapSort(duplicate) == sorted(duplicate)
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"\nExecution Time for Quick Sort DUPLICATES on 'Age' column: {execution_time:.3f} seconds\n")