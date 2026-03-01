class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for x in n:
            res = max(int(x), res)
        return res

# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers