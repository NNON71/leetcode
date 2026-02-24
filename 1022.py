# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, s):
            s = (s << 1) | root.val  

            if not root.left and not root.right:
                self.res += s
                return
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
        dfs(root, 0)
        return self.res

# 1022. Sum of Root To Leaf Binary Numbers