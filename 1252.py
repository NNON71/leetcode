class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0] * n for _ in range(m)]
        for x, y in indices:
            for r in range(m):
                matrix[r][y] += 1
            for c in range(n):
                matrix[x][c] += 1

        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] % 2 == 1:
                    res += 1
        return res

