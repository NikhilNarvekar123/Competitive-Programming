# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        return self.helper(root, math.inf, -math.inf)    
    
    def helper(self, root, lessThan, largerThan):
        
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        
        left = self.helper(root.left, min(lessThan, root.val), largerThan)
        right = self.helper(root.right, lessThan, max(largerThan, root.val))
        return left and right
        

        
