'''
run-time: 54 ms, faster than 6.32%
mem-usage: 14 mb, less than 94.92%
O(m*n) so still meets required problem criteria
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        counter = 0
        result = []
        
        visited = set()
        
        direction = 'right'
        
        while counter != (m * n):
            
            result.append(matrix[i][j])
            visited.add('{}{}'.format(i,j))
            
            temp_i, temp_j = i, j
            
            if direction == 'right':
                temp_j += 1
            elif direction == 'down':
                temp_i += 1
            elif direction == 'left':
                temp_j -= 1
            elif direction == 'up':
                temp_i -= 1
            
            key = '{}{}'.format(temp_i, temp_j)
            
            if temp_j >= n or (key in visited and direction == 'right'):
                direction = 'down'
                temp_j = j
                temp_i = i + 1
            elif temp_i >= m or (key in visited and direction == 'down'):
                direction = 'left'
                temp_i = i
                temp_j = j - 1
            elif temp_j < 0 or (key in visited and direction == 'left'):
                direction = 'up'
                temp_j = j
                temp_i = i - 1
            elif temp_i < 0 or (key in visited and direction == 'up'):
                direction = 'right'
                temp_i = i
                temp_j = j + 1
            
            i = temp_i
            j = temp_j
            counter += 1
        
        return result
            
