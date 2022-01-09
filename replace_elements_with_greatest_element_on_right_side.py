'''
O(n)
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxVal = -1
        
        for i in range(len(arr) - 1, -1, -1):
            temp = max(arr[i], maxVal)
            arr[i] = maxVal
            maxVal = temp
            
        return arr
        

        # left-to-right approach that has worst-case n^2 but average O(n)        
        '''
        maxNum = -1
        maxIdx = 0
        
        for i in range(len(arr)):
            if i == maxIdx:
                maxNum = -1
                for j in range(i + 1, len(arr)):
                    if arr[j] > maxNum:
                        maxNum = arr[j]
                        maxIdx = j
                arr[i] = maxNum
            else:
                arr[i] = maxNum
        
        return arr
        '''
