class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        subfix = [0] * n
        subfix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            subfix[i] = subfix[i + 1] * nums[i]
    
        res[0] = subfix[1]
        res[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            res[i] = subfix[i + 1] * prefix[i - 1]
        return res


    def productExceptSelf2(self, nums):
        n = len(nums)
        res = [0] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        subfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= subfix
            subfix *= nums[i]
    
        return res