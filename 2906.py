# 2906. Construct Product Matrix
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MOD = 12345
        res = [[0] * n for _ in range(m)]

        pref = 1
        for i in range(m):
            for j in range(n):
                res[i][j] = pref
                pref = (pref * grid[i][j]) % MOD
        
        suff = 1
        for i in range(m - 1, - 1, -1):
            for j in range(n - 1, -1, -1):
                res[i][j] = (res[i][j] * suff) % MOD
                suff = (suff * grid[i][j]) % MOD
        return res