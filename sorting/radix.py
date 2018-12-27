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
    


    return max_exponent



