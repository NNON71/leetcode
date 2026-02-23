class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m = set()
        n = len(s)
        for i in range(n - k + 1):
            subset = s[i:i + k]
            if subset not in m:
                m.add(subset)
        return len(m) == 2 ** k
                
                
# 1461. Check If a String Contains All Binary Codes of Size K