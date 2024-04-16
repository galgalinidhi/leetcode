# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        # Otherwise, recursively insert the new nodes
        self.insert(val, root, 1, depth)
        return root
    
    def insert(self, val: int, node: TreeNode, depth: int, n: int) -> None:
        if not node:
            return
        if depth == n - 1:
            # Insert new nodes at the desired depth
            left_temp = node.left
            node.left = TreeNode(val)
            node.left.left = left_temp
            right_temp = node.right
            node.right = TreeNode(val)
            node.right.right = right_temp
        else:
            # Recursively insert at the next level
            self.insert(val, node.left, depth + 1, n)
            self.insert(val, node.right, depth + 1, n)