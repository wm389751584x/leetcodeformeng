class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [1] * len(nums)
        if not nums: return False
        temp = nums[0]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return True if max(dp) >= 3 else False


if __name__ == "__main__":
    pass