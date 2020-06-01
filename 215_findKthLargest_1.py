# 方法一: 先排序然后找第n个.
# Time: O()
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]
