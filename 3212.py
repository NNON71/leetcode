#3212. Count Submatrices With Equal Frequency of X and Y
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [0] * n
        dy = [0] * n
        cnt = 0
        for i in range(m):
            rx, ry = 0, 0
            for j in range(n):
                if grid[i][j] == 'X':
                    rx += 1
                elif grid[i][j] == 'Y':
                    ry += 1
                
                dx[j] += rx
                dy[j] += ry

                if dx[j] > 0 and dx[j] == dy[j]:
                    cnt += 1
        return cnt