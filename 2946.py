# 2946. Matrix Similarity After Cyclic Shifts
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i % 2 == 0 and mat[i][(j + k) % n] != mat[i][j]:
                    return False
                elif i % 2 == 1 and mat[i][(j - k) % n] != mat[i][j] :
                    return False
        return True  