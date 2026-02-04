class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp0 = [float('-inf')]*n
        dp1 = [float('-inf')]*n
        dp2 = [float('-inf')]*n

        for i in range(1, n):
            # increasing
            if nums[i - 1] < nums[i]:
                new = float('-inf')
                val = nums[i - 1] + nums[i]
                if dp0[i - 1] != 0:
                    new = dp0[i - 1] + nums[i]
                dp0[i] = max(val, new)

            # decreasing
            if nums[i - 1] > nums[i]:
                best_prev_sum = float('-inf')
                if dp1[i - 1] != 0:
                    best_prev_sum = dp1[i - 1]
                if dp0[i - 1] != 0:
                    best_prev_sum = max(best_prev_sum, dp0[i - 1])
                if best_prev_sum != 0:
                    dp1[i] = best_prev_sum + nums[i]
            
            # incresing
            if nums[i - 1] < nums[i]:
                best_prev_sum = float('-inf')
                if dp2[i - 1] != 0:
                    best_prev_sum = dp2[i - 1]
                if dp1[i - 1] != 0:
                    best_prev_sum = max(best_prev_sum, dp1[i - 1])
                if best_prev_sum != 0:
                    dp2[i] = best_prev_sum + nums[i]
        print(dp0)
        print(dp1)
        print(dp2)
        ans = float('-inf')
        for x in dp2:
            ans = max(ans, x)
        return ans