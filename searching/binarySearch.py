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