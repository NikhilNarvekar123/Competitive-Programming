'''
demo prob
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        res = []
        
        res.append(root.val)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        res += left if len(left) != 0 else []
        res += right if len(right) != 0 else []
        
        return res
        
