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
        
        ans = []
        for i in range(len(nums)):
            val = nums[i]
            m = len(ans)
            for j in range(val):
                if j | j + 1 == val:
                    ans.append(j)
                    break
            n = len(ans)
            if n == m:
                ans.append(-1)
        return ans