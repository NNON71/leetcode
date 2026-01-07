class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in range(len(nums)) :
            if nums[i] in h :
                return nums[i]
            h[nums[i]] = True
            