# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root == None or not (root.left or root.right):
            return True
        
        
        def check(left, right):
            
            if left == None and right == None:
                return True
            elif (left and not right) or (right and not left):
                return False
            
            if left.val == right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else:
                return False
        
        
        return check(root.left, root.right)
