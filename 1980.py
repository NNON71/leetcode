class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numSet = set(nums)
        for i in range(n + 1):
            biNum = bin(i)[2:].zfill(n)
            
            if biNum not in numSet:
                return biNum
            
    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return ''.join(res)