'''
run-time: 28 ms (faster than 91.27%)
mem-usage: 14.5 (less than 18.60%)
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # initialize matrix
        m = [[None] * n for i in range(n)]
        nums = [i for i in range(n*n, 0, -1)]
        
        top = 0
        bottom = len(m)
        left = 0
        right = len(m[0])
        
        
        while top < bottom and left < right:
            
            # go right and increase top border
            for i in range(left, right):
                m[top][i] = nums.pop()
            top += 1
            
            # go down and decrease right border
            for i in range(top, bottom):
                m[i][right-1] = nums.pop()
            right -= 1
            
            # already iterated over the last row or last column
            if top == bottom or left == right: 
                break
            
            # go left and decrease bottom border
            for i in range(right-1, left-1, -1):
                m[bottom-1][i] = nums.pop()
            bottom -= 1
            
            # go up and increase left border
            for i in range(bottom-1, top-1, -1):
                m[i][left] = nums.pop()
            left += 1
        
        return m
