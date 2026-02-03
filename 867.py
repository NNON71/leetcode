class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        newMatrix = [[0] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                newMatrix[c][r] = matrix[r][c]
        return newMatrix