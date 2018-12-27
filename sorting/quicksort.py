from random import randrange, shuffle
"""
Quicksort partitions the array into two smaller. 

We use a pivot we can do this by selecting the first element as the pivot. 

We will have a lesser than sub array  and a greater than sub array.  

we proceed by checking the first element comparing to the next and placing the items in the appropriate array. Based off less than or greater than. 

We will then have two sub arrays of less than or greater than values and we will repeat these subarray steps until there is one or zero elements in each
sub array. 

Quicksort is considered a comparison sort and uses the divide and conquer strategy breaking the problem into smaller sub problems. 

We choose a single pivot element from the list. Every other element is compared with the pivot, which partitions the array into three groups.

A sub-array of elements smaller than the pivot.
The pivot itself.
A sub-array of elements greater than the pivot.

19,22,7,14,3,9,12 32 25

the piviot from the above list would be 19.  We then iterate through the entire list 
less than = [] 
greater than = [] 

so after the first iteration through we will have the following 
1. less than = 7, 14 3 9 12  
2. pivot 19
3. greater than = 22 32 25

Notice that the less than and greater than are not sorted however  we will continue the pivoting until the list has 1 or zero elements.   

for example  greater than will start over and look like this 
1.less than = [] <--- empty list 
2. pivot 22 
3. greater than 32  25 

We will go again  
1. less than = 25 
2.pivot = 32 
3. greater than = [] <--- empty   

As the returns work back recursively  the greater than section from the first sub array gets to be  22 25 32.   The process will (and likely have already started)
with the original less than stack orginally created through the first iteration. 

Notice that the problem gets cut into halfs  with each step. 

Worse case runtime is O(N^2)   average case O(N * logN)
Very uncommon to have the worse case so quick sort is typically considered to be a O(N * logN) solution. 

With choosing the pivot it is very popular to make a random selection instead of just choosing the first element.  
You can also take the first middle and last elements and choose the median as the pivot.  The benefit is that the division of the array tends to be more uniform. 

For quicksort to achieve the average case runtime of O(n*logn)   the partition step must divide the array into halves of roughly equal length. 
This will reduce the number of recursive calls. 

Because this is a recursive  algorithm   what would be the base case  when the algorithm stops recursing?   When the array passed in is no longer than one element. 
We need it to be  1 or 0...

If the first element is always chosen we would experience worse case if we  are attempting to sort a a sorted data set.  1 2 3 4 5 6 7 8   if we choose 1
as pivot   we would virtually go through more recursive calls because  greater than would feature n-1 elements each time. 
Ideally we want the partition to divide the problem in half. One reason why many programmers will randomly select a pivot element in quicksort. 

Quicksort is a comparison sort.

Our algorithm will be recursive, so we'll have a base case and an inductive step that takes us closer to the base case.
We'll also sort our list in-place to keep it as efficient as possible.

Sorting in place means we'll need to keep track of the sub-lists in our algorithm using pointers and swap values inside the list rather than create new lists. 
We'll use pointers a lot in this algorithm so it's worth spending a little time practicing. Pointers are indices that keep track of a portion of a list. Here's an example of using pointers to represent the entire list:

my_list = ['jonathan', 'jason', 'brandon', 'zack', 'mitchell']
start_of_list = 0
end_of_list = len(my_list) - 1

my_list[start_of_list : end_of_list + 1]
# ['jonathan', 'jason', 'brandon', 'zack', 'mitchell']

Let's cut it in half 
end_of_half_sub_list = len(my_list) // 2

my_list[start_of_list : end_of_half_sub_list + 1]

Since there is 5 elements we will get 2.5 which because we used floor division we will have an index of 2. So we have  start of the list equal 
0  and end of half sub list = 2  we want to include the index so we add 1 to it.  this means [0:3]  which gives us 0 1 2   the first three elements
['jonathan', 'jason', 'brandon']

start_of_list  and  end_of_half_sub_list  are pointers.   We are pointing to specific place in the list. 

imported randrange from random for the random pivot selection. 
https://docs.python.org/3/library/random.html#random.randrange  for information on how to use this function. 
"""

#define quicksort function with list start end as parmaters 
def quicksort(lst, start, end):
    """Quicksort algorithm which has a run time of O(N * logN)"""
    #Create a base case. 
    """
    we are going to pass the same list recursively but the start and end will mark the parts of the list we are considering.
    when start to end contains one or zero elements we will return form the function.  this means start would equal end or start will be greater than end. 
    For example  if  start is 2 and end is 2    and we attempt to grab something from the array array [start:]   we will get one element. 

    something = ["test", "nothing"]  try it   something[0:0]  will produce an empty list and something [2:1]  will produce an empty list. 
    """
    if start >= end:#base case. 
        return 
    # define pivot variables
    pivot_idx = randrange(start, end)
    """
    Remember choosing a random pivot will decrease the likelihood of the worse case. There will be times where the algorithm has to perform and,
    you being human won't be able to check if the list is sorted as the algorithm runs behind the scenes of your application. This is very effective,
    in preventing our algorithm against inefficient runtimes. 
    """
    pivot_element = lst[pivot_idx]

    #Swap the elements in the list. end swapped with idx
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end] #parallel assignment swap. 
    """
    Now to carry this algorithm to other languages performing a swap would likely force you to create a temp variable for other languages. 
    This line of code above is unique to Python and maybe a couple other languages. What happens is the left side is set with the right side. 
    However it remembers the initial values before setting it avoiding the need for a temp variable. 
    """ 
    #partitioning 
    """
    pseduo code.    
    start a for loop use idx as the variable 
    for idx in lst 
    check if the value at idx is less than pivot 
    if true  swap lesser pointer and idx values 
    increment lesser pointer 

    after loop is finished 
    swap pivot with value at lesser than pointer 
    """
    #Remember we are not going to create new lists. We will being doing this in place and using pointers. 
    #one pointer will keep track of the lesser than elements.  The other pointer keeps track of progress through the list. 
    """
    [5, 6, 2, 3, 1, 4]
    # we randomly select "3" and swap with the last element
    [5, 6, 2, 4, 1, 3]

    # We'll use () to mark our "lesser than" pointer
    # We'll use {} to mark our progress through the list

    [{(5)}, 6, 2, 4, 1, 3]
    # {5} is not less than 3, so the "lesser than" pointer doesn't move

    [(5), {6}, 2, 4, 1, 3]
    # {6} is not less than 3, so the "lesser than" pointer doesn't move

    [(5), 6, {2}, 4, 1, 3]
    # {2} is less than 3, so we SWAP the values...
    [(2), 6, {5}, 4, 1, 3]
    # Then we increment the "lesser than" pointer
    [2, (6), {5}, 4, 1, 3]

    [2, (6), 5, {4}, 1, 3]
    # {4} is not less than 3, so the "lesser than" pointer doesn't move

    [2, (6), 5, 4, {1}, 3]
    # {1} is less than 3, so we SWAP the values...
    [2, (1), 5, 4, {6}, 3]
    # Then we increment the "lesser than" pointer
    [2, 1, (5), 4, {6}, 3]
    """
    #create varaiable for the lesser than pointer assign it to the start of the list. 
    lesser_than_pointer = start
    #create a for loop that iterates from start to end.
    #Note our other pointer will be used as the variable in range of our list. 
    for idx in range(start, end):
        #check if the element at idx is less than the pivot_element. 
        if lst[idx] < pivot_element:
            #we will again use parallel assignment to swap the values at lesser than pointer and idx 
            #after increment lesser than pointer. 
            lst[lesser_than_pointer], lst[idx] = lst[idx], lst[lesser_than_pointer] #parallel assignment
            lesser_than_pointer += 1
    #end of the for loop. 

    #swap pivot element with the value located at lesser than pointer and element at end. 
    lst[end], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[end]

    #After the first iteration 
    """
    # the pivot, 3, is correctly placed
    whole_list = [2, 1, (3), 4, 6, 5]

    less_than_pointer = 2
    start = 0
    end = len(whole_list) - 1
    # start and end are pointers encompassing the entire list
    # pointers for the "lesser than" sub-list
    left_sub_list_start = start
    left_sub_list_end = less_than_pointer - 1

    lesser_than_sub_list = whole_list[left_sub_list_start : left_sub_list_end]
    # [2, 1]

    # pointers for the "greater than" sub-list
    right_sub_list_start = less_than_pointer + 1
    right_sub_list_end = end
    greater_than_sub_list = whole_list[right_sub_list_start : right_sub_list_end]
    # [4, 6, 5]

    Now with this  if you notice the less than pointer  everything to the left of index 2 is the less than list or sublist.  
    Everything to the right or greater than the less than pointer is the greater than sub list. Remember 3 was our orginal random pivot. 

    The left sublists is marked from start to less_than_pointer -1 
    The right sub list is marked from less than pointer + 1 to end 

    Less than pointer marks the location of the pivot element and we've just swapped it into the correct location (at the end of the for loop). 
    We want to sort the sub-lists to the left (-1)   and right (+1) of that pivot. 
    """

    #call quicksort on the left and right sub lists. 
    #inductive step to take us closer to the base case. 
    quicksort(lst, start, lesser_than_pointer - 1)
    quicksort(lst, lesser_than_pointer + 1, end)

    #notice we didn't have to concatenate or return anything the reason being our base case stops once we reach 1 or zero elements. 
    # also because we are using pointers we will adjust the orginal lists.  
    #This method also gives us a space complexity of O(N)  there are many other ways to implement quick sort. 
    #We will use more memory if we create new lists instead of using pointers. 








# end of quicksort 
unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!
quicksort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)

