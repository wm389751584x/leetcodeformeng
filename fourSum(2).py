
class Solution:
    def fourSum(self, nums, target):

        N = len(nums)
        nums.sort()
        res = []

        if N <= 4:
            res.append(nums)
            return res

        for i in range(N - 3):
            if i == 0 or nums[i] != nums[i-1]:

                for j in range(i, N - 2):
                    if j == i or nums[j] != nums[j-1]:

                        # two sum
                        left = j + 1
                        right = N - 1
                        new = target - nums[i] - nums[j]
                        while left < right:
                            if nums[left] + nums[right] < new:
                                left += 1
                            elif nums[left] + nums[right] > new:
                                right -= 1
                            else:
                                res.append([nums[i], nums[j], nums[left], nums[right]])
                                while nums[left] == nums[left+1]:
                                    left += 1
                                while nums[right] == nums[right-1]:
                                    right -= 1
                                left += 1
                                right -= 1

            return res


nums = [1, 0, -1, 0, -2, 2]
print(Solution().fourSum(nums, 0))
