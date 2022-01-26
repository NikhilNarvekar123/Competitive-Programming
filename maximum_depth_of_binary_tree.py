'''
O(V+E)
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxDepth = -1
        
        def dfs(node, count):
            nonlocal maxDepth
        
            if not node:
                maxDepth = max(maxDepth, count)
                return
        
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        
        dfs(root, 0)
        return maxDepth
