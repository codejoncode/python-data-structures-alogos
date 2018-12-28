"""
Using linear search to find duplicates instead of stopping on the first occurrence.

pseduo code 

# For each element in the searchList
    # if element equal target value then
        # Add its index to a list of occurrences
# if the list of occurrences is empty
   # raise ValueError
# otherwise
   # return the list occurrences
Because we are searching best case average case and worse case is O(N)  we have to go through the entire list to find all duplicates. 
"""

#Linear Search Algorithm
def linear_search(search_list, target_value):
  """
  linear search algorithm searching for duplicate values. Will iterate over the entire list. Needs a list and a target value to work properly.
  """
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
  	raise ValueError("{0} not in list".format(target_value))
#End of function 

tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"
#Function call
try:
    tour_stops = linear_search(tour_locations, target_city)
    print(tour_stops)
except ValueError as error_message:
    print("{0}".format(error_message))



