# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #---------- SOLUTION 1 ----------
        # self.max_sum = float('-inf')
        # self.total = 0

        # def dfs_total(root) :
        #     if not root :
        #         return 
        #     self.total += root.val 
        #     dfs_total(root.left) 
        #     dfs_total(root.right)

        # def dfs(root) :
        #     if not root :
        #         return 0
        #     sub_tree = root.val + dfs(root.left) + dfs(root.right)
        #     self.max_sum = max(self.max_sum, (self.total - sub_tree) * sub_tree)
        #     return sub_tree
        
        # dfs_total(root)
        # dfs(root)
        # return self.max_sum % (10**9 + 7)
        
        
        #---------- SOLUTION 2 ----------
        self.sub_tree = []
        
        def dfs(root) :
            if not root :
                return 0
            sub = root.val + dfs(root.left) + dfs(root.right)
            self.sub_tree.append(sub)
            return sub
               
        total = dfs(root)
        return max([(total - i) * i for i in self.sub_tree]) % (10**9 + 7)