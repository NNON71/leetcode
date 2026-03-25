class Solution:
    def canPartitionGrid(self, grid) -> bool:
        m, n = len(grid), len(grid[0])
        
        rowSum = [0] * m
        colSum = [0] * n
        totalRow, totalCol = 0, 0
        for i in range(m):
            for j in range(n):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]
                totalRow += grid[i][j]
                totalCol += grid[i][j]

        leftSum = 0
        for i in range(1, m):
            leftSum += rowSum[i - 1]
            if leftSum == totalRow - leftSum:
                return True 
            
        leftSum = 0
        for j in range(1, n):
            leftSum += colSum[j - 1]
            if leftSum == totalCol - leftSum:
                return True

        return False
    
s = Solution()
grid = [[1,4],[2,3]]
print(s.canPartitionGrid(grid))

