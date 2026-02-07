class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cum_a = [0] * n
        cum_b = [0] * n

        # count b left -> right
        c = 0
        for i in range(n):
            cum_a[i] = c
            if s[i] == 'b':
                c += 1

        # count a right -> left
        c = 0
        for i in range(n - 1, -1, -1):
            cum_b[i] = c
            if s[i] == 'a':
                c += 1
        
        mid = n
        for i in range(n):
            mid = min(mid, cum_a[i] + cum_b[i])
        return mid 

    
    def minimumDeletions2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if s[i - 1] == 'a':
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])
        
        return min(dp[n][0], dp[n][1])