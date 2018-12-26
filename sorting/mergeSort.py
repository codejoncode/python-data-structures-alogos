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

# define a function called merge_sort()  Give it one paramater items


def merge_sort(items):
    """Merge sort will be used to break down items into smaller lists and then combined back together sorted"""
    # check that the length of items is one or less then return items if true
    if len(items) < 2:
        return items
    """How will we break up the data in a merge sort?  We split it in half until there is no more data to split.
    i.e. when len(items) is less than 2. After returning all inputs that have less than 2 elements. Split everything up 
    that's longer."""
    # create a variable that will serve as the middle index to the middle element in the list.
    middle_index = len(items)//2
    """Above here we use pythons floor division so not only are we just dividing the length of items by 2 but if the length is not even we round down"""
    # create a variable that will take the 0 index to the index just before the middle index.
    left_split = items[:middle_index]
    # create a variable that will take the middle index right to the last index.
    right_split = items[middle_index:]
    # create  two variables  left sorted and right sorted
    # left sorted will be merge_sort function on left_split and right sorted will be using right_split
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)
    # return the result of calling merge on left_sorted and right_sorted
    return merge(left_sorted, right_sorted)
# end of merge_sort


def merge(left, right):
    """define function merge  this will take care of merging out two lists together
left and right split. It takes two paramaters left and right.  
"""
    # instantiate a new empty list
    result = []
    """purpose is to add members of left and right to result until it has the
     sorted list will all elements. returning result at the end of the function"""

    """
    We need to build out our result list. When we're creating ordered lists 
    that combine the elements of the two lists. 
    """
    # create a while loop that continues while left and right have elements
    # when one of the lists are empty we move on.
    while left and right:
        # left and right are arrays
        """
        For sequences (strings, lists, tuples) if they are empty they are false
        If they have something in them they are true.  So you could use 
        something like while left and right:  However PEP 20 --
        The Zen of Python states Explicit is better than implicit. 
        len(left) > 0 and len(right) > 0 is slower. We can use while left and right
        then provide a comment that left and right are arrays for anyone that may not
        understand the purpose of the while loop and use the under the hood feature of
        python lists that provide false if the list are empty and true if it is not.
        """
        # Check if the first element of left is smaller than the first element of right.
        if left[0] < right[0]:
            # append left[0] to the result lists.
            result.append(left[0])
            # pop off the first index of left
            left.pop(0)
            """
            Without a argument pop usually removes the last. Providing the index
            removes where you want to remove. 
            Imagine the following 
            def pop (index = len(array) -1):
            So we virtually remove the last index by default.  If we change index
            by providing a parameter we then change what we remove. 
            """
        # if left[0] is greater than right[0]   append right 0 index and pop
        # Make sure this is a single conditional statement and not nested in the previous one.
        else:
            result.append(right[0])
            right.pop(0)
    # end of while loop
    # check if there are elements still in left if so add to result
    if left:
        result += left
    # check if there are elements still in right if so add to result
    if right:
        result += right
    """
    When it comes to lists in python you can concatenate with the + (plus) operator.
    [1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
    a = [1, 2, 3]
    a += [4, 5, 6]
    print(a)
    prints  [1, 2, 3, 4, 5, 6].
    Behind the scenes or under the hood a loop is likely involved but there 
    is no reason for us to reinvent the wheel. 
    """

    return result
# end of merge function


unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19,
                   202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
