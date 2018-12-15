"""
Bubble sort is a intro sorting algorithm that compares pairs of elements connected during iteration. 

Swapping will occur to shit the elements to the begining or end of list. 

Two loops will be used to sort the list.   The first loop goes until the list is sorted or as long as the list is not sorted. 
The assumption will be made from the start that the list is unsorted. The inner loop will perform our checks greater than or less than
it will also make our swap. It is seen in many algorithms where you may have a swap function separated from the actual bubble sort
function we will implement. 

Swapping the elements will work like this: 

temp = list[index_1]//make a copy.. 
list[index_1] = list[index_2]
list[index_2] = temp

O(n(n−1))=O(n(n))=  O(n^2) runtime. 


We are performing n-1 comparisons for our inner loop.
 Then, we must go through the list n times in order to ensure that each item in our list has been placed in its proper order.


An input list which is mostly ordered will require less swaps than an input list which is mostly unordered. 
Buble sort will only make a swap if an element is out of order. 


If no copy is made of the input list then bubble sort will alter the original array to produce the sorted data-set. 
list[index_1] = list[index_2]
list[index_2] = list[index_1]  

will not work   we must make a copy. 

Bubble sort is the not the most efficient of the comparison sorting algorithms. 

Bubble sort orders an input array thorugh a series of comparisons and swaps. 

Pseduod code   

for each pair (one, two ) : 
    if one > two: 
        swap(one, two)
    else 
        analyze next set of pairs 

"""

#Since the swap function is such a crtical part of the bubble start lets start with implementing that. 
def swap(arr, index_1, index_2):
    """This is function will swap the two index postions within the array. """
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

"""
If you would like to test out your swap function:   
nums = [5, 2, 9, 1, 5, 6]
swap(nums, 3, 5)
print(nums)

should produce :  [5, 2, 9, 6, 5, 1]

Testing out a function is always a smart move before moving forward. 
"""

"""
Once we can swap itmes we can create the bubble sort function that will perform the iteration of the list and comparison. 
Two loops will be present one that will go through each element of the list.   

The nested or inside loop will take the index of the loop and compare the element at that index with the element at the next index. 
If they are out of order swap. 
"""

#define bubble_sort() 
def bubble_sort(arr):
    """bubble sort algorithm uses swap function if the item is greater than  the next item in list. """
    for element in arr: 
        for index in range (len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swap(arr, index, index+1)
#

#Optimizing bubble sort 
"""
You may have realized that we are doing some unneccessary iterations 

nums = [5, 4, 3, 2, 1]
# 5 element list: N is 5
bubble_sort(nums)
# 5 > 4
# [4, 5, 3, 2, 1]
# 5 > 3
# [4, 3, 5, 2, 1]
# 5 > 2
# [4, 3, 2, 5, 1]
# 5 > 1
# [4, 3, 2, 1, 5]
# four comparisons total

As we sort fewer  elements have to be compared moving forward. It will be fewer than n^2 - n but still has  O(N^2) runtime because we drop the constant. 

"""

def bubble_sort_optimized(arr): 
    """Optimpized buble sort that doesn't iterate over items already placed does not use swap function"""
    iteration_count = 0 
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            #iterater through unplaced elements
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx] 
                #a little trick that allows us to not need a temp variable and get the swap accomplished in one line. 

# for idx in range (len(arr) - i - 1)  performs a micor optimization to reduce the number of overall iterations necessary to sort the input list 

"""
If my_nums = [7,3,4,2]  after one iteration of the bubble sort  it should look like this  [3,4,2,7]
After one iteration of the outer loop.  After a single pass the greatest value element would be moved to the end of the list. 
"""  