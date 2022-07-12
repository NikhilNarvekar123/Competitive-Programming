# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # recursive stack - dfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        elif not root.left and not root.right:
            return root
        
        new_right = self.invertTree(root.left)
        new_left = self.invertTree(root.right)
        
        root.left = new_left
        root.right = new_right
        
        return root
    
    # queue - bfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        queue = deque()
        queue.appendleft(root)
        
        while len(queue):
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        
        return root
    
    # stack - dfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        stack = deque()
        stack.append(root)
        
        while len(stack):
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root
        
        
