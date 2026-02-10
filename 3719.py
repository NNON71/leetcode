class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        _max = 0
        for i in range(n - 1):
            dist_even = set()
            dist_odd = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    dist_even.add(nums[j])
                else:
                    dist_odd.add(nums[j])

                if len(dist_even) == len(dist_odd):
                    _max = max(_max, len(nums[i:j + 1]))
        return _max
