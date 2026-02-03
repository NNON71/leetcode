class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0
        # strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False

        # strictly decreasing
        j = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if j == i:
            return False
        
        # strictly increasing
        j = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if j == i or i < n - 1:
            return False
    
        return True

        # Sol1
        # prev, curr = 0, 1
        # p, q = 0, 0
        # while curr < n:
        #     if nums[prev] < nums[curr]:
        #         if q != 0:
        #             break
        #         p = curr
        #     elif nums[prev] > nums[curr]:
        #         q = curr
        #     else:
        #         return False
        #     prev = curr
        #     curr += 1
        #     print(p, q)
        # for i in range(q, n - 1):
        #     if nums[i] >= nums[i + 1]:
        #         return False
        # if p < q and p > 0 and q < n - 1:
        #     return True
        # return False


