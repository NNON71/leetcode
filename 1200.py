class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        n = len(arr)
        arr = sorted(arr)
        _min_diff = arr[1] - arr[0]
        res = [[arr[0], arr[1]]]
        for i in range(2, n):
            val = abs(arr[i] - arr[i - 1])
            if val < _min_diff:
                _min_diff = val
                res = [[arr[i - 1], arr[i]]]
            elif val == _min_diff:
                res.append([arr[i - 1], arr[i]])
            else:
                continue
        return res
        
        # for i in range(n-1):
        #     for j in range(i + 1, n):
        #         val = abs(arr[j] - arr[i])
        #         if val == _min_diff:
        #             res.append([arr[i], arr[j]])
        #         elif val < _min_diff:
        #             res = []
        #             _min_diff = val
        #             res.append([arr[i], arr[j]])
        #         else:
        #             continue
        # return res