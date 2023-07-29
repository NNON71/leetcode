class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        m = (1+x)//2
        while m*m>x:
            m = (1+m)//2
        return m
    
s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(3))
