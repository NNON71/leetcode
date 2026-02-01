class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1
        while l <= r :
            m = (l + r) // 2
            if letters[m] > target:
                r = m - 1
            else:
                l = m + 1
        return letters[l % len(letters)]