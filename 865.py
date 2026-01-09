# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        import collections
        q = collections.deque()
        q.append(root)
    
        last_level = []    
        parent = {root: None}

        while q :
            len_q = len(q)
            last_level = []
            for _ in range(len_q):
                node = q.popleft()
                last_level.append(node)

                if node.left :
                    parent[node.left] = node
                    q.append(node.left)
                if node.right :
                    parent[node.right] = node
                    q.append(node.right)
        
        deepest = set(last_level)

        while len(deepest) > 1 :
            deepest = {parent[node] for node in deepest}

        return deepest.pop()