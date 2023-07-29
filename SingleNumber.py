class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i
    def fastest(self,nums):
        result = 0
        for num in nums:
            result ^= num
        return result
        
s=Solution()
# print(s.singleNumber(nums = [2,2,1]))
# print(s.singleNumber(nums = [4,1,2,1,2]))
# print(s.singleNumber(nums = [1]))

print(s.fastest(nums = [2,2,1]))
print(s.fastest(nums = [4,1,2,1,2]))
print(s.fastest(nums = [1]))