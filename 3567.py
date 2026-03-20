# 3567. Minimum Absolute Difference in Sliding Submatrix

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                val = set()
                for x in range(k):
                    for y in range(k):
                        val.add(grid[i + x][j + y])
                
                val = sorted(val)
                if len(val) == 1:
                    row.append(0)
                else:
                    minDiff = float('inf')
                    for idx in range(len(val) - 1):
                        minDiff = min(minDiff, abs(val[idx] - val[idx + 1]))
                    row.append(minDiff)
            ans.append(row)
        
        return ans