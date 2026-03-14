# 1415. The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def dfs(i, s):
            if i == n:
                res.append(s[:])
                return 
            prev = s[-1]
            if prev == 'a':
                dfs(i + 1, s + 'b')
                dfs(i + 1, s + 'c')
            if prev == 'b':
                dfs(i + 1, s + 'a')
                dfs(i + 1, s + 'c')
            if prev == 'c':
                dfs(i + 1, s + 'a')
                dfs(i + 1, s + 'b')
        dfs(1, "a")
        dfs(1, 'b')
        dfs(1, 'c')
        if len(res) < k:
            return ""
        return res[k - 1]   
    
    def getHappyString2(self, n: int, k: int) -> str:
        self.count = 0
        self.res = ""
        
        def dfs(s):
            if self.res:
                return 
            
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.res = s
                return
            
            for char in ['a', 'b', 'c']:
                if not s or s[-1] != char:
                    dfs(s + char)
            
        dfs("")
        return self.res