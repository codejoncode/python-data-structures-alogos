"""
This code was tested on leetcode   https://leetcode.com/problems/two-sum/
Submitted and was faster than 44.11% of all other submissions using Python 3 

The problem :  
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    obj = {} #used to work as memory so that we can keep track of the past as we move forward. 
    #the dictionary will hold memory of previously index's and values. 
    count = 0 # will keep track of the index. 
    returning = [] # will pass the indexs that equal up to the target to this. 

    #Step 1 iterate through the list 
    for x in nums:
      #step2 find out if  x is in the obj if it is we have a matching pair to the target.
      #if it is return the index in the obj and the count  
      if x in obj:
        returning.append(obj[x])
        returning.append(count)
        return returning
      """
      It is important to do the above first because given the array [3,2 1] and a target of 6. 
      You will add 3 to the array and then check if the pair 3 is in the obj and it will be. 
      We cannot not use the same element twice must go to another index. 
      """
      #step 3 take the number subtract it from the sum place this in a variable. 
      pair =  target - x


      #step4 find out if the variable created in step 2 is in the obj if not add it in. 
      if pair not in obj:
        obj[pair] = count
      
      #step5 increment the index. 
      count += 1 

result = twoSum([2,7,11,15], 9)
print(result)

result1 = twoSum([3,2,4], 6)
print(result1)