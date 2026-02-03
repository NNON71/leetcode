class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        n = len(image)
        for c in range(n):
            row = []
            for r in range(n - 1, -1, -1):
                n_r = 0 if image[c][r] == 1 else 1
                row.append(n_r)
            res.append(row)
        return res
                

"""
[[1,1,0],
 [1,0,1],
 [0,0,0]]

[[0,1,1],
 [1,0,1],
 [0,0,0]].

 [[1,0,0],
  [0,1,0],
  [1,1,1]]
"""