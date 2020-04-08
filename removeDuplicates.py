class Solution:
    def removeDuplicates(self, nums) -> int:
        
        if not nums or len(nums) <= 2: return len(nums)
        
        slow = 2
        for fast in range(2, len(nums)):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
                
        return slow


if __name__ == "__main__":
    l = [1, 1, 1, 2, 2, 3]
    r = Solution().removeDuplicates(l)
    assert l == [1, 1, 2, 2, 3, 3]
    assert r == 5