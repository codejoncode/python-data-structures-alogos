"""
binarySearch.py is wasteful as at each recursive call we're copying N/2 elements where N is the length of the sorted list.

Pointers allow us to search without making copies of the list.

we will now pass in a left_pointer right_pointer  along with sorted_list and target.

base case that checks for a empy list will  will now check using the pointers to indicate a empty list

instead of doing sub copies of a list  it will now past updated pointers

the arithmetic for the right side is no longer neccessary
"""


def binary_search(sorted_list, left_pointer, right_pointer, target):
    """
    Binary search takes a sorted list  left pointer should start at 0 right pointer starts at the end of the list
    and a target.  O(log N) run time.
    """
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"
	
    # We calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))

