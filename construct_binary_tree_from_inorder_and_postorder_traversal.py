'''
run-time: 164 ms (faster than 40.88%)
mem-usage: 53.3 mb (lower than 35.03%)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(postorder.pop())
        
        if len(inorder) > 1:
            
            rightArr = inorder[inorder.index(root.val)+1:]
            leftArr = inorder[:inorder.index(root.val)]
        
            if len(rightArr) != 0:
                root.right = self.buildTree(rightArr, postorder)
            if len(leftArr) != 0:
                root.left = self.buildTree(leftArr, postorder)
        
        return root
