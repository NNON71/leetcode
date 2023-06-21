class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs)
        st = strs[0]   
        ed = strs[-1]
        ans = ""
        for i in range(min(len(st),len(ed))):
            if st[i] != ed[i]:
               return ans 
            ans += st[i]
        return ans
    
    def faster(self,strs):
        prefix = ''
        minlen = min(len(i) for i in strs)
        for i in range(0,minlen):
            if len(set([l[i] for l in strs])) != 1:
                return prefix    
            prefix += strs[0][i] 
        return prefix  
        
s=Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))
print(s.longestCommonPrefix(strs = ["aaa","aa","aaa"]))