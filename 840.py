class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(row, col):
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[row + i][col + j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True

            # Diagonal
            diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diag2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
            if diag1 != diag2 :
                return False
            
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
            if not (row1 == diag1 and row2 == diag1 and row3 == diag1):
                return False

            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
            if not (col1 == diag1 and col2 == diag1 and col3 == diag1):
                return False

            return True

        ans = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    ans += 1
        return ans 