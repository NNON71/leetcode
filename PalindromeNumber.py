class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rex = str(x)[::-1]
        if str(x) == rex:
            return True
        return False

    def fastest(self,x):
        x = str(x)
        return x==x[::-1]
    
s= Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))