class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        while len(nums) > 1:
            if nums == sorted(nums):
                return c
            m = len(nums)
            _min = float("inf")
            _min_pos = None
            for i in range(m - 1):
                if _min > nums[i] + nums[i+1]:
                    _min = nums[i] + nums[i+1]
                    _min_pos = i
                # _min = min(_min, nums[i] + nums[i+1])
            nums = nums[:_min_pos] + [_min] + nums[_min_pos + 2:]
            c += 1
        return c