class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(4):
            if i < 2 and s1[i] != s2[i] and (s1[i + 2] != s2[i] or s1[i] != s2[i + 2]):
                return False
            elif i >= 2 and s1[i] != s2[i] and (s1[i - 2] != s2[i] or s1[i] != s2[i - 2]):
                return False
            
        return True