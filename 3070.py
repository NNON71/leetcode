# 3070. Count Submatrices with Top-Left Element and Sum Less Than k
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0 if grid[0][0] > k else 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] = grid[i][j] + grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
                if grid[i][j] > k:
                    break
                cnt += 1
        return cnt
