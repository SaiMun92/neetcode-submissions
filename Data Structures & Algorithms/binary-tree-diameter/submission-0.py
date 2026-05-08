# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node):
        if not node:
            return 0
        
        leftDepth = self.dfs(node.left)
        rightDepth = self.dfs(node.right)

        self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use dfs for this
        self.maxDiameter = 0
        self.dfs(root)
        return self.maxDiameter
        