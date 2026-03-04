class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        sumRow = [sum(row) for row in mat]
        sumCol = [sum(col) for col in zip(*mat)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and sumRow[i] == 1 and sumCol[j] == 1:
                    ans += 1
        return ans

"""
1 0 0
0 0 1
1 0 0
sumRow = [1, 0, 1]
sumCol = [2, 0, 1]

sumRow = [1, 0, 1, 1]
sumCol = [2, 0, 1]


"""