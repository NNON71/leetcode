class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        p = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                p[r][c] = p[r - 1][c] + p[r][c - 1] - p[r - 1][c - 1] + mat[r - 1][c - 1]
        
        def getRect(x1, y1, x2, y2):
            return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]

        r, ans = min(rows, cols), 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                for c in range(ans + 1, r + 1):
                    if (
                        i + c - 1 <= rows
                        and j + c - 1 <= cols
                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
                    ):
                        ans += 1
                    else:
                        break
        return ans