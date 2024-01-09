# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        res = []
        def dfs(root):
            
            if not root:
                return False
            if not root.left and not root.right: 
                res.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
            
            return res 
      
        r1 = dfs(root1)
        # print(r1)
        res = []
        r2 = dfs(root2)
        # print(r2)
        
        if r1 == r2:
            return True
        return False