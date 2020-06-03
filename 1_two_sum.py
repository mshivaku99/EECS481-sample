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
