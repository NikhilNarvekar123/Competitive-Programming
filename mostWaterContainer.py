'''
O(n)
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        
        maxVol = -1
        while i < j:

            vol = (j - i) * min(height[i], height[j])
            maxVol = max(vol, maxVol)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return maxVol
