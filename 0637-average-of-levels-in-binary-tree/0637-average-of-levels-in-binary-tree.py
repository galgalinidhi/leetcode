# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        q = deque([root])
        while q:
            count = 0
            level_sum = 0
            for i in range(len(q)):
                
                node = q.popleft()
                level_sum += node.val
                count+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum/count) 
            
            
        return res    