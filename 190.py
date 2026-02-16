class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b_32 = bin(n)[2:].zfill(32)
        res = 0
        for i in range(31, -1, -1):
            res = (res << 1) | int(b_32[i])
        return res