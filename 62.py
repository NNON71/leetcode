class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # def recursive(x, y):
        #     if x < 0 or y < 0:
        #         return 0
        #     if x >= n or y >= m:
        #         return 0
        #     if x == n - 1 and y == m - 1:
        #         return 1

        #     return recursive(x, y + 1) + recursive(x + 1, y)
        # return recursive(0, 0)

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
