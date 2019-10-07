class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        first, last = 0, (len(nums) - 1)
        found = False

        while not found:
            if first <= last:
                middle = (first + last) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    first = middle + 1
                else:
                    last = middle - 1
            else:
                if target < last:
                    return last
                else:
                    found = True
                    return first


nums = [1, 3, 5, 7, 9]
print(Solution().searchInsert(nums, 2))
