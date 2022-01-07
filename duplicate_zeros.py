'''
run-time: 1286 ms, faster than 9.26%
mem-usage: 15.1 mb, less than 7.96%\
Still O(1) mem space (in-space modification)
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        i = 0
        
        while i < len(arr):
            if arr[i] == 0:
                nextVal = 0
                for j in range(i + 1, len(arr)):
                    temp = arr[j]
                    arr[j] = nextVal
                    nextVal = temp
                i += 1
            i += 1
                
