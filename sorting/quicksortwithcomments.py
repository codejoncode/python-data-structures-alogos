from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


    
  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)




"""
Explain the purpose of the highlighted portion of code  

def quicksort(list, start, end):
  if start >= end:
    return
 
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
 
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  less_than_pointer = start
  
  for i in range(start, end):
    if list[i] < pivot_element:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  
  #### EXPLAIN THE PURPOSE OF THE LINE BELOW #####
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  #### EXPLAIN THE PURPOSE OF THE LINE ABOVE #####

  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


This line moves the pivot_element into the correct placement within the list.  At this point, the list has been 
partitioned and everything with a lesser index than less_than_pointer has a value lower than pivot_element. 

What does an in place quicksort mean? Values are swapped within the original list, and no additional memory is used. 
More space efficient but they mutate the original list.  
This is not a tool for every sorting job sometimes you need the orginal list to remain the same and not be mutated. 
Possibly rare but a possibility. 

Select the missing portion of code. 

from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return
 
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  
 	# WHAT CODE GOES HERE?
  # ?????????????

  less_than_pointer = start
  
  for i in range(start, end):
    if list[i] < pivot_element:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1

  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


list[end], list[pivot_idx] = list[pivot_idx], list[end]
After randomly selecting the pivot we move it to the end of the list. 



explain the following base case 
 ### BASE CASE ####
  if start >= end:
    return
  ##################

Using pointers we're checking if the portion of the lists between start and end contains one or less elements. 

we have succeeded in sorting that portion of the list when we are at one or less elements. 


 ##### EXPLAIN LINES BELOW ########
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)

These lines recursively call quicksort on the lesser than and greater than sub lists created from the partition. 

for i in range(start, end):
    # WHAT OCCURS BELOW?
    if # ??????????:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1


if list[i] < pivot_element. Checking to see which elements in the list have a value lesser than our pivot so we can swap them 
to the left of the less than pointer. 


"""

#quick sort algorithm that is not in place 

def qs(arr):
  """
  more memory will be used using this method of quick sort but it will sort the array provided. 
  This implementation creates two new lists for each recursive call. The new lists are eventaully combined into a 
  new list with values in sorted order. 
  """
  if len(arr) <= 1:
    return arr

  smaller = []
  larger = []
  
  pivot = 0
  pivot_element = arr[pivot]
  
  for i in range(1, len(arr)):
    if arr[i] > pivot_element:
      larger.append(arr[i])
    else:
      smaller.append(arr[i])

  sorted_smaller = qs(smaller)
  sorted_larger = qs(larger)

  return sorted_smaller + [pivot_element] + sorted_larger