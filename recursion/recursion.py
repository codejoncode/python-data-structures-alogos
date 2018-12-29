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

    return result, call_stack
