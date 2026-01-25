class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        _min = float("inf")
        for i in range(n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            _min = min(_min, diff)
        return _min
        
        # return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))
