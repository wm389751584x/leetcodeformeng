
class Solution:
    def fourSum(self, nums, target):

        N = len(nums)
        nums.sort()
        res = []

        if N < 4 or not nums:
            return []

        for i in range(N - 3):
            if i == 0 or nums[i] != nums[i-1]:

                for j in range(i + 1, N - 2):
                    if j == i+1 or nums[j] != nums[j-1]:

                        # two sum
                        l = j + 1
                        r = N - 1
                        new = target - nums[i] - nums[j]
                        while l < r:
                            if nums[l] + nums[r] < new:
                                l += 1
                            elif nums[l] + nums[r] > new:
                                r -= 1
                            else:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                while l < r and nums[l] == nums[l+1]:
                                    l += 1
                                while l < r and nums[r] == nums[r-1]:
                                    r -= 1
                                l += 1
                                r -= 1

        return res


nums = [0,0,0,0]
print(Solution().fourSum(nums, 0))
