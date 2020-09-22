class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        
        j = len(height) - 1
        i = 0
        maxArea = 0
        
        while i != j:
            x = abs(j - i)
            y = height[j] if height[j] < height[i] else height[i]
            maxArea = x * y if x * y > maxArea else maxArea
            
            if height[j] > height[i]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            else:
                i += 1
        
        return maxArea
            
            
        
            
        
        
        ''' old solution
        maxArea = 0
        
        for i in range(0, len(height) - 1):
            
            num1 = height[i]
            
            for j in range(i + 1, len(height)):
                num2 = height[j]
                
                area = j - i
                area = area * num1 if num1 < num2 else area * num2
                maxArea = area if area > maxArea else maxArea  
        
        return maxArea
        '''
