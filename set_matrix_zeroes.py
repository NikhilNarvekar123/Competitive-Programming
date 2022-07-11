class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # O(mn) + O(m + n) space
        # R O(mn) + M O(m + n)
#         rows_to_change = set()
#         cols_to_change = set()
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0:
#                     rows_to_change.add(r)
#                     cols_to_change.add(c)
        
#         # R O(m) + M O(1)
#         for r in rows_to_change:
#             for c in range(len(matrix[0])):
#                 matrix[r][c] = 0
        
#         # R O(n) + M O(1)
#         for c in cols_to_change:
#             for r in range(len(matrix)):
#                 matrix[r][c] = 0
                
    
        # R O(mn) and O(1) m
        # R O(mn) + M O(1)
        first_col_marked = False                
        for r in range(len(matrix)):
            
            if matrix[r][0] == 0:
                first_col_marked = True
            
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # R O(mn) + M O(1)
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
                    
        # R O(n) + M O(1)
        if matrix[0][0] == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        # R O(m) + M O(1)
        if first_col_marked:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        
