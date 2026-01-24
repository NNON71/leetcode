class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxSum = 0
        n = len(nums)
        for i in range(n // 2):
            maxSum = max(maxSum, nums[i] + nums[n - i - 1])
        return maxSum