'''
dfs becomes O(n) when memoization used
true dfs O(n)
both solutions O(n) mem space
'''

class Solution:
    
    def climbStairs(self, n: int) -> int:

        # dfs with memoization
        memo = {}
        
        def dfs(val):
            
            if val == n:
                return 1
            elif val > n:
                return 0
            
            if not (val in memo):
                memo[val] = dfs(val + 1) + dfs(val + 2)
            
            return memo[val]
                
        dfs(0)
        return memo[0]
    
    
        # true dp (bottom-up)
#         dp = [0] * (n + 1)
        
#         for i in range(n, -1, -1):
#             if i + 2 <= n:
#                 dp[i] = dp[i + 1] + dp[i + 2]
#             else:
#                 dp[i] = 1
        
#         return dp[0]
