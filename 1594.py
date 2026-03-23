# 1594. Maximum Non Negative Product in a Matrix
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 : 
                    grid[i][j] = grid[i][j], grid[i][j]
                elif i == 0 and j > 0 :
                    grid[i][j] = grid[i][j - 1][0] * grid[i][j], grid[i][j - 1][1] * grid[i][j]
                elif i > 0 and j == 0 :
                    grid[i][j] = grid[i - 1][j][0] * grid[i][j], grid[i - 1][j][1] * grid[i][j]
                else:
                    nums = [grid[i - 1][j][0] * grid[i][j], grid[i][j - 1][0] * grid[i][j],
                            grid[i - 1][j][1] * grid[i][j], grid[i][j - 1][1] * grid[i][j]]
                    small, large = min(nums), max(nums)
                    grid[i][j] = (small, large)
        return grid[m-1][n-1][1]%MOD if grid[m-1][n-1][1] >= 0 else -1