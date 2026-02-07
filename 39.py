class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def combine(nums, idx, totals):
            if totals == target:
                res.append(nums[:])
                return
            if totals > target or idx >= len(candidates):
                return
            nums.append(candidates[idx])
            combine(nums, idx, totals + candidates[idx])
            nums.pop()
            combine(nums, idx + 1, totals)

        combine([], 0, 0)
        return res

