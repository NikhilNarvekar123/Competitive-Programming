'''
run-time: 36 ms (faster than 95.96%)
mem-usage: 15.1 mb (less than 84.03%)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def recur(node, val):
            
            if node == None:
                return 0
            
            val += node.val

            if node.right == None and node.left == None:
                return targetSum == val
            
            left = recur(node.left, val)
            right = recur(node.right, val)
            
            return left or right
                        
            
        return recur(root, 0)
