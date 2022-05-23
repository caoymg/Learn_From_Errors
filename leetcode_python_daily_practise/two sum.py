"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        cnt_i = 0
        for i in nums:
            # note [where to initiate j]
            cnt_j = 0
            for j in nums:
                # note [order of i and j]
                if i + j == target and cnt_i != cnt_j and cnt_i > cnt_j:
                    output.append(cnt_i)
                    output.append(cnt_j)
                # note [where to update]
                cnt_j = cnt_j + 1
            cnt_i = cnt_i + 1     
        
        
        return output