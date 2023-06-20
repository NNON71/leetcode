class Solution(object):
    def twoSum(self, nums, target):
            for i in range(len(nums)-1):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
            return []

    def twoSum1(self,nums,target):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
                print(d)
            else:
                return [i,d[nums[i]]]
                
solution = Solution()
print(solution.twoSum1(nums = [2,7,11,15], target = 9))
print(solution.twoSum1(nums = [3,2,3], target = 6))
print(solution.twoSum1(nums = [3,3], target = 6))