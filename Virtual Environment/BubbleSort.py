# ============================= BUBBLE SORT PRACTISE =============================


#--------------------- SIMPLE VERSION ----------------------------------
def bubble_sort(list1):   

    # loop for number of passes in list
    for i in range(0,len(list1)-1):  

        # compares current element to elemnt beside it and swaps them in needed
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  

    # retuns sorted list
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted first list is: ", list1)  # prints original list
print("The sorted first list is: ", bubble_sort(list1)) # prints sorted list



#----------------------- OMPTIMISED VERSION --------------------------------


def bubble_sort(list2):  

    # indicates tht the swap is true as elements need to be swapped
    has_swapped = True  
  
# while that hsa swapped is true, following loop with take effect and will exist once no swapping need be done
    while(has_swapped):  
        has_swapped = False  
        for i in range(len(list2) - 1):  
            if list2[i] > list2[i+1]:  
                # Swap  
                list2[i], list2[i+1] = list2[i+1], list2[i]  
                has_swapped = True  
    return list2  
  
list2 = [5, 3, 8, 6, 7, 2]  
print("\nThe unsorted second list is: ", list2)  # prints original list
print("The sorted second list is: ", bubble_sort(list2)) # prints sorted list