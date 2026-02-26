class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        n = 0
        for i in range(len(s)):
            n = (n << 1) | int(s[i])
        
        while n > 1:
            cnt += 1
            if n%2 == 0:
                n = n//2
            else:
                n += 1
        return cnt

# 1404. Number of Steps to Reduce a Number in Binary Representation to One