class Solution:
    def permute(self, nums):
        
        if not nums:
            return[]
        
        nums.sort()
        res = []
        
        self.dfs(res, nums, [])
        return res
    
    def dfs(self, res, nums, temp):
        
        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.dfs(res, nums, temp)
            temp.pop()

print(Solution().permute([1, 2, 3]))