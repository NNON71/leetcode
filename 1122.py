class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        h = {}
        for i in arr1:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        res = []
        for i in arr2:
            while h[i] > 0:
                res.append(i)
                h[i] -= 1
        
        temp = []
        for k,v in h.items():
            for _ in range(v):
                temp.append(k)
        temp.sort()
        return res + temp
