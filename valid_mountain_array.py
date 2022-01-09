'''
run-time: 200 ms, faster than 74.60%
mem-usage: 15.6 mb, less than 60.27%
O(n)
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
                
        maxIdx = None
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                maxIdx = i
            elif arr[i] < arr[i - 1]:
                break
            else:
                return False
        
        if maxIdx == None or maxIdx == len(arr) - 1:
            return False
        
        for i in range(maxIdx + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False
        
        return True
