from collections import deque

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        if amount == 0:
            return 0
        

        queue = deque([(0, 0)])
        visited = [True] + [False] * amount

        while queue:
            
            totalCoins, currVal = queue.popleft()
            totalCoins += 1 # take a coin
            
            for coin in coins:
                
                nextVal = currVal + coin # add next coin
                
                if nextVal == amount:  # Find a combination.
                    return totalCoins

                if nextVal < amount: 
                    if not visited[nextVal]:  # Current value not checked.
                        visited[nextVal] = True  # Prevent checking again.
                        queue.append((totalCoins, nextVal))
            
            
    
        return -1
            
        
#         def dfs(val, count, curMin):
            
#             if val == 0:
#                 return count
#             if val < 0:
#                 return -1
            
            
#             for coin in coins:
                
#                 temp = dfs(val - coin, count + 1, curMin)
                
#                 if temp != -1:
#                     if curMin != None:
#                         curMin = min(temp, curMin)
#                     else:
#                         curMin = temp
#                 else:
#                     break
                
            
#             if curMin == None:
#                 return -1
#             else:
#                 return curMin
            
            
            
