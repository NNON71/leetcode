class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        memo = [[1] * i for i in range(1, numRows + 1)] 
        if numRows > 2 :
            for n in range(3, numRows + 1) :
                # print(f"-------{n}")
                for i in range(1, n - 1) :
                    # print(memo[n - 1][i - 1: i])
                    # print(i, memo[n - 2][i - 1] + memo[n - 2][i], memo)
                    memo[n - 1][i] = memo[n - 2][i - 1] + memo[n - 2][i]
        return memo


"""
118. Pascal's Triangle
3 - 1 [0, 1]
4 - 1 [0, 1], 2 [1, 2]
5 - 1 [0, 1], 2 [1, 2], 3[2, 3]
"""

s = Solution()
print(s.generate(5))