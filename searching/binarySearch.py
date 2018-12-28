"""
With a sorted data set we can take advantage of the ordering to make a search which is more efficient than going element by element. 

Binary search requires a sorted data-set. We then take the following steps:

Check the middle value of the dataset.

If this value matches our target we can return the index.
If the middle value is less than our target

Start at step 1 using the right half of the list.
If the middle value is greater than our target

Start at step 1 using the left half of the list.
We eventually run out of values in the list, or find the target value.

It would be important to know how the list is sorted because this would indicate how your conditional should be. 

Binary Search O (log N) 

each iteration we are cutting the list in half. 

sorted list of 64 elements will take at most log2(64) = 6 comparisons.

while the speed of the binary search algorithm is great it does not work with every data set. It would only be effective for a sorted list. 

 the worst case:

Comparison 1: We look at the middle of all 64 elements

Comparison 2: If the middle is not equal to our search value, we would look at 32 elements

Comparison 3: If the new middle is not equal to our search value, we would look at 16 elements

Comparison 4: If the new middle is not equal to our search value, we would look at 8 elements

Comparison 5: If the new middle is not equal to our search value, we would look at 4 elements

Comparison 6: If the new middle is not equal to our search value, we would look at 2 elements

When there's 2 elements, the search value is either one or the other, and thus, there is at most 6 comparisons in a sorted list of size 64.
"""

def binary_search(sorted_list, target):
    """
    Binary Search algorithm O(log(N)) run time. Requires a sorted list for efficiency. 
    Here's a recap of the algorithm:

    Check the middle value of the dataset.

    If this value matches our target we return the target value index.
    If the middle value is greater than our target

    Begin at step 1 using the left half of the list.
    If the middle value is less than our target

    Begin at step 1 using the right half of the list.

    Uses recursion 
    """
    #Using recursion requires base case.  Two will be used 

    #list is empty base case 1. 
    if not sorted_list: # could also if len(sorted_list) == 0: 
        return "value not found"
    #create middle index and get the value of that index 
    mid_idx = len(sorted_list) // 2 #floor division 
    mid_val = sorted_list[mid_idx]
    """
    three options for second base case 
    mid_val matches target 
    mid_val less than target step to reach base case
    mid_val greater than target step to reach base case
    """
    #conditional check for mid_val matches target
    if mid_val == target: #second base case. 
        return mid_idx 
    #conditional check if mid_val is greater than target 
    if mid_val > target:
        #create a left half variable with 0 up to but not inculding the mid_idx we have already checked for that
        left_half = sorted_list[:mid_idx]
        #recrusively return a call to binary search using left half as sorted list 
        return binary_search(left_half, target)
    #conditional check if mid_val is less than target 
    if mid_val < target: 
        #create a right_half variable with mid_idx + 1 (already checked mid_idx) to the end of the list 
        right_half = sorted_list[mid_idx + 1 :]
        #store call to binary search in a variable. 
        result = binary_search(right_half, target)
        """
        Why store the above in a variable?  We are making a smaller copy of the sorted list at each recursive call, so our indices for the same value
        change.   

        sorted_list = [7, 8, 9, 10, 11]
        right_half = [10, 11]

        # index of "11" in sorted_list: 4
        # index of "11" in right_half: 1

        we will need to return mid_idx + 1 to account for  segments of the lists we've discarded. as long as result is not "value not found"
        """
        if result is "value not found":
            return result
        return result + mid_idx + 1
#end of function 
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))




