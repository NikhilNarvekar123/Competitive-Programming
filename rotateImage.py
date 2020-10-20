class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        
        # same basic solution only a bit more efficient
        n = len(matrix)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c] , matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            row.reverse()
        
        
        
        ''' slightly slower solution due to extra variables
        for r in range(len(matrix)):
            matrix.insert(0, matrix.pop(r))
        
        
        col = 0
        
        for r in range(len(matrix)):
            
            for c in range(col, len(matrix)):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
            
            col += 1
            
            
        '''
