class Solution:
    def binaryGap(self, n: int) -> int:
        bi = bin(n)[2:]
        p = 0
        _max = 0
        for i in range(len(bi)):
            if bi[i] == '1':
                _max = max(_max, i - p)
                p = i
        return _max

# 868. Binary Gap