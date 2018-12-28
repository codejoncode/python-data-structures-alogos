"""
Linear search or sequential search algorithm sequentially checks whether a given value is an element of a specified list by scanning 
the elements of a list one by one. it checks every item in the list in order from beginning to end until it finds a target value. 

If it finds the target value in the list, the linear search algorithm stops and returns the position in the list corresponding to the target value. 
If it does not find the value a message is returned that pretty much states it is not in the list. 

The steps are:

Examine the first element of the list.
If the first element is equal to the target value, stop.
If the first element is not equal to the target value, check the next element in the list.
Continue steps 1-3 until the element is found or the end of the list is reached.

Best Case performance    O(1)    

Linear search is not considered the most efficient search algorithm, especially for large lists.   It is a great choice if you expect to find the target
value at the beginning of the lists, or if you have a small list. 

Also works well if the item is in the list.  Imagine checking a list of 10 million items and it doesn't exist , waste of time. 

Worse case Performance   target is at the end of the list,   or target does not exist. O(N)

Average Case performance  O(n/2) which is O(n)

Linear search runs in linear time. 
"""