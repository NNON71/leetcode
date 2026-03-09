class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        self.res = 0
        def dfs(zNum, oNum, arr, cZero, cOne):
            if zNum == 0 and oNum == 0:
                self.res += 1 
                return
            if zNum > 0 and cZero < limit:
                dfs(zNum - 1, oNum, arr + [0], cZero + 1, 0)
            if oNum > 0 and cOne < limit:
                dfs(zNum, oNum - 1, arr + [1], 0, cOne + 1)
        dfs(zero, one, [], 0, 0)
        return self.res % (10**9 + 7)
    
    def numberOfStableArrays2(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        MOD = 10**9 + 7

        for i in range((min(zero, limit) + 1)):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD

                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % MOD
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD

                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD