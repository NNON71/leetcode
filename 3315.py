class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for n in nums:
        #     if n & 1 :
        #         res.append(n & ~(((n + 1) & ~n) >> 1))
        #     else:
        #         res.append(-1)
        # return res
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums