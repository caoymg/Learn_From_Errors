

# 😛🥳 Memory Usage: 13.5 MB, less than 93.63% of Python online submissions for Median of Two Sorted Arrays.

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        while len(nums) > 2:
            nums.remove(max(nums))
            nums.remove(min(nums))
        if len(nums) == 1:
            mid = nums[0]
        else:
            mid = (nums[0]+nums[1])/2.0
        
        return mid
            