class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums) - 1):
            p1 = nums[:i + 1]
            p2 = nums[i + 1:]
            _sum = (sum(p1) - sum(p2)) % 2
            if not _sum :
                ans += 1
        return ans
            