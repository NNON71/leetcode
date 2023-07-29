class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=0
        check = ['()','[]','{}']
        while i<len(s):
            if s[i:i+2] not in check and s[j]+s[-1-j] not in check:  
                return False
            if s[i:i + 2] in check:
                i += 2
            else:
                j += 1
            if j > len(s) // 2:
                break
        return True
    
    def ch(self,s):
        stack = []  
        mapping = {')': '(', ']': '[', '}': '{'} 

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False 
            else:
                stack.append(char)  
        return not stack 
        
s = Solution()
# print(s.isValid(s = "()")) #true
# print(s.isValid(s = "()[]{}")) #true
# print(s.isValid(s = "(]")) #false
# print(s.isValid(s = "{[]}")) #true
# print(s.isValid(s = "(){}}{")) #false

print(s.ch(s = "()")) #true
print(s.ch(s = "()[]{}")) #true
print(s.ch(s = "(]")) #false
print(s.ch(s = "{[]}")) #true
print(s.ch(s = "(){}}{")) #false