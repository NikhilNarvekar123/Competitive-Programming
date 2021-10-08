from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        if root == None:
            return []
    
        res = []
        visited = set()
        queue = deque()
        queue.append(root)
        
        
        while len(queue) != 0:
        
            curr = []
            
            for i in range(len(queue)):
                
                node = queue.popleft()
                curr.append(node.val)
                visited.add(node)
            
                if not (node.left in visited) and node.left:
                    queue.append(node.left)
                if not (node.right in visited) and node.right:
                    queue.append(node.right)
            
            res.append(curr)
        
        return res
        
        
