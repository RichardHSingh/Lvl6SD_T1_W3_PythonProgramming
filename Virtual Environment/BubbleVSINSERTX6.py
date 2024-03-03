# ============================= BUBBLE SORT VS INSERT SORT ALGORITHM =============================

import time 

def Bubble_Sort(setData):  
    # Initialize the flag to True, indicates swap has occurred
    has_swapped = True  
    
    # Continue the loop until no swaps are made in a pass
    while(has_swapped):  
        # Reset the flag before each pass
        has_swapped = False  
        
        # Iterate through the list
        for x in range(len(setData) - 1):  
            # Compare elements next to each other
            if setData[x] > setData[x+1]:  
                # Swap the elements if they are in the wrong order
                setData[x], setData[x+1] = setData[x+1], setData[x]  
                # Set the flag to True, indicating that a swap has occurred
                has_swapped = True  
    
    # Return the sorted list
    return setData  

# dataset usage
setData = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "mango", "peach", "pear", "watermelon",
"strawberry", "blueberry", "raspberry", "blackberry", "lemon", "lime", "cherry", "plum", "apricot", "fig",
"grapefruit", "pomegranate", "avocado", "papaya", "coconut", "passionfruit", "guava", "lychee", "dragonfruit",
"persimmon", "raspberry", "blackberry", "strawberry", "cranberry", "blueberry", "elderberry", "gooseberry",
"boysenberry", "currant", "huckleberry", "blackcurrant", "lingonberry", "mulberry", "raspberry", "sloeberry",
"marionberry", "tayberry", "loganberry"]

print(f"\n\nThe unsorted list for Bubble Sort is:\n{setData}\n")  


#calculating time taken 
start_time = time.time()

#-------------------------------------------------------

Bubble_Sort(setData)

#-------------------------------------------------------
end_time = time.time()

process_bubbleSort = end_time - start_time

print("\nThe sorted list for Bubbble Sort is:\n", Bubble_Sort(setData))

# will display time in seconds to to 6dp
print(f"\n\nTime taken to process BubbleSort: {process_bubbleSort:.6f} seconds\n\n\n")


#---------------------------- VS Insert-----------------------------------------

def Insert_Sort(setData1):
    # Traverse through the entire array starting from the second element
    for x in range(1, len(setData1)):

        # Store the current element to be compared
        current_element = setData1[x]
        
        # Move elements of array[0..i-1] that are greater than current_element
        # to one position ahead of their current position
        y = x - 1
        while y >= 0 and current_element < setData1[y]:
            setData1[y + 1] = setData1[y]
            y -= 1
        
        # Place the current element at its correct position in sorted order
        setData1[y + 1] = current_element

# dataset usage
setData1 = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "mango", "peach", "pear", "watermelon",
"strawberry", "blueberry", "raspberry", "blackberry", "lemon", "lime", "cherry", "plum", "apricot", "fig",
"grapefruit", "pomegranate", "avocado", "papaya", "coconut", "passionfruit", "guava", "lychee", "dragonfruit",
"persimmon", "raspberry", "blackberry", "strawberry", "cranberry", "blueberry", "elderberry", "gooseberry",
"boysenberry", "currant", "huckleberry", "blackcurrant", "lingonberry", "mulberry", "raspberry", "sloeberry",
"marionberry", "tayberry", "loganberry"]

print(f"Unsorted array for Insertion Sort:\n {setData1}")

Insert_Sort(setData1)

#calculating time taken 
start_time = time.time()

#-------------------------------------------------------

Insert_Sort(setData1)

#-------------------------------------------------------
end_time = time.time()

process_insertSort = end_time - start_time

print(f"\nSorted array:\n {setData1}")

# will display time in seconds to to 6dp
print(f"\n\nTime taken to process for Insertion Sort: {process_insertSort:.6f} seconds")