# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        q.append(root)
        curr_level = 0
        res = []

        while q:
            n = len(q)
            _sum = 0
            for _ in range(n):
                node = q.popleft()
                _sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr_level += 1
            res.append(_sum/n)
           
        return res