class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        memo = [[1] * i for i in range(1, rowIndex + 2)] 
        if rowIndex > 1 :
            for n in range(3, rowIndex + 2) :
                # print(f"-------{n}")
                for i in range(1, n - 1) :
                    memo[n - 1][i] = memo[n - 2][i - 1] + memo[n - 2][i]
                    # print(i, memo[n - 2][i - 1] + memo[n - 2][i], memo)
        return memo[rowIndex]

"""
118. Pascal's Triangle II
rowIndex = 3
3 - [1, 3, 3, 1]
"""

s = Solution()
# print(s.getRow(3))
print(s.getRow(2))