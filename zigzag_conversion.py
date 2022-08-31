class Solution:
    def convert(self, s: str, numRows: int) -> str:
                
        '''
        simplify by realizing columns not needed in matrix, just rows
        '''
        
        if numRows == 1:
            return s
        
        rows = ['' for _ in range(numRows)]
        goingDown = False
        curRow = 0
        
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        
        res = ''
        for row in rows:
            res += row
        
        return res
        
        
        '''        
        m = len(s)
        mat = [[''] * m for _ in range(numRows)]
        
        # fill in matrix
        r = c = 0
        direction = -1
        for i in range(len(s)):
            mat[r][c] = s[i]
            if direction == -1:
                if r >= numRows - 1:
                    direction = 1
                    r -= 1
                    c += 1
                else:
                    r += 1
            else:
                if r <= 0:
                    direction = -1
                    r += 1 
                else:
                    r -= 1
                    c += 1
        
        # scan each row for final answer
        res = ''
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] != '':
                    res += mat[r][c]
        
        return res
        '''
