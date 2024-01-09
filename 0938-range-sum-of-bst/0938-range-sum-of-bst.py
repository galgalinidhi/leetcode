# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
       
        def dfs(root, add):
            if not root:
                return add
            if root.val>= low and root.val<=high:
                add+=root.val
                
            
            add = dfs(root.left,add)
            add = dfs(root.right,add)
            
            return add
       
        
    
        return(dfs(root,0))
            
            
            
            