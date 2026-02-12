class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            cnt = [0] * 26
            uniq = maxfreq = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                if cnt[idx] == 0:
                    uniq += 1
                cnt[idx] += 1

                if cnt[idx] > maxfreq:
                    maxfreq = cnt[idx]

                curr_len = j - i + 1
                if maxfreq * uniq == curr_len:
                    res = max(res, curr_len)
        return res
