"""
Implementing the radix sort algorithm. 

Our number system is based off a radix of 10. 0-9.
Our system is called base 10. 

The concecpt is based of   123   and 3   here  3 represents a value of 3 in each.  

for  347 and 223590     3 has a value of 300 and a value of 3000.  

Two different kinds of radix sorts.   
Most significant digit or MSD  
least significant or LSD

Both radix sorts organize the input list into ten "buckets", one for each digit.
 The numbers are placed into the buckets based on the MSD (left-most digit) or LSD (right-most digit). 
 For example, the number 2367 would be placed into the bucket "2" for MSD and into "7" for LSD.

This bucketing process is repeated over and over again until all digits in the longest number have been considered.
 The order within buckets for each iteration is preserved. For example, the numbers 23, 25 and 126 are placed in the "3", "5",
  and "6" buckets for an initial LSD bucketing. On the second iteration of the algorithm, they are all placed into the "2" bucket,
   but the order is preserved as 23, 25, 126.

Raidx sort sorts a list of integers witout performing any comparisions. non-comparision sort. 

For each iteration of the algorithm we are deciding which bucket to place each of the n entries into. 

iteration continues until we examine each digit. This means we need to iterate for how ever many digits we have.   We call this average number of digits
the word size of w. 

Teh complexity of radix sort is O(wn)    w can be a constant because the length of the list is much larger than the number of digits most likely. 
Making radix sort a O(n) run time complexity. 

A radix is the base of a number system. For the decimal number system, the radix is 10. Radix sort has two variants - MSD and LSD   

Numbers are bucketed based on the value of digits moving left to right (for MSD) or right to left (for LSD)
Radix sort is consisdered a non comparision sort 
The performance of radix sort is O(n)

When performing an MSD radix sort  the following numbers from this list [22, 23, 32, 42, 25, 77] would be bucketed into the "2" bucket for the first step.

[22,23,25]

22, 32, 42 would be the case for a LSD. 

What is a radix? is the base of a number system. 

We will need to erase and rewrite the output list a number of times. For this sort it would be bad practice to mutate the input list. in case something goes
wrong with our code or someone using our sort decides they don't want to wait anymore. 
"""

def radix_sort(to_be_sorted):
    """
    Implementation or radix sort a non comparision sorting algorithm with run time of O(n). 
    """
    
    #decalre a new variable to get the max of to be sorted 
    maximum_value = max(to_be_sorted) #allows us to determine how many digits are in the longest number in the list. 

    #define max_exponent 
    """
    cast maximum value to a string 
    take the length of that string 
    assign that length to the varaible max_exponenet 
    return max_exponent 
    """
    max_exponent = len(str(maximum_value))

    #create a copy of to_be_sorted 
    being_sorted = to_be_sorted[:]
    #Other methods 
    # list(to_be_sorted)
    # to_be_sorted.copy()
    #could import copy and copy.copy(to_be_sorted)
    #could import copy copy.deepcopy(to_be_sorted)  <----   if the list contains objects and you want to copy them as well.

    #create a for loop to iterate over the range over max_exponent
    for exponent in range(max_exponent):

        #create variable to keep track of what exponent we are looking at. exponent is zero indexed so this varaible should always be 1 greater than exponent
        position = exponent + 1
        #create a varaible that will be the negative version of position 
        index = -position
        # go through each position of each number and put all of the inputs in different buckets depending on the value
        #0 - 9 
        digits = [[] for digit in range(10)]

        """
        LSD radix sort algorithm will take each number in the input list from left to right and incrementally appends each number into the bucket corresponding
        to the value of that digit.  
        """
        #iterate over being_sorted grab each value being_sorted and save it as a temporary variable. 
        for number in being_sorted:
            #convert number to a string and save that to a variable 
            number_as_a_string = str(number)
            #access the index of the number_as a string. 
            #We have to be prepared for some numbers to be shorter than other numbers. 
            try: 
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            #what we did is tried to access the digit using index if we can't we will get a IndexError so we have an exception in place that sets digit to 0
            """
            Couple of note worthy mentions,   If we get an IndexError it is because the value for number at index is actually 0. 
            We could also except without a specific error.  However this leaves room for error  
            try: 
                digit = number_as_a_string[index]
            except:
                digit = 0 

            would work however what if we get an error that is not a IndexError?   we wouldn't know it.   We are prepared to except only one error. 
            If we get an IndexError we know why so we can set digit to the appropriate value. Any other error and we wouldn't know why.  Since a IndexError
            would stop our code from running and we can expect it to happen we prepare for it. 

            Zen of Ptyon  Errors should never pass silently Unless explicitly silenced. 
            Have except IndexError is an explicity pass that we won't even see happen.   Using except could allow for a error to pass silently but again, 
            it would allow for any type of error to pass outside of IndexError. 
            """

            #Now we need to return digit to a integer so we can use it to index. 
            digit = int(digit) 
            """
            It might seem weird but consider  12909 we cannot access the last digit if its an integer which is the reason we cast it as a string first.
            """
            #Now we append the number to the list index of digits 
            digits[digit].append(number)
        #end of for loop

        #reassign being sorted 
        being_sorted = []
        #create a loop to add the items from digits back to being_sorted
        for numeral in digits:
            being_sorted.extend(numeral)
            #The line above will add each element in the list numeral to the list being_sorted
        #end of for loop
        return being_sorted

# end of function 

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(radix_sort(unsorted_list))
# [830, 40, 921, 961, 641, 621, 1, 182, 163, 373, 183, 524, 535, 355, 559, 89, 199, 959, 689]
# ^ output   notice the 0 in the least signficant position all the way to 9 of course not all the numbers are there from 0-9 but they are sorted. 
second = [26,52,34,62,33]
radix_sort(second)



"""
To recap we this algorithm 
takes numbers in a list as input. 
passes through each digit from least to most significant. 
looks at the values of the digits 
Buckets the input list according to those digits
renders the results from that bucketing. 
repeats the process until the list is sorted. 
"""


"""
N is the length of the input list and w is the lement in the input list with the most digits.  Which lines are responsible for that runtime? 
def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]
    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = int(item_as_a_string[index])
      except IndexError:
        digit_for_item = 0

      digits[digit_for_item].append(item)
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted

N comes from the line for item in being_sorted: 
W comes from for pass_through in range(max_exponent)

for item in being_sorted iterates for each element in the input and line 

for pass_through in range(max_exponent) we are iterating for the max number of digits within the input. 

What is the code doing inbetween the commented sections ? 

def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]
		# BEGIN COMMENT #######
    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = int(item_as_a_string[index])
      except IndexError:
        digit_for_item = 0

      digits[digit_for_item].append(item)
		# END COMMENT ##########
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted

We are selecting the digit at the current iteration index and placing it in the correct bucket. 


Fill in the missing line of code. 

def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]
    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = int(item_as_a_string[index])
      except IndexError:
        digit_for_item = 0

      ????????????
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted

digits[digit_for_item].append(item)

Fill in the missing portion of code 

def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]

    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = int(item_as_a_string[index])
      except ???????:
        digit_for_item = 0

      digits[digit_for_item].append(item)
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted

IndexError   

We will have an IndexError if the numbers contained in the input list have varied numbers of digits. 

Given the following implementation of radix_sort(), what will the being_sorted list reference after one iteration with the input [26, 52, 34, 62, 33]?

def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]
    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = int(item_as_a_string[index])
      except IndexError:
        digit_for_item = 0

      digits[digit_for_item].append(item)
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted

Fill in the missing line of code!

def radix_sort(to_be_sorted):
  max_exponent = len(str(max(to_be_sorted)))
  being_sorted = to_be_sorted[:]

  for pass_through in range(max_exponent):
    exponent = pass_through + 1
    index = -exponent
    digits = [[] for digit in range(10)]

    for item in being_sorted:
      item_as_a_string = str(item)
      try:
        digit_for_item = ????????
      except IndexError:
        digit_for_item = 0

      digits[digit_for_item].append(item)
    being_sorted = []
    for digit in digits:
      being_sorted.extend(digit)

  return being_sorted
int(item_as_a_string[index])
"""


