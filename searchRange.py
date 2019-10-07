'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ln = len(nums)
        if ln == 0:
            return [-1, -1]
        
        left = right = -1
        low, high = 0, ln - 1
        
        # find left
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                left = mid
                high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        # find right
        low, high = 0, ln - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                right = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return [left, right]

nums = [1]
print(Solution().searchRange(nums, 1))