class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        cnt = [0, 0]
        for i in range(n):
            b1 = str(i%2)
            b2 = str((i+1)%2)
            if b1 != s[i]:
                cnt[0] += 1
            if b2 != s[i]:
                cnt[1] += 1
        return min(cnt)
        
    def minOperations2(self, s: str) -> int:
        count = 0
        for i in range (len(s)):
            if i % 2:
                if s[i] == "0":
                    count += 1
            else:
                if s[i] == "1":
                    count +=1
        return min(count,len(s) - count)

# Minimum Changes To Make Alternating Binary String