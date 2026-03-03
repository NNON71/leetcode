class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"] * 20
        for i in range(1, 20):
            s[i] = s[i - 1] + "1" + "".join([str(int(b)^1) for b in s[i - 1]][::-1])
        return s[n - 1][k - 1]

    def findKthBit2(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        length = 2 ** n - 1
        mid = length // 2 + 1
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit2(n - 1, k)
        else:
            return str(1 - int(self.findKthBit2(n - 1, length - k + 1)))

# 1545. Find Kth Bit in Nth Binary String