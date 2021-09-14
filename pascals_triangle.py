'''
run-time: 56 ms, faster than 5.83%
mem-usage: 14.1 mb, less than 81.14%
Still uses dynamic programming approach with high efficiency
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # base cases        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        
        result = [[1],[1,1]]
    
        for i in range(numRows - 2):
            
            row = result[len(result) - 1]
            i = 0
            
            newRow = [1]
            
            while i + 1 < len(row):
                newRow.append(row[i] + row[i+1])
                i += 1
            
            newRow.append(1)
            
            result.append(newRow)
        
        return result
