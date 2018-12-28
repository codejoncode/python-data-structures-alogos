import random


def bubble_sort(arr, comparison_function):
    """
    bubble sort best used on data that is nearly sorted.  This bubble sort implemenation accepts a list and a function as paramaters. 
    the function it uses will compare two elements and return true or false. 
    """
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr) - 1):
            #   if arr[idx] > arr[idx + 1]:
            if comparison_function(arr[idx], arr[idx + 1]):
                sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr
# end of bubble sort


def quicksort(arr, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    less_than_pointer = start
    for i in range(start, end):
        # if pivot_element > arr[i]:
        if comparison_function(pivot_element, arr[i]):
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
    quicksort(arr, start, less_than_pointer - 1, comparison_function)
    quicksort(arr, less_than_pointer + 1, end, comparison_function)
# end of quicksort
