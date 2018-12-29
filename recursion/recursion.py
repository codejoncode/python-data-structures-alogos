"""
Recursion involves a base case which will end the function and  a step that gets us closer to the base case.

Sometimes more than one base case is needed and likewise more than one step is needed at times to reach a base case.

Recursion means a function definition will include an invocation of the function within its own body.  Pseduo code example

define function, speller
  (if there are no more letters
    print all done )base case
  print the first letter
  (invoke speller with the given name minus the first letter.) gets us closer to the base case.

Iterative appraoch of the same problem
define function, speller
   for each letter in the name argument
     print the letter
   print "all done"

Call stacks and Execution frames
Stacks, a data structure, follow a strict protocol for the order data enters and exits the structure:
 the last thing to enter is the first thing to leave.

Your programming language often manages the call stack, which exists outside of any specific function.
This call stack tracks the ordering of the different function invocations, so the last function to enter the call stack
is the first function to exit the call stack

psedudo code function which sums the integers in an array:

Your programming language often manages the call stack, which exists outside of any specific function.
This call stack tracks the ordering of the different function invocations, so the last function to enter
the call stack is the first function to exit the call stack

This function will be invoked as many times as there are elements within the list!

Stepping through:

CALL STACK EMPTY
___________________

Our first function call...
sum_list([5, 6, 7])

CALL STACK CONTAINS
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________

Base case, a list of one element not met.
We invoke sum_list with the list of [6, 7]...

CALL STACK CONTAINS
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________

Base case, a list of one element not met.
We invoke sum_list with the list of [7]...

CALL STACK CONTAINS
___________________
sum_list([7])
with the execution context of a list being [7]
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________

We've reached our base case! List is one element.
We return that one element.
This return value does two things:

1) "pops" sum_list([7]) from CALL STACK.
2) provides a return value for sum_list([6, 7])

----------------
CALL STACK CONTAINS
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
RETURN VALUE = 7
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________

sum_list([6, 7]) waits for the return value of sum_list([7]), which it just received.

sum_list([6, 7]) has resolved and "popped" from the call stack...


----------------
CALL STACK contains
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
RETURN VALUE = 6 + 7
___________________

sum_list([5, 6, 7]) waits for the return value of sum_list([6, 7]), which it just received.
sum_list([5, 6, 7]) has resolved and "popped" from the call stack.


----------------
CALL STACK is empty
___________________
RETURN VALUE = (5 + 6 + 7) = 18


stack overflow will happen if the base case in not sufficient.  Without one it is similar to a infinite loop.

A call stack is a data structure typically abstracted away from us which stores function calls in programs.

What is the purpose of the base case in a recursive function?  In the base case there is no recursive function call.

What are the two main sections of a recursive function?
The base case and the recursive step.

Recursion is not typcially more efficient than iteration.    Recrusion has additional overahead of function frames on the call stack.

What is the importance of the recursive step?   It recursively calls the function with an argument which will reach the base case.

When analyzing the Big O runtime of recursive functions we count the relation of input to function calls.
"""


def sum_to_one(n):
    """
    given a number as input sums every number from 1 to the given input.
    simulates a recursive solution using call stack and execution context.
    """
    result = 1
    call_stack = []
    while n > 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")

    """
    After the values are added to the call stack. Once the base case is reached   the excution contexts stored are popped off the call stack.
    """
    while call_stack:
        return_value = call_stack.pop()
        print(return_value)
        print("Adding {0} to result of {1}".format(
            return_value["n_value"], result))
        result += return_value["n_value"]

    return result, call_stack


def sumToOne(n):
    """
    Given a number as input sums every number from 1 to the given input.
    Uses recursion.
    No call stack or execution context variables because this is already done under the hood.
    """
    # start by creating base case
    if n == 1:
        return n
    # recursive step.
    else:
        print("Recursing with input: {0}".format(n))
        return n + sumToOne(n-1)

# end of funciton


print(sumToOne(7))


def factorial(n):
    """
    returns the product of every integer from 1 up to the input.
    If the input is less than 2 return 1 = base case.
    A stack overflow will be produced with really large numbers as input.
    Recursion has costs that iteration doesn't.   Every recursive call spends time on the call stack.
    eventually there is no room left.

    Recursion reduces the lines of code needed.   The Zen of Python states beautiful is better than ugly.
    """
    if n < 2:  # base case
        return 1
    else:
        return n * factorial(n-1)

# end of function


print(factorial(12))


"""
The next function will implement  a power set.   A power set is a list of all subsets of the values in a list.

[a, b, c]

a b c
a b
a c
a
b c
b
c

producing subsets requires a runtime of at least O(2 ^ N) we won't ever do better than that because a set of N elements creates a power set of 2 ^ N elements.

Binary, a number system of base 2, can represent 2^N numbers for N binary digits.

# 1 binary digit, 2 numbers
# 0 in binary
0
# 1 in binary
1

# 2 binary digits, 4 numbers
# 00 => 0
# 01 => 1
# 10 => 2
# 11 => 3

The iterative approach uses this insight for a very clever solution by including an element in the subset if its "binary digit" is 1.

set = ['a', 'b', 'c']
binary_number = "101"
# produces the subset ['a', 'c']
# 'b' is left out because its binary digit is 0
That process is repeated for all O(2^N) numbers!

"""


def power_set_iterative(set):
    """
    produces power sets  A power set is a list of all subsets of the values in a list.

    """
    power_set_size = 2**len(set)
    result = []

    for bit in range(0, power_set_size):
        sub_set = []
        for binary_digit in range(0, len(set)):
            if((bit & (1 << binary_digit)) > 0):
                sub_set.append(set[binary_digit])
        result.append(sub_set)
    return result


def power_set(my_list):
    """
    produces power sets  A power set is a list of all subsets of the values in a list.
    base case will be once the list is empty.
    """
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first
# end of function


universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for sub_set in power_set_of_universities:
    print(sub_set)
# end of for loop.


def flatten(my_list):
    """
    Uses recursion to flatten an array.
    """
    result = []
    for lst in my_list:
        # conditional recursive step. Check if lst is a list.
        if isinstance(lst, list):
            print("List found!")
            flat_list = flatten(lst)
            result += flat_list
        else:
            result.append(lst)
    return result
# end of function.


planets = ['mercury', 'venus', ['earth'], 'mars', [
    ['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))


def fibonacci(n):
    """
    Using recursion on multiple
    Fibonacci numbers are the sum of the previous two fibonacci numbers.
    The base case will be  if  we receive 0 and 1   since this is the first two fibonacci numbers.
    fibonacci(3) == fibonacci(1) + fibonacci(2)
    runtime  O(2^N)
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    # recursive step
    return fibonacci(n-1) + fibonacci(n-2)

# end of function


fibonacci(5)


def sum_digits(n):
    """
    recursive function to sum the individual digits of a number.
    # base case: if input <= 9
    # return input
    # recursive step
    # last_digit set to input % 10
    # return recursive call with (input // 10) added to last_digit
    """
    if n < 10:
        return n
    else:
        last_digit = n % 10
        # What argument is every digit except the last?
        return last_digit + sum_digits(n // 10)


# end of function
sum_digits(12)
# 3
sum_digits(194)
# 14

# Linear - O(N)


def sum_digits_iterative(n):
    """
    sum of digits iterative approach. 
    """
    if n < 0:
        ValueError("Inputs 0 or greater only!")
    result = 0
    while n is not 0:
        result += n % 10
        n = n // 10
    return result + n


sum_digits_iterative(12)
# 1 + 2
# 3
sum_digits_iterative(552)
# 5 + 5 + 2
# 12
sum_digits_iterative(123456789)
"""
Data structures can also be recursive.
Trees are a recursive data structure because their definition is self-referential. A tree is a data structure which contains a piece of data and references
to other trees.  A tree can be both parent and child. We're going to write a recursive function that builds a special type of tree: binary search tree:

Binary search trees:
Reference two children at most per node.
the left search child of the tree must contain a value lesser than its parent.
the right child of the tree must contain a value greater than its parent.

Trees are an abstract data type.

bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}

bst_tree_node["data"] > bst_tree_node["left_child"]["data"]
# True
bst_tree_node["data"] < bst_tree_node["right_child"["data"]
# True


Our high-level strategy before moving through the checkpoints.

base case: the input list is empty
Return "No Child" to represent the lack of node
recursive step: the input list must be divided into two halves
Find the middle index of the list
Store the value located at the middle index
Make a tree node with a "data" key set to the value
Assign tree node's "left child" to a recursive call using the left half of the list
Assign tree node's "right child" to a recursive call using the right half of the list
Return the tree node
"""


def build_bst(my_list):
    """
    Using recursion on binary tree data structure.
    """
    if not my_list:  # base case
        return "No Child"

    # declare middle index of the my_list
    middle_index = len(my_list) // 2
    # declare the middle idx value
    middle_value = my_list[middle_index]
    print("Middle index: {0}".format(middle_index))
    print("Middle value: {0}".format(middle_value))

    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[: middle_index])
    tree_node["right_child"] = build_bst(my_list[middle_index + 1:])

    return tree_node


# end of function

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)


def factorial_iterative(n):
    """
    when supplied a integer find the factorial using a iterative approach
    # initialize a result variable set to 1
    # loop while the input does not equal 0
    # reassign result to be result * input
    # decrement input by 1
    # return result
    """
    result = 1
    while n != 0:
        result *= n
        n -= 1
    # end while loop
    return result
# end of function


# test cases
print(factorial_iterative(3) == 6)
print(factorial_iterative(0) == 1)
print(factorial_iterative(5) == 120)


def fibonacci_iterative(n):
    """
    when supplied an integer find the fibonacci using a iterative approach.
    # define a fibs list of [0, 1]
    # if the input is <= to len() of fibs - 1
    # return value at index of input
    # else:
    # while input is > len() of fibs - 1
    # next_fib will be fibs[-1] + fibs[-2]
    # append next_fib to fibs
    # return value at index of input
    """
    fibs_list = [0, 1]
    if n <= len(fibs_list) - 1:
        return fibs_list[n]
    else:
        while n > len(fibs_list):
            next_fib = fibs_list[-1] + fibs_list[-2]
            print(next_fib)
            fibs_list.append(next_fib)
        # end of while loop
    next_fib = fibs_list[-1] + fibs_list[-2]
    fibs_list.append(next_fib)
    return fibs_list[n]


# end of function
# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)


def find_min_iterative(my_list):
    """findthe minimum of the list. using iterative approach
    """
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min


find_min_iterative([42, 17, 2, -1, 67])
find_min_iterative([])
find_min_iterative([13, 72, 19, 5, 86])


def find_min(my_list, min=None):
    """Find the minimum of the list using iterative approach
    # function definition with two inputs: 
    # a list and a min that defaults to None
    # BASE CASE
    # if input is an empty list
    # return min
    # else
    # RECURSIVE STEP
    # if min is None
    # OR
    # first element of list is < min
    # set min to be first element
    # return recursive call with list[1:] and the min
    """
    if not my_list:
        return min
    else:
        if min is None or my_list[0] < min:
            min = my_list[0]
        return find_min(my_list[1:], min)


# end of function
# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)


# Linear - O(N)
# def palindrome(my_string):
#     """
#     Iterative approach to check whether a given string is a palindrome:
#     """
#     string_length = len(my_string)
#     middle_index = string_length // 2
#     for index in range(0, middle_index):
#         opposite_character_index = string_length - index
#         if my_string[index] != my_string[opposite_character_index]:
#             return False
#     #end of for loop.
#     return
# #end of function.
# print(palindrome("abba") == True)
# print(palindrome("abcba") == True)
# print(palindrome("") == True)
# print(palindrome("abcd") == False)

def is_palindrome(my_str):
    """
    recursive approach to check whether a given string is a palindrome: 
    A palindrome is a word that reads the same forward and backward. 
    # BASE CASE
    # the input string is less than 2 characters
    # return True
    # RECURSIVE STEP
    # str[0] does not match str[-1]
    # return False
    # return recursive call with str[1:-1]
    """
    if len(my_str) < 2:
        return True
    if my_str[0] != my_str[-1]:
        return False
    return is_palindrome(my_str[1:-1])


print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)


def multiply(num_1, num_2):
    """
    pretending Python does not come with a * multiply symbol.   using iterative approach 
    """
    result = 0
    # for count in range(0, num_2):
    #     result += num_1
    # return result
    iterations = 0
    if num_1 < num_2:
        for count in range(0, num_1):
            result += num_2
            iterations += 1
        return result, iterations
    else:
        for count in range(0, num_2):
            result += num_1
            iterations += 1
        return result, iterations
    """
    the second version is more work but will allow us to iterate faster.  this is virtually a O(N) solution however  N can mean the lesser between the two inputs. 
    Instead of just going with one and going the max at times the extra lines insures we only go the minimum lines of code and either way gets the same answer.
    For example 0 * 10000  no reason to go 10000 times when the first tells us exactly what the answer will be.   Or even  2 *  12 million.   why travel 12 million times by 2?
    Extra lines is not a bad thing.   
    """


# end of function
print(multiply(3, 7))
# 21
print(multiply(5, 5))
# 25
print(multiply(0, 4))
#


def multiplication(num_1, num_2):
    """
    pretend that python does not have a a mulplication operator use a recursive method. 
    # BASE CASE
    # if either input is 0, return 0
    # RECURSIVE STEP
    # return one input added to a recursive call with the OTHER input decremented by 1
    """
    iterations = 0
    if num_1 == 0 or num_2 == 0:
        return 0
    else:
        iterations += 1
        if num_1 < num_2:
            return num_2 + multiplication(num_2, num_1-1)
        else:
            return num_1 + multiplication(num_1, num_2-1)


# end of function
# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)


"""
How deep is your tree? 

Binary trees, trees which have at most two children per node, are a useful data structure for organizing hierarchical(arranged in order of rank) data. 

# first level
root_of_tree = {"data": 42}
# adding a child - second level
root_of_tree["left_child"] = {"data": 34}
root_of_tree["right_child"] = {"data": 56}
# adding a child to a child - third level
first_child = root_of_tree["left_child"]
first_child["left_child"] = {"data": 27}
"""


def depth_iterative(tree):
    """
    Iterative approach to finding the depth of a tree.  Utilizing a queue type data structure which is just a python list but following the rules of queues. 
    """
    result = 0
    # our "queue" will store nodes at each level
    queue = [tree]
    # loop as long as there are nodes to explore
    while queue:
        # count the number of child nodes
        level_count = len(queue)
        for child_count in range(0, level_count):
            # loop through each child
            child = queue.pop(0)
           # add its children if they exist
            if child["left_child"]:
                queue.append(child["left_child"])
            if child["right_child"]:
                queue.append(child["right_child"])
        # count the level
        result += 1
    return result


two_level_tree = {
    "data": 6,
    "left_child":
    {"data": 2}
}

four_level_tree = {
    "data": 54,
    "right_child":
    {"data": 93,
     "left_child":
     {"data": 63,
      "left_child":
      {"data": 59}
      }
     }
}
print(depth_iterative(two_level_tree))
print(depth_iterative(four_level_tree))

def depth(tree):
    """
    recursive implementation to get the depth of a binary tree. 
    # function takes "tree_node" as input
    # BASE CASE
    # if tree_node is None
        # return 0
    # RECURSIVE STEP
    # set left_depth to recursive call passing tree_node's left child
    # set right_depth to recursive call passing tree_node's right child

    # if left_depth is greater than right depth:
        # return left_depth + 1
    # else
        # return right_depth + 1
    """
    if tree is None:
        return 0
    left_depth = depth(tree["left_child"])
    right_depth = depth(tree["right_child"])

    if left_depth > right_depth:
        return left_depth + 1
    else: 
        return right_depth + 1


# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)