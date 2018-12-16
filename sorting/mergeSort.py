"""
Created by John von Neumann in 1945 merge sort is a divide and conquer algorithm. It breaks the list to be sorted into smaller parts. 

Breaking down into smaller parts happens until sorting is very simple. Merge sort is one of the first to use this strategy. 

Why is it that separating a list into sublists makes sorting faster? 

Due to the sorting taking two steps  splitting all of the data into smaller componenets and then recombining the components into sorted 
lists. The second step is why this algorithm is called "merge" sort. 

We are required to split the list in half.   We will then recursively continue to split the list in half until there is only a single element left. 

Once we have only 1 element left we will begin merging. 

Before merging two single element lists we check if the first element is smaller or larger than the other.  Returning the two element list followed 
by the larger. 

How can we be sure that the leftover contents from two lists that we're merging are all larger than the result we've built so far?

When merging larger pre-sorted lists we build the list similarly to how we did with single-element lists.

Let's call the two lists left and right. Bothleft and right are already sorted. We want to combine them (to merge them) into a larger sorted list, let's call it both. To accomplish this we'll need to iterate through both with two indices, left_index and right_index.

At first left_index and right_index both point to the start of their respective lists. left_index points to the smallest element of left (its first element) and right_index points to the smallest element of right.

Compare the elements at left_index and right_index. The smaller of these two elements should be the first element of both because it's the smallest of both! It's the smallest of the two smallest values.

Let's say that smallest value was in left. We continue by incrementing left_index to point to the next-smallest value in left. 
Then we compare the 2nd smallest value in left against the smallest value of right. 
Whichever is smaller of these two is now the 2nd smallest value of both.

This process of "look at the two next-smallest elements of each list and add the smaller one to our resulting list" continues on for as long as both lists have elements to compare. 
Once one list is exhausted, say every element from left has been added to the result, then we know that all the elements of the other list, right, should go at the end of the resulting list (they're larger than every element we've added so far).

Why is it important that we only merge pre-sorted lists?
Merge sort was unique for its time in that the best, worst, and average time complexity are all the same: Θ(N*log(N)).
 This means an almost-sorted list will take the same amount of time as a completely out-of-order list.
 This is acceptable because the worst-case scenario, where a sort could stand to take the most time, is as fast as a sorting algorithm can be.

Some sorts attempt to improve upon the merge sort by first inspecting the input and looking for "runs" that are already pre-sorted. 
Timsort is one such algorithm that attempts to use pre-sorted data in a list to the sorting algorithm's advantage.
 If the data is already sorted, Timsort runs in Θ(N) time.

Merge sort also requires space. Each separation requires a temporary array, and so a merge sort would require enough space to save the whole of the input a second time.
This means the worst-case space complexity of merge sort is O(N).


In the merge sub-routine, how do we combine two sub-lists into a signle sorted list? 
By looping as long as both sub-lists have elements, comparing their first element and transferring the smaller element to a result list. 

What kind of algorithm is merge sort? 
Divide and conquer

What is always true of the sub-lists passed as arguments to merge? They are sorted. 

By using already sorted sub-lists, the merge sub-routine can combine them into a single sorted list in O(N) time. (tim sort)

What is the time complexity of merge sort ?    O(N * log(N))

What are the two steps to a merge sort? 
Split and merge

What is the base case for merge sort, when the function does not recurse? 
When merge sort is passed an empty or single element list as the argument. 

No comparisons are made in the merge sort function, only the merge sub-routine. 

Merge sort creates many copies of the original lists, there is no mutation. 


"""

