class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        mid = len(nums1)//2
        if len(nums1)%2 != 0:
            return "%.05f"%float(nums1[mid])
        else:
            return "%.05f"%float((nums1[mid]+nums1[mid-1])/2)
        
s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

