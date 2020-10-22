class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowCount = set()
        

        for r in range(0 , len(board)):   
            
            for c in range(0, len(board)):
                
                val = board[r][c]
                print(val)
                
                if(val == '.'):
                    continue
                
                if((val + " r: " + str(r)) in rowCount):
                    return False
                else:
                    rowCount.add(val + " r: " + str(r))
                
                if((val + " c: " + str(c)) in rowCount):
                    return False
                else:
                    rowCount.add(val + " c: " + str(c))
                
                if((val + " b: " + str(r//3) + " " + str(c//3)) in rowCount):
                    return False
                else:
                    rowCount.add(val + " b: " + str(r//3) + " " + str(c//3))
                
                
        
        return True
        
        
        
        
        
        
        
        '''
                rowCount = [{'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0 }] * 9
            colCount = [{'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0 }] * 9
            boxCount = [[{'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0 }] * 3] * 3
      
        
                row = rowCount[r]
                col = colCount[c]
                box = boxCount[r // 3][c // 3]
                
                if(row[val] != 0):
                    print(row)
                    return False
                else:
                    row[val] = 1
                    print(row)
                    
                if(col[val] != 0):
                    print("col")
                    return False
                else:
                    col[val] = 1
        
                if(box[val] != 0):
                    print("box")
                    return False
                else:
                    box[val] = 1
        
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        '''
        
        
        
        for row in board:
            
            for col in row:
                if(col == "."):
                    continue
                elif(rowCount[col] != 0):
                    return False
                elif(rowCount[col] == 0):
                    rowCount[col] = 1
                
            rowCount = {'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0, }
    
        rowCount = {'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0, }
        
        for col in range(len(board)):
            
            for row in range(len(board)):
                val = board[row][col]
                if(val == "."):
                    continue
                elif(rowCount[val] != 0):
                    return False
                elif(rowCount[val] == 0):
                    rowCount[val] = 1
                    
            rowCount = {'1' : 0, '2' : 0, '3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0, '8' : 0, '9' : 0, }
        
        return True
        '''
