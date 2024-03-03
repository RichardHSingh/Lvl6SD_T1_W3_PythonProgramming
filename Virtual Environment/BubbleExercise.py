# ============================= BUBBLE SORT EXERCISE =============================

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

# Example usage
setData = [67, 12, 89, 43, 56, 34, 78, 23, 91, 
           45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 
           47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

#calculating time taken 
# start_time = time.time()
# Bubble_Sort(setData)
# end_time = time.time()



start_time = time.time()

end_time = time.time() 

process_time_take = end_time - start_time

print(f"\n\nThe unsorted list is:\n{setData}\n")  
print("\nThe sorted list is:\n", Bubble_Sort(setData))

# will display time in seconds to to 6dp
print(f"\n\nTime taken to process: {process_time_take:.6f} seconds")


