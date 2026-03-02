class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxRight = [0] * m
        for i in range(m):
            rightmost = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    break
                rightmost += 1
            maxRight[i] = rightmost

        ans = 0
        for k in range(n - 1, 0, -1):
            for x in maxRight:
                if x >= k:
                    maxRight.remove(x)
                    break
                ans += 1
            else:
                return -1

        return ans