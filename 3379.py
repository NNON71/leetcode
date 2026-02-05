class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] > 0:
                index = (i + nums[i]) % n
            elif nums[i] < 0:
                index = (i - abs(nums[i])) % n
            else:
                index = i
            res[i] = nums[index]
        return res
