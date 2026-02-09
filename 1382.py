# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, vals):
        if not root:
            return 
        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)
    
    def build(self, vals, l, r):
        if l> r:
            return None
        mid = (l + r) // 2
        tree = TreeNode(vals[mid])
        tree.left = self.build(vals, l, mid - 1)
        tree.right = self.build(vals, mid + 1, r)
        return tree

    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        vals = []
        self.inorder(root, vals)
        return self.build(vals, 0, len(vals) - 1)


