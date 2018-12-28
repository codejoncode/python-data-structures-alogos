"""
Linear Search algorithm searching for the max value in the list. 
Will go through the entire list.  O(N) best worse and aveage. 

pseduo code 

# Create a variable called max_value_index    
# Set max_value_index to the index of the first element of the search list
     # For each element in the search list
          # if element is greater than the element at max_value_index
               # Set max_value_index equal to the index of the element
# return max_value_index


"""
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    print(search_list[idx])
    if maximum_score_index is None or search_list[idx] > search_list[maximum_score_index]:
    	maximum_score_index = idx
 
  return maximum_score_index


test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)