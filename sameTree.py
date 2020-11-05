# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if(p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        '''
        t1 = []
        t2 = []
        self.buildTree(p, t1)
        self.buildTree(q, t2)
        print(t1,t2)
        if t1 == t2:
            return True
        return False
        '''
        
    
    
    def buildTree(self, p : TreeNode, t1 : List[int]):
        
        if(p):
            if(p.left):
                self.buildTree(p.left, t1)
            t1.append(p.val)
            self.buildTree(p.right, t1)
        else:
            t1.append(None)
