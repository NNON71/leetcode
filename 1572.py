class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = 0
        for r in range(m):
            left = mat[r][r]
            right = mat[r][n - 1 - r]
            if r == n - 1 - r:
                res += left
            else:
                res += left + right
        return res