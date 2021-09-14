'''
run-time: 188 ms, faster than 85.37%
mem-usage: 16.7 MB, less than 83.85%
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        i = 0
        j = 0
        r = len(mat)
        c = len(mat[0])
        result = []
        direction = 1 # 1 - up, -1 - down
        
        while (i >= 0 and j >= 0) and (i < r and j < c):
            
            result.append(mat[i][j])
            
            # if everything in bounds keep going
            if (-direction + i >= 0 and direction + j >= 0) and (-direction + i < r and direction + j < c):
                i += -direction
                j += direction
                continue
            
            if direction == 1:
                if j + 1 < c:
                    j += 1
                else:
                    i += 1
                direction = -1
            elif direction == -1:
                if i + 1 < r:
                    i += 1
                else:
                    j += 1
                direction = 1
            
        return result
            
