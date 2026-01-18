class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(size, r, c):
            # Base
            targetSum = sum([grid[r][c+j] for j in range(size)])

            # Diagonal
            diag1 = diag2 = 0
            for i in range(size):
                diag1 += grid[r + i][c + i]
                diag2 += grid[r + i][c + size - 1 - i]
            if diag1 != targetSum or diag2 != targetSum:
                return False
            
            # Row
            for i in range(1, size):
                s = 0
                for j in range(size):
                    s += grid[r + i][c + j]
                if s != targetSum:
                    return False
            
            # Col
            for i in range(size):
                s = 0
                for j in range(size):
                    s += grid[r + j][c + i]
                if s != targetSum:
                    return False
            return True

        rows, cols = len(grid), len(grid[0])

        max_size = min(rows, cols)

        for size in range(max_size, 1, -1):
            for r in range(rows - size + 1):
                for c in range(cols - size + 1):
                    if isMagic(size, r, c):
                        return size
        return 1