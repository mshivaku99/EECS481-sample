""" 
Leetcode #1, easy, array, hash table; 1/24/2019
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9, because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matches = {} # key is element of nums, val is index
        for i in range(len(nums)): # range and len to track indices
            if target - nums[i] in matches: return [matches[target - nums[i]], i]
            # else match is not in dictionary
            matches[nums[i]] = i